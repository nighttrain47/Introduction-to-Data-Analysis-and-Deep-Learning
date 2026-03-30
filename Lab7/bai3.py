"""
BÀI 3: Kiểm tra danh sách các stopword bằng các ngôn ngữ khác nhau
"""

import nltk
nltk.download('stopwords', quiet=True)

from nltk.corpus import stopwords

print("=" * 70)
print("BÀI 3: Kiểm tra danh sách các stopword bằng các ngôn ngữ khác nhau")
print("=" * 70)

# Hiển thị 10 stopword đầu tiên của một số ngôn ngữ
sample_languages = ['english', 'french', 'german', 'spanish', 'italian']
for lang in sample_languages:
    sw = stopwords.words(lang)
    print(f"\n  Ngôn ngữ: {lang.upper()}")
    print(f"  Tổng số stopword: {len(sw)}")
    print(f"  10 stopword đầu tiên: {sw[:10]}")
