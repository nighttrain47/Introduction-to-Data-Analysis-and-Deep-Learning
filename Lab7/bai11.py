"""
BÀI 11: Tìm số lượng tên nam và nữ trong kho ngữ liệu names
"""

import nltk
nltk.download('names', quiet=True)

from nltk.corpus import names

print("=" * 70)
print("BÀI 11: Số lượng tên nam và nữ trong kho ngữ liệu names")
print("=" * 70)

male_names = names.words('male.txt')
female_names = names.words('female.txt')

print(f"\n  Số lượng tên nam (male.txt):   {len(male_names)}")
print(f"  Số lượng tên nữ (female.txt):  {len(female_names)}")
print(f"  Tổng cộng:                     {len(male_names) + len(female_names)}")

print(f"\n  10 tên nam đầu tiên:  {male_names[:10]}")
print(f"  10 tên nữ đầu tiên:   {female_names[:10]}")
