# -*- coding: utf-8 -*-
"""
Phần 4 - Câu 4: Vẽ biểu đồ đường Multiple Line cho biến T1 được phân loại bởi biến phanloai1
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
print("BIỂU ĐỒ MULTIPLE LINE CHO T1 THEO phanloai1")
print("="*60)

# Vẽ biểu đồ Multiple Line giống hình mẫu
fig, ax = plt.subplots(figsize=(14, 6))

# Lấy tất cả các giá trị T1 unique và sắp xếp
all_t1_values = sorted(df['T1'].unique())

# Màu sắc và nhãn cho từng phân loại (giống hình mẫu PDF)
# PhanlopT1: Gioi=xanh lá, Kem=xanh dương, Kha=vàng/olive, Trungbinh=tím
colors = {'G': 'green', 'L': 'blue', 'K': 'olive', 'B': 'purple'}
labels = {'G': 'Gioi', 'L': 'Kem', 'K': 'Kha', 'B': 'Trungbinh'}

# Vẽ đường tần suất cho từng nhóm phanloai1
for phanloai in ['G', 'L', 'K', 'B']:
    # Lọc dữ liệu theo nhóm
    df_group = df[df['phanloai1'] == phanloai]
    
    # Đếm tần suất của T1 trong nhóm này
    t1_counts = df_group['T1'].value_counts().sort_index()
    
    if len(t1_counts) > 0:
        # Vẽ đường với marker để điểm đơn lẻ cũng hiển thị
        ax.plot(t1_counts.index, t1_counts.values, 
                marker='o', markersize=4, linewidth=1.5, 
                color=colors[phanloai], label=labels[phanloai])

# Legend
ax.legend(title='PhanlopT1', fontsize=9, loc='upper right')

ax.set_xlabel('T1', fontsize=10)
ax.set_ylabel('Count', fontsize=10)

# Xoay nhãn trục X
plt.xticks(rotation=45, ha='right', fontsize=8)

plt.tight_layout()
plt.savefig('DuLieu/Phan4_Cau4_T1_MultiLine.png', dpi=300, bbox_inches='tight')
plt.show()

# Thống kê theo nhóm
print("\n--- Thống kê T1 theo phanloai1 ---")
stats = df.groupby('phanloai1')['T1'].agg(['count', 'mean', 'std', 'min', 'max'])
print(stats.round(2))

print("\nĐã lưu biểu đồ: DuLieu/Phan4_Cau4_T1_MultiLine.png")
