# -*- coding: utf-8 -*-
"""
Phần 4 - Câu 5: Vẽ biểu đồ Drop-line cho biến T1 được phân loại bởi biến phanloai1
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

# Tạo biến phanloai1
def phan_loai_t1(diem):
    if diem < 5:
        return 'L'      # Kém
    elif diem < 7:
        return 'B'      # Trung bình
    elif diem < 9:
        return 'K'      # Khá
    else:
        return 'G'      # Giỏi

df['phanloai1'] = df['T1'].apply(phan_loai_t1)

print("="*60)
print("BIỂU ĐỒ DROP-LINE CHO T1 THEO phanloai1")
print("="*60)

# Vẽ biểu đồ Drop-line giống hình mẫu
fig, ax = plt.subplots(figsize=(14, 6))

# Màu sắc cho từng phân loại (giống hình mẫu PDF)
colors = {'L': 'blue', 'B': 'red', 'K': 'green', 'G': 'purple'}

# Vẽ drop-line (bar chart dạng đường) cho từng điểm
bar_width = 0.8
for idx, row in df.iterrows():
    color = colors[row['phanloai1']]
    ax.bar(row['STT'], row['T1'], width=bar_width, color=color, alpha=0.8, edgecolor='none')

# Tạo legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='blue', label='L'),
    Patch(facecolor='red', label='B'),
    Patch(facecolor='green', label='K'),
    Patch(facecolor='purple', label='G')
]
ax.legend(handles=legend_elements, title='phanloai1', fontsize=9, loc='upper right')

ax.set_xlabel('Case Number', fontsize=10)
ax.set_ylabel('Count', fontsize=10)
ax.set_title('Drop-line of T1 by phanloai1', fontsize=12)

# Set x-axis ticks
ax.set_xticks(range(0, len(df)+1, 10))
ax.set_xlim(0, len(df)+1)
ax.set_ylim(0, df['T1'].max() + 0.5)

plt.tight_layout()
plt.savefig('DuLieu/Phan4_Cau5_T1_DropLine.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nĐã lưu biểu đồ: DuLieu/Phan4_Cau5_T1_DropLine.png")
