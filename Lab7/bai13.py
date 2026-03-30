"""
BÀI 13: Trích xuất ký tự cuối cùng của tất cả các tên và tạo mảng mới
"""

import nltk
import random
from collections import Counter

nltk.download('names', quiet=True)

from nltk.corpus import names

print("=" * 70)
print("BÀI 13: Trích xuất ký tự cuối cùng của tất cả các tên")
print("=" * 70)

male_names = names.words('male.txt')
female_names = names.words('female.txt')

# Tạo danh sách tên có gắn nhãn
labeled_names = ([(name, 'male') for name in male_names] +
                 [(name, 'female') for name in female_names])

# Trộn ngẫu nhiên
random.shuffle(labeled_names)

# Tạo mảng mới với chữ cái cuối cùng và nhãn
last_letter_data = [(name[-1].lower(), label) for name, label in labeled_names]

print("\n  20 mẫu đầu tiên (chữ cái cuối cùng, nhãn):")
print(f"  {'STT':>4s}  {'Tên gốc':<20s}  {'Chữ cái cuối':<14s}  {'Nhãn':<10s}")
print(f"  {'----':>4s}  {'--------':<20s}  {'------------':<14s}  {'----':<10s}")
for i in range(20):
    name, label = labeled_names[i]
    last_char = last_letter_data[i][0]
    print(f"  {i+1:>4d}  {name:<20s}  {last_char:^14s}  {label:<10s}")

# Thống kê phân bổ ký tự cuối cùng theo giới tính
print("\n  --- Thống kê phân bổ ký tự cuối cùng theo giới tính ---")

male_last = [name[-1].lower() for name in male_names]
female_last = [name[-1].lower() for name in female_names]

male_counter = Counter(male_last)
female_counter = Counter(female_last)

print(f"\n  {'Ký tự':>6s}  {'Nam':>6s}  {'Nữ':>6s}")
print(f"  {'-----':>6s}  {'---':>6s}  {'---':>6s}")

all_letters = sorted(set(male_last + female_last))
for letter in all_letters:
    m_count = male_counter.get(letter, 0)
    f_count = female_counter.get(letter, 0)
    print(f"  {letter:>6s}  {m_count:>6d}  {f_count:>6d}")

# Tìm các chữ cái phổ biến nhất theo giới tính
print(f"\n  Top 5 chữ cái cuối phổ biến nhất ở tên NAM:  {male_counter.most_common(5)}")
print(f"  Top 5 chữ cái cuối phổ biến nhất ở tên NỮ:   {female_counter.most_common(5)}")
