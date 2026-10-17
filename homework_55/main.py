import argparse
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sklearn.metrics.pairwise import cosine_similarity


EMBEDDING_MODEL = "models/gemini-embedding-001"
EXAMPLE_QUESTIONS = [
    "რამდენი ღირს ოთხი ადამიანისთვის განკუთვნილი ნომერი?",
    "საუზმე შედის ნომრის ფასში?",
    "შემიძლია თუ არა ჯავშნის გაუქმება ჩამოსვლამდე ერთი დღით ადრე?",
    "რომელ საათზე უნდა დავტოვო ნომერი?",
    "რა აქტივობებია ხელმისაწვდომი სტუმრებისთვის?",
    "რა პირობებია შინაური ცხოველის წამოყვანისთვის?",
    "რა მოხდება, თუ ჯავშნის გარეშე კი არა, დაჯავშნილი ნომრით საერთოდ არ მივალ?",
]


def load_chunks(markdown_path: Path) -> list[Document]:
    documents = UnstructuredMarkdownLoader(str(markdown_path)).load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )
    chunks = splitter.split_documents(documents)
    if not chunks:
        raise ValueError(f"No text was found in {markdown_path}.")
    return chunks


def print_similar_chunks(
    question: str,
    chunks: list[Document],
    embeddings: GoogleGenerativeAIEmbeddings,
    chunk_vectors: list[list[float]],
) -> None:
    question_vector = embeddings.embed_query(question)
    similarities = cosine_similarity([question_vector], chunk_vectors)[0]
    ranked_indices = sorted(
        range(len(similarities)),
        key=lambda index: similarities[index],
        reverse=True,
    )

    print(f"\nQuestion: {question}")
    for rank, index in enumerate(ranked_indices[:3], start=1):
        print(f"\n{rank}. Similarity: {similarities[index]:.4f}")
        print(chunks[index].page_content)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Find the most relevant hotel information for a question."
    )
    parser.add_argument(
        "--examples",
        action="store_true",
        help="Run the example questions from the homework prompt.",
    )
    args = parser.parse_args()

    load_dotenv(Path(__file__).with_name(".env"))
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set. Add it to homework_55/.env.")

    markdown_path = Path(__file__).with_name("hotel_info.md")
    chunks = load_chunks(markdown_path)
    embeddings = GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=api_key,
    )
    chunk_vectors = embeddings.embed_documents(
        [chunk.page_content for chunk in chunks]
    )

    questions = (
        EXAMPLE_QUESTIONS
        if args.examples
        else [input("Enter your question: ").strip()]
    )
    for question in questions:
        if not question:
            raise ValueError("The question cannot be empty.")
        print_similar_chunks(question, chunks, embeddings, chunk_vectors)


if __name__ == "__main__":
    main()
