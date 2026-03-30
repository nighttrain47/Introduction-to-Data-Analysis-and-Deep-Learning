# -*- coding: utf-8 -*-
"""
Phần 3 - Câu 4: Trực quan dữ liệu số lượng thí sinh đậu, rớt trên từng nhóm khối thi
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

print("="*70)
print("TRỰC QUAN SỐ LƯỢNG THÍ SINH ĐẬU/RỚT TRÊN TỪNG NHÓM KHỐI THI")
print("="*70)

# Bảng chéo
crosstab = pd.crosstab(df['KT'], df['KQXT'])
crosstab.columns = ['Rớt (0)', 'Đậu (1)']
print("\n--- Bảng chéo: Số lượng đậu/rớt theo Khối thi ---")
print(crosstab)

# Tính tỷ lệ đậu
crosstab['Tỷ lệ đậu (%)'] = (crosstab['Đậu (1)'] / (crosstab['Rớt (0)'] + crosstab['Đậu (1)']) * 100).round(2)
print("\nBảng với tỷ lệ đậu:")
print(crosstab)

# Vẽ biểu đồ
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

kt_list = crosstab.index.tolist()
x = np.arange(len(kt_list))
width = 0.35

# === Biểu đồ 1: Grouped Bar Chart ===
rot_values = crosstab['Rớt (0)'].values
dau_values = crosstab['Đậu (1)'].values

bars1 = axes[0].bar(x - width/2, rot_values, width, label='Rớt', color='#e74c3c', edgecolor='black')
bars2 = axes[0].bar(x + width/2, dau_values, width, label='Đậu', color='#2ecc71', edgecolor='black')

axes[0].set_xlabel('Khối thi', fontsize=12)
axes[0].set_ylabel('Số lượng thí sinh', fontsize=12)
axes[0].set_title('Số lượng Đậu/Rớt theo Khối thi', fontsize=14, fontweight='bold')
axes[0].set_xticks(x)
axes[0].set_xticklabels(kt_list, fontsize=11)
axes[0].legend()
axes[0].grid(axis='y', alpha=0.3)

# Thêm giá trị
for bar, val in zip(bars1, rot_values):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, 
                 str(val), ha='center', va='bottom', fontsize=10, fontweight='bold')
for bar, val in zip(bars2, dau_values):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, 
                 str(val), ha='center', va='bottom', fontsize=10, fontweight='bold')

# === Biểu đồ 2: Stacked Bar Chart với tỷ lệ % ===
tot_values = rot_values + dau_values
rot_percent = rot_values / tot_values * 100
dau_percent = dau_values / tot_values * 100

bars3 = axes[1].bar(kt_list, rot_percent, label='Rớt', color='#e74c3c', edgecolor='black')
bars4 = axes[1].bar(kt_list, dau_percent, bottom=rot_percent, label='Đậu', color='#2ecc71', edgecolor='black')

axes[1].set_xlabel('Khối thi', fontsize=12)
axes[1].set_ylabel('Tỷ lệ (%)', fontsize=12)
axes[1].set_title('Tỷ lệ Đậu/Rớt theo Khối thi (Stacked 100%)', fontsize=14, fontweight='bold')
axes[1].legend(loc='upper right')
axes[1].grid(axis='y', alpha=0.3)

# Thêm giá trị %
for i, (rot, dau) in enumerate(zip(rot_percent, dau_percent)):
    axes[1].text(i, rot/2, f'{rot:.1f}%', ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    axes[1].text(i, rot + dau/2, f'{dau:.1f}%', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

plt.tight_layout()
plt.savefig('DuLieu/Phan3_Cau4_KQXT_by_KT.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nĐã lưu biểu đồ: DuLieu/Phan3_Cau4_KQXT_by_KT.png")
