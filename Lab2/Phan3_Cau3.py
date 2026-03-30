# -*- coding: utf-8 -*-
"""
Phần 3 - Câu 3: Trực quan dữ liệu số lượng thí sinh từng khu vực dựa trên từng nhóm khối thi
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

print("="*70)
print("TRỰC QUAN SỐ LƯỢNG THÍ SINH TỪNG KHU VỰC THEO NHÓM KHỐI THI")
print("="*70)

# Bảng chéo
crosstab = pd.crosstab(df['KT'], df['KV'])
print("\n--- Bảng chéo: Số lượng thí sinh theo Khối thi và Khu vực ---")
print(crosstab)
print(f"\nTổng: {crosstab.sum().sum()}")

# Vẽ biểu đồ
fig, ax = plt.subplots(figsize=(12, 6))

kt_list = crosstab.index.tolist()
kv_list = crosstab.columns.tolist()
x = np.arange(len(kt_list))
width = 0.25

# Màu sắc cho từng khu vực
colors = {'1': '#3498db', '2': '#e74c3c', '2NT': '#2ecc71'}

# Vẽ từng nhóm khu vực
for i, kv in enumerate(kv_list):
    offset = (i - len(kv_list)/2 + 0.5) * width
    values = crosstab[kv].values
    bars = ax.bar(x + offset, values, width, label=f'KV {kv}', 
                  color=colors.get(kv, '#95a5a6'), edgecolor='black', linewidth=0.8)
    
    # Thêm giá trị
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, 
                str(val), ha='center', va='bottom', fontsize=10, fontweight='bold')

ax.set_xlabel('Khối thi', fontsize=12)
ax.set_ylabel('Số lượng thí sinh', fontsize=12)
ax.set_title('Số lượng thí sinh từng Khu vực theo Nhóm Khối thi', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(kt_list, fontsize=11)
ax.legend(title='Khu vực', fontsize=10)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('DuLieu/Phan3_Cau3_KV_by_KT.png', dpi=300, bbox_inches='tight')
plt.show()

# Biểu đồ stacked để so sánh tổng thể
fig2, ax2 = plt.subplots(figsize=(10, 6))

bottom = np.zeros(len(kt_list))
for kv in kv_list:
    values = crosstab[kv].values
    ax2.bar(kt_list, values, bottom=bottom, label=f'KV {kv}', 
            color=colors.get(kv, '#95a5a6'), edgecolor='black', linewidth=0.8)
    bottom += values

ax2.set_xlabel('Khối thi', fontsize=12)
ax2.set_ylabel('Số lượng thí sinh', fontsize=12)
ax2.set_title('Biểu đồ Stacked - Số lượng thí sinh theo Khối thi và Khu vực', 
              fontsize=14, fontweight='bold')
ax2.legend(title='Khu vực', fontsize=10)
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('DuLieu/Phan3_Cau3_KV_by_KT_stacked.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nĐã lưu biểu đồ: DuLieu/Phan3_Cau3_KV_by_KT.png")
print("Đã lưu biểu đồ: DuLieu/Phan3_Cau3_KV_by_KT_stacked.png")
