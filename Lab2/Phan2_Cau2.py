# -*- coding: utf-8 -*-
"""
Phần 2 - Câu 2: Trình bày dữ liệu lần lượt các biến US_TBM1, US_TBM2 và US_TBM3
- Lập bảng tần số và tần suất
- Vẽ biểu đồ
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

# Danh sách biến cần phân tích
variables = ['US_TBM1', 'US_TBM2', 'US_TBM3']

# Hiển thị thống kê mô tả
print("="*80)
print("THỐNG KÊ MÔ TẢ CÁC BIẾN US_TBM1, US_TBM2, US_TBM3")
print("="*80)

for var in variables:
    print(f"\n--- Biến {var} ---")
    print(f"Số lượng: {df[var].count()}")
    print(f"Giá trị nhỏ nhất: {df[var].min():.4f}")
    print(f"Giá trị lớn nhất: {df[var].max():.4f}")
    print(f"Trung bình: {df[var].mean():.4f}")
    print(f"Độ lệch chuẩn: {df[var].std():.4f}")
    print(f"Trung vị: {df[var].median():.4f}")

# Tạo bảng tần số cho dữ liệu liên tục (chia thành các khoảng)
print("\n" + "="*80)
print("BẢNG TẦN SỐ VÀ TẦN SUẤT (CHIA KHOẢNG)")
print("="*80)

# Định nghĩa các khoảng (bins)
bins = [0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
labels = ['0-1.5', '1.5-2.0', '2.0-2.5', '2.5-3.0', '3.0-3.5', '3.5-4.0']

for var in variables:
    print(f"\n--- Biến {var} ---")
    df[f'{var}_bin'] = pd.cut(df[var], bins=bins, labels=labels, right=False)
    freq = df[f'{var}_bin'].value_counts().sort_index()
    freq_percent = (freq / freq.sum() * 100).round(2)
    
    freq_table = pd.DataFrame({
        'Khoảng': freq.index,
        'Tần số': freq.values,
        'Tần suất (%)': freq_percent.values
    })
    print(freq_table.to_string(index=False))

# Vẽ biểu đồ
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

colors = ['#3498db', '#e74c3c', '#2ecc71']

# Hàng 1: Histogram
for i, var in enumerate(variables):
    axes[0, i].hist(df[var], bins=15, color=colors[i], edgecolor='black', alpha=0.7)
    axes[0, i].set_xlabel(var, fontsize=11)
    axes[0, i].set_ylabel('Tần số', fontsize=11)
    axes[0, i].set_title(f'Histogram - {var}', fontsize=12, fontweight='bold')
    axes[0, i].grid(axis='y', alpha=0.3)
    
    # Thêm đường trung bình
    mean_val = df[var].mean()
    axes[0, i].axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_val:.2f}')
    axes[0, i].legend()

# Hàng 2: Boxplot
for i, var in enumerate(variables):
    bp = axes[1, i].boxplot(df[var], patch_artist=True)
    bp['boxes'][0].set_facecolor(colors[i])
    axes[1, i].set_ylabel('Giá trị', fontsize=11)
    axes[1, i].set_title(f'Boxplot - {var}', fontsize=12, fontweight='bold')
    axes[1, i].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('DuLieu/Phan2_Cau2_US_TBM.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nĐã lưu biểu đồ: DuLieu/Phan2_Cau2_US_TBM.png")
