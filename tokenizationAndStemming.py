import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter
import pandas as pd
nltk.download('punkt')

def tokenize_and_stem(text):
    # Tokenize the text into words
    tokens = word_tokenize(text)

    # Initialize a Porter stemmer
    stemmer = PorterStemmer()

    # Stem each token and add it to the stemmed list
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    return stemmed_tokens

if __name__ == "__main__":
    # Load the dataset from CSV file
    csv_file = "your_dataset.csv"  # Update with your dataset filename
    df = pd.read_csv(csv_file) #We will use a dataset called (Twitter US Airline Sentiment)

    # Concatenate text from all rows into a single string
    text = " ".join(df['text_column'])  # Update 'text_column' with the column containing text

    # Tokenize and stem the text
    stemmed_tokens = tokenize_and_stem(text)

    # Count the frequency of each stemmed word
    word_counts = Counter(stemmed_tokens)

    # Display word frequencies
    print("Word Frequencies:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")
