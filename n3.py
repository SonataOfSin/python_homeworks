sentence = input("enter sentence: ")
word_to_replace = input("enter word to replace: ")
new_word = input("enter new word: ")
updated_sentence = sentence.replace(word_to_replace, new_word) 
print(f"updated sentence: {updated_sentence}")
# პირველი ხაზი იღებს მომხმარებლისგან წინადადებას.
# მეორე ხაზი იღებს მომხმარებლისგან სიტყვას, რომელსაც ისინი სურთ შეცვალონ.
# მესამე ხაზი იღებს მომხმარებლისგან ახალ სიტყვას, რომელიც მათ სურთ გამოიყენონ.
# მეოთხე ხაზი იყენებს replace() მეთოდს წინადადებისგან word_to_replace სიტყვას new_word სიტყვით შეცვლის და შედეგს შეინახავს updated_sentence ცვლადში.
# მეხუთე ხაზი დაბეჭდავს updated_sentence ცვლადში შენახულ განახლებულ წინადადებას შესაბამის შეტყობინებასთან ერთად.    
# შენიშვნა: replace() მეთოდი შეცვლის წინადადების ყველა შემთხვევას word_to_replace სიტყვით new_word სიტყვით. თუ თქვენ მხოლოდ პირველი შემთხვევის შეცვლას გსურთ, შეგიძლიათ გამოიყენოთ მესამე არგუმენტი, რომელიც განსაზღვრავს რამდენი შემთხვევა უნდა შეიცვალოს. მაგალითად: sentence.replace(word_to_replace, new_word, 1) მხოლოდ პირველი შემთხვევის შეცვლას მოახდენს.