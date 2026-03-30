# -*- coding: utf-8 -*-
"""
Phần 5 - Câu 2: Mô tả và khảo sát phân phối cho biến T1 trên từng nhóm phân lớp (phanlopT1)
- Trực quan hóa biểu đồ Box-plot, histogram và QQ-plot theo phân nhóm là giá trị của 'phanlopT1'
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

# Tạo biến phanlopT1
def phan_loai_t1(diem):
    if diem < 5:
        return 'k'      # Kém
    elif diem < 7:
        return 'tb'     # Trung bình
    elif diem < 8:
        return 'kha'    # Khá
    else:
        return 'g'      # Giỏi

df['phanlopT1'] = df['T1'].apply(phan_loai_t1)

print("="*80)
print("MÔ TẢ VÀ KHẢO SÁT PHÂN PHỐI CHO BIẾN T1 THEO NHÓM phanlopT1")
print("="*80)

# Thống kê theo nhóm
print("\n--- Thống kê mô tả T1 theo phanlopT1 ---")
groups = ['k', 'tb', 'kha', 'g']
labels_map = {'k': 'Kém (k)', 'tb': 'Trung bình (tb)', 'kha': 'Khá (kha)', 'g': 'Giỏi (g)'}

for group in groups:
    group_data = df[df['phanlopT1'] == group]['T1']
    if len(group_data) > 0:
        print(f"\n{labels_map[group]}:")
        print(f"  n = {len(group_data)}")
        print(f"  Mean = {group_data.mean():.4f}")
        print(f"  Median = {group_data.median():.4f}")
        print(f"  Std = {group_data.std():.4f}")
        print(f"  Min = {group_data.min():.4f}")
        print(f"  Max = {group_data.max():.4f}")
        print(f"  Skewness = {group_data.skew():.4f}")
        print(f"  Kurtosis = {group_data.kurtosis():.4f}")

# Vẽ biểu đồ
fig, axes = plt.subplots(3, 4, figsize=(16, 12))

colors = {'k': '#e74c3c', 'tb': '#f39c12', 'kha': '#3498db', 'g': '#2ecc71'}

# Hàng 1: Box-plot
for i, group in enumerate(groups):
    group_data = df[df['phanlopT1'] == group]['T1']
    if len(group_data) > 0:
        bp = axes[0, i].boxplot(group_data, patch_artist=True)
        bp['boxes'][0].set_facecolor(colors[group])
        axes[0, i].set_title(f'Box-plot: {labels_map[group]}', fontsize=11, fontweight='bold')
        axes[0, i].set_ylabel('Điểm T1')
        axes[0, i].grid(axis='y', alpha=0.3)
    else:
        axes[0, i].text(0.5, 0.5, 'Không có dữ liệu', ha='center', va='center')
        axes[0, i].set_title(f'Box-plot: {labels_map[group]}', fontsize=11)

# Hàng 2: Histogram
for i, group in enumerate(groups):
    group_data = df[df['phanlopT1'] == group]['T1']
    if len(group_data) > 0:
        axes[1, i].hist(group_data, bins=8, color=colors[group], edgecolor='black', alpha=0.7)
        axes[1, i].axvline(group_data.mean(), color='red', linestyle='--', linewidth=2, 
                           label=f'Mean={group_data.mean():.2f}')
        axes[1, i].set_title(f'Histogram: {labels_map[group]}', fontsize=11, fontweight='bold')
        axes[1, i].set_xlabel('Điểm T1')
        axes[1, i].set_ylabel('Tần số')
        axes[1, i].legend(fontsize=8)
        axes[1, i].grid(axis='y', alpha=0.3)
    else:
        axes[1, i].text(0.5, 0.5, 'Không có dữ liệu', ha='center', va='center')
        axes[1, i].set_title(f'Histogram: {labels_map[group]}', fontsize=11)

# Hàng 3: QQ-plot
for i, group in enumerate(groups):
    group_data = df[df['phanlopT1'] == group]['T1']
    if len(group_data) > 2:
        stats.probplot(group_data, dist="norm", plot=axes[2, i])
        axes[2, i].set_title(f'QQ-plot: {labels_map[group]}', fontsize=11, fontweight='bold')
        axes[2, i].grid(True, alpha=0.3)
    else:
        axes[2, i].text(0.5, 0.5, 'Không đủ dữ liệu', ha='center', va='center')
        axes[2, i].set_title(f'QQ-plot: {labels_map[group]}', fontsize=11)

plt.tight_layout()
plt.savefig('DuLieu/Phan5_Cau2_T1_by_phanlopT1.png', dpi=300, bbox_inches='tight')
plt.show()

# Vẽ biểu đồ Box-plot so sánh các nhóm
fig2, ax2 = plt.subplots(figsize=(10, 6))

data_to_plot = [df[df['phanlopT1'] == g]['T1'] for g in groups]
labels = [labels_map[g] for g in groups]

bp2 = ax2.boxplot(data_to_plot, labels=labels, patch_artist=True)
for patch, color in zip(bp2['boxes'], [colors[g] for g in groups]):
    patch.set_facecolor(color)

ax2.set_xlabel('Phân loại T1', fontsize=12)
ax2.set_ylabel('Điểm T1', fontsize=12)
ax2.set_title('So sánh phân phối T1 theo phanlopT1', fontsize=14, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('DuLieu/Phan5_Cau2_T1_Comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nĐã lưu biểu đồ: DuLieu/Phan5_Cau2_T1_by_phanlopT1.png")
print("Đã lưu biểu đồ: DuLieu/Phan5_Cau2_T1_Comparison.png")
