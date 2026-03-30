# -*- coding: utf-8 -*-
"""
Phần 4 - Câu 1: Vẽ biểu đồ đường Simple cho biến T1
"""

import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

print("="*60)
print("BIỂU ĐỒ ĐƯỜNG SIMPLE CHO BIẾN T1 (ĐIỂM TOÁN LẦN 1)")
print("="*60)

# Thống kê mô tả T1
print("\n--- Thống kê mô tả T1 ---")
print(df['T1'].describe())

# Vẽ biểu đồ đường Simple (giống mẫu PDF)
# Đếm tần suất của mỗi giá trị T1
t1_counts = df['T1'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(12, 5))

# x = giá trị T1, y = số lần xuất hiện (Count)
x = t1_counts.index
y = t1_counts.values

# Vẽ đường simple 
ax.plot(x, y, linewidth=1, color='black')

ax.set_xlabel('T1', fontsize=10)
ax.set_ylabel('Count', fontsize=10)

# Xoay nhãn trục X để dễ đọc
plt.xticks(rotation=45, ha='right', fontsize=8)

plt.tight_layout()
plt.savefig('DuLieu/Phan4_Cau1_T1_Line.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nĐã lưu biểu đồ: DuLieu/Phan4_Cau1_T1_Line.png")
