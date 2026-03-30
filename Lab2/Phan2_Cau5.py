# -*- coding: utf-8 -*-
"""
Phần 2 - Câu 5: Trình bày dữ liệu lần lượt các biến DH1, DH2, DH3 lớn hơn bằng 5.0 
và thuộc khu vực 2NT
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

# Lọc dữ liệu: KV = '2NT' và DH1, DH2, DH3 >= 5.0
condition = (df['KV'] == '2NT') & (df['DH1'] >= 5.0) & (df['DH2'] >= 5.0) & (df['DH3'] >= 5.0)
df_filtered = df[condition]

print("="*70)
print("TRÌNH BÀY DỮ LIỆU DH1, DH2, DH3 >= 5.0 VÀ THUỘC KHU VỰC 2NT")
print("="*70)
print(f"Tổng số học sinh thỏa điều kiện: {len(df_filtered)}")

# Kiểm tra nếu không có dữ liệu
if len(df_filtered) == 0:
    print("\nKhông có học sinh thỏa mãn điều kiện!")
    # Thử với điều kiện lỏng hơn: chỉ cần 1 trong 3 điểm >= 5.0
    print("\n--- Thử với điều kiện: KV = '2NT' và ít nhất 1 điểm >= 5.0 ---")
    condition_loose = (df['KV'] == '2NT') & ((df['DH1'] >= 5.0) | (df['DH2'] >= 5.0) | (df['DH3'] >= 5.0))
    df_filtered = df[condition_loose]
    print(f"Số học sinh với điều kiện lỏng: {len(df_filtered)}")

if len(df_filtered) > 0:
    # Thống kê mô tả
    print("\n--- Thống kê mô tả các biến DH1, DH2, DH3 ---")
    for var in ['DH1', 'DH2', 'DH3']:
        data = df_filtered[var]
        print(f"\n{var}:")
        print(f"  Số lượng: {data.count()}")
        print(f"  Min: {data.min():.2f}")
        print(f"  Max: {data.max():.2f}")
        print(f"  Mean: {data.mean():.2f}")
        print(f"  Std: {data.std():.2f}")
        print(f"  Median: {data.median():.2f}")

    # Hiển thị chi tiết dữ liệu
    print("\n--- Chi tiết dữ liệu ---")
    print(df_filtered[['STT', 'KV', 'DH1', 'DH2', 'DH3', 'KT', 'KQXT']].to_string(index=False))

    # Vẽ biểu đồ
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    variables = ['DH1', 'DH2', 'DH3']
    colors = ['#3498db', '#e74c3c', '#2ecc71']

    # Hàng 1: Histogram
    for i, var in enumerate(variables):
        axes[0, i].hist(df_filtered[var], bins=10, color=colors[i], edgecolor='black', alpha=0.7)
        axes[0, i].set_xlabel(var, fontsize=11)
        axes[0, i].set_ylabel('Tần số', fontsize=11)
        axes[0, i].set_title(f'Histogram - {var}\n(KV=2NT, điểm>=5.0)', fontsize=12, fontweight='bold')
        axes[0, i].grid(axis='y', alpha=0.3)
        
        # Thêm đường trung bình
        mean_val = df_filtered[var].mean()
        axes[0, i].axvline(mean_val, color='red', linestyle='--', linewidth=2, 
                           label=f'Mean = {mean_val:.2f}')
        axes[0, i].legend()

    # Hàng 2: Boxplot
    for i, var in enumerate(variables):
        bp = axes[1, i].boxplot(df_filtered[var], patch_artist=True)
        bp['boxes'][0].set_facecolor(colors[i])
        axes[1, i].set_ylabel('Điểm', fontsize=11)
        axes[1, i].set_title(f'Boxplot - {var}\n(KV=2NT, điểm>=5.0)', fontsize=12, fontweight='bold')
        axes[1, i].grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig('DuLieu/Phan2_Cau5_DH_2NT.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\nĐã lưu biểu đồ: DuLieu/Phan2_Cau5_DH_2NT.png")
else:
    print("\nKhông có dữ liệu để vẽ biểu đồ!")
