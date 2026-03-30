"""
BÀI 1: Liệt kê các tên của corpus
"""

import nltk
nltk.download('gutenberg', quiet=True)

from nltk.corpus import gutenberg

print("=" * 70)
print("BÀI 1: Liệt kê các tên của corpus")
print("=" * 70)

print("Các corpus trong Gutenberg:")
for i, fileid in enumerate(gutenberg.fileids(), 1):
    print(f"  {i}. {fileid}")

print(f"\nTổng số corpus: {len(gutenberg.fileids())}")
