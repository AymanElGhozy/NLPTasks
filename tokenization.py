import nltk
nltk.download('punkt')

def tokenize_words(text):
    tokens = nltk.word_tokenize(text)
    print("Tokenized Words:")
    for token in tokens:
        print(token)

def tokenize_sentences(text):
    sentences = nltk.sent_tokenize(text)
    print("Tokenized Sentences:")
    for sentence in sentences:
        print(sentence)

def split_text(text):
    print("Split Text using split() function:")
    words = text.split()
    for word in words:
        print(word)

if __name__ == "__main__":
    text = input("Enter the text: ")

    while True:
        print("\nChoose one of the following options:")
        print("1. Print tokenized words")
        print("2. Print tokenized sentences")
        print("3. Print output using split function")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            tokenize_words(text)
        elif choice == '2':
            tokenize_sentences(text)
        elif choice == '3':
            split_text(text)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
