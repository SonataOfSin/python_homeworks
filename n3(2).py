import string 
txt = input("Enter a sentence: ")
cleaned_sentence = txt.translate(str.maketrans("", "", string.punctuation)) # The translate() method is used to remove all punctuation characters from the input sentence. The str.maketrans() function creates a translation table that maps each punctuation character to None, effectively removing them from the sentence. The cleaned sentence is then stored in the variable cleaned_sentence.
words = cleaned_sentence.split()
longest_word = max(words, key=len)
print(f"longest word is: '{longest_word}'")
print(f"its length is: {len(longest_word)} characters.")
# პირველი ხაზი იმპორტირებს string მოდულს, რომელიც შეიცავს სხვადასხვა სტრინგის ოპერაციებს და კონსტანტებს.
# მეორე ხაზი იღებს მომხმარებლისგან წინადადებას.
# მესამე ხაზი იყენებს translate() მეთოდს და str.maketrans() ფუნქციას წინადადებისგან ყველა პუნქტუაციის სიმბოლოს მოსაშორებლად. ეს უზრუნველყოფს, რომ პუნქტუაცია არ იქნეს გათვალისწინებული სიტყვების სიგრძის შედარებისას.
# მეოთხე ხაზი იყენებს split() მეთოდს წინადადების სიტყვებად დაყოფისთვის.
# მეხუთე ხაზი იყენებს max() ფუნქციას longest_word ცვლადში ყველაზე გრძელი სიტყვის შესანახად. key=len არგუმენტი max() ფუნქციას ეუბნება, რომ სიტყვების სიგრძე უნდა გამოიყენოს შედარებისთვის.
# მეექვსე და მეშვიდე ხაზები დაბეჭდავს longest_word ცვლადში შენახულ ყველაზე გრძელ სიტყვას და მისი სიგრძეს შესაბამის შეტყობინებებთან ერთად. 
