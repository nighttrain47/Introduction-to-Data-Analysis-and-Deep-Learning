"""
BÀI 12: In 15 kết hợp ngẫu nhiên đầu tiên tên nam và tên nữ
"""

import nltk
import random

nltk.download('names', quiet=True)

from nltk.corpus import names

print("=" * 70)
print("BÀI 12: 15 kết hợp ngẫu nhiên tên nam và tên nữ từ kho tên")
print("=" * 70)

male_names = names.words('male.txt')
female_names = names.words('female.txt')

# Tạo danh sách tên có gắn nhãn
labeled_names = ([(name, 'male') for name in male_names] +
                 [(name, 'female') for name in female_names])

# Trộn ngẫu nhiên
random.shuffle(labeled_names)

print("\n  15 kết hợp ngẫu nhiên đầu tiên:")
print(f"  {'STT':>4s}  {'Tên':<20s}  {'Giới tính':<10s}")
print(f"  {'----':>4s}  {'----':<20s}  {'---------':<10s}")
for i, (name, label) in enumerate(labeled_names[:15], 1):
    print(f"  {i:>4d}  {name:<20s}  {label:<10s}")
