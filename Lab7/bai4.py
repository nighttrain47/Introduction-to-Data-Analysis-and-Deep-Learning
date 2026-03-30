"""
BÀI 4: Loại bỏ các stopword từ một văn bản đã cho
"""

import nltk
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

from nltk.corpus import stopwords

print("=" * 70)
print("BÀI 4: Loại bỏ các stopword từ một văn bản đã cho")
print("=" * 70)

sample_text = "This is a sample sentence showing off the stop words filtration. " \
              "The quick brown fox jumps over the lazy dog."
print(f"Văn bản gốc:\n  {sample_text}")

# Tokenize văn bản
tokens = nltk.word_tokenize(sample_text)
print(f"\nCác từ sau khi tokenize ({len(tokens)} từ):\n  {tokens}")

# Loại bỏ stopword
sw_english = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w.lower() not in sw_english]
print(f"\nCác từ sau khi loại bỏ stopword ({len(filtered_tokens)} từ):\n  {filtered_tokens}")

filtered_sentence = ' '.join(filtered_tokens)
print(f"\nVăn bản sau khi loại bỏ stopword:\n  {filtered_sentence}")
