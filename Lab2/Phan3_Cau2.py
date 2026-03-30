# -*- coding: utf-8 -*-
"""
Phần 3 - Câu 2: Trực quan dữ liệu KQXT trên nhóm học sinh có khối thi A, A1, B thuộc khu vực 1, 2
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

# Lọc dữ liệu: Khối thi A, A1, B và Khu vực 1, 2
condition = (df['KT'].isin(['A', 'A1', 'B'])) & (df['KV'].isin(['1', '2']))
df_filtered = df[condition]

print("="*70)
print("TRỰC QUAN KQXT TRÊN NHÓM KHỐI THI A, A1, B VÀ KHU VỰC 1, 2")
print("="*70)
print(f"Tổng số học sinh thỏa điều kiện: {len(df_filtered)}")

# Bảng chéo KQXT theo KT
crosstab = pd.crosstab(df_filtered['KT'], df_filtered['KQXT'])
crosstab.columns = ['Rớt (0)', 'Đậu (1)']
print("\n--- Bảng chéo KQXT theo Khối thi ---")
print(crosstab)

# Bảng chéo KQXT theo KV
crosstab_kv = pd.crosstab(df_filtered['KV'], df_filtered['KQXT'])
crosstab_kv.columns = ['Rớt (0)', 'Đậu (1)']
print("\n--- Bảng chéo KQXT theo Khu vực ---")
print(crosstab_kv)

# Vẽ biểu đồ
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# === Biểu đồ 1: KQXT theo Khối thi ===
kt_list = df_filtered['KT'].unique()
x = np.arange(len(kt_list))
width = 0.35

rot_counts = []
dau_counts = []
for kt in kt_list:
    kt_data = df_filtered[df_filtered['KT'] == kt]
    rot_counts.append(len(kt_data[kt_data['KQXT'] == 0]))
    dau_counts.append(len(kt_data[kt_data['KQXT'] == 1]))

bars1 = axes[0].bar(x - width/2, rot_counts, width, label='Rớt (0)', color='#e74c3c', edgecolor='black')
bars2 = axes[0].bar(x + width/2, dau_counts, width, label='Đậu (1)', color='#2ecc71', edgecolor='black')

axes[0].set_xlabel('Khối thi', fontsize=12)
axes[0].set_ylabel('Số lượng', fontsize=12)
axes[0].set_title('KQXT theo Khối thi (A, A1, B)\n(Khu vực 1, 2)', fontsize=13, fontweight='bold')
axes[0].set_xticks(x)
axes[0].set_xticklabels(kt_list, fontsize=11)
axes[0].legend()
axes[0].grid(axis='y', alpha=0.3)

# Thêm giá trị
for bar, val in zip(bars1, rot_counts):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, str(val), 
                 ha='center', va='bottom', fontsize=10, fontweight='bold')
for bar, val in zip(bars2, dau_counts):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, str(val), 
                 ha='center', va='bottom', fontsize=10, fontweight='bold')

# === Biểu đồ 2: KQXT theo Khu vực ===
kv_list = df_filtered['KV'].unique()
x2 = np.arange(len(kv_list))

rot_counts_kv = []
dau_counts_kv = []
for kv in kv_list:
    kv_data = df_filtered[df_filtered['KV'] == kv]
    rot_counts_kv.append(len(kv_data[kv_data['KQXT'] == 0]))
    dau_counts_kv.append(len(kv_data[kv_data['KQXT'] == 1]))

bars3 = axes[1].bar(x2 - width/2, rot_counts_kv, width, label='Rớt (0)', color='#e74c3c', edgecolor='black')
bars4 = axes[1].bar(x2 + width/2, dau_counts_kv, width, label='Đậu (1)', color='#2ecc71', edgecolor='black')

axes[1].set_xlabel('Khu vực', fontsize=12)
axes[1].set_ylabel('Số lượng', fontsize=12)
axes[1].set_title('KQXT theo Khu vực (1, 2)\n(Khối thi A, A1, B)', fontsize=13, fontweight='bold')
axes[1].set_xticks(x2)
axes[1].set_xticklabels(kv_list, fontsize=11)
axes[1].legend()
axes[1].grid(axis='y', alpha=0.3)

# Thêm giá trị
for bar, val in zip(bars3, rot_counts_kv):
    axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, str(val), 
                 ha='center', va='bottom', fontsize=10, fontweight='bold')
for bar, val in zip(bars4, dau_counts_kv):
    axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, str(val), 
                 ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('DuLieu/Phan3_Cau2_KQXT_KT_KV.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nĐã lưu biểu đồ: DuLieu/Phan3_Cau2_KQXT_KT_KV.png")
