#!/usr/bin/env python
# coding: utf-8

# In[2]:


import string
from collections import Counter

def word_frequency_counter(filename, num_words):
    # Read the text document
    with open(filename, 'r') as file:
        text = file.read().lower()

    # Remove punctuation from the text
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split the text into individual words
    words = text.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    # Get the most frequent words and their counts
    most_common_words = word_counts.most_common(num_words)

    # Display the results
    print(f"The {num_words} most frequent words in the document '{filename}' are:")
    for word, count in most_common_words:
        print(f"{word}: {count}")


# Example usage
filename = 'sample3.txt'  # Replace with your own file path
num_words = 10  # Number of most frequent words to display

word_frequency_counter(filename, num_words)


# In[ ]:




