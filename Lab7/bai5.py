"""
BÀI 5: Bỏ qua các stopword từ danh sách các stopword
"""

import nltk
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

from nltk.corpus import stopwords

print("=" * 70)
print("BÀI 5: Bỏ qua các stopword từ danh sách các stopword")
print("=" * 70)

sw_english = set(stopwords.words('english'))

# Loại bỏ một số stopword ra khỏi danh sách stopword
words_to_ignore = {'not', 'no', 'nor', 'neither', 'never', 'nobody'}
print(f"Các stopword muốn bỏ qua (giữ lại trong văn bản): {words_to_ignore}")

custom_sw = sw_english - words_to_ignore
print(f"\nSố stopword ban đầu: {len(sw_english)}")
print(f"Số stopword sau khi bỏ qua: {len(custom_sw)}")

sample_text2 = "I do not like this movie. It is not good and nobody likes it."
print(f"\nVăn bản gốc:\n  {sample_text2}")

tokens2 = nltk.word_tokenize(sample_text2)

# Lọc với bộ stopword gốc
filtered_original = [w for w in tokens2 if w.lower() not in sw_english]
print(f"\nLọc với bộ stopword gốc:\n  {' '.join(filtered_original)}")

# Lọc với bộ stopword tùy chỉnh (giữ lại not, no, ...)
filtered_custom = [w for w in tokens2 if w.lower() not in custom_sw]
print(f"\nLọc với bộ stopword tùy chỉnh (giữ lại phủ định):\n  {' '.join(filtered_custom)}")
