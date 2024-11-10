from collections import Counter
import re

def word_frequency(text):
    # Convert text to lowercase and remove non-alphabetic characters
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Use Counter to count word frequencies
    word_counts = Counter(words)
    
    return word_counts

# Example usage
text = """Hello, hello world! This is a test. World world hello."""
frequency = word_frequency(text)

# Print word frequency
for word, count in frequency.items():
    print(f"{word}: {count}")
