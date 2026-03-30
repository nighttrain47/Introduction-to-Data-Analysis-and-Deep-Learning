"""
BÀI 2: Liệt kê danh sách các stopword bằng các ngôn ngữ khác nhau
"""

import nltk
nltk.download('stopwords', quiet=True)

from nltk.corpus import stopwords

print("=" * 70)
print("BÀI 2: Liệt kê danh sách các stopword bằng các ngôn ngữ khác nhau")
print("=" * 70)

languages = stopwords.fileids()
print(f"Số ngôn ngữ có stopword: {len(languages)}")
print("\nDanh sách các ngôn ngữ:")
for i, lang in enumerate(languages, 1):
    print(f"  {i}. {lang}")
