# -*- coding: utf-8 -*-
"""
Phần 2 - Câu 4: Trình bày dữ liệu biến KV với các học sinh là nam thuộc dân tộc Kinh,
có điểm thỏa mãn điều kiện (DH1 >= 5.0 và DH2 >= 4.0 và DH3 >= 4.0)
"""

import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

# Lọc dữ liệu theo điều kiện:
# - Học sinh nam (GT = 'M')
# - Dân tộc Kinh (DT = 0.0)
# - DH1 >= 5.0 và DH2 >= 4.0 và DH3 >= 4.0
condition = (df['GT'] == 'M') & (df['DT'] == 0.0) & \
            (df['DH1'] >= 5.0) & (df['DH2'] >= 4.0) & (df['DH3'] >= 4.0)

df_filtered = df[condition]

print("="*70)
print("TRÌNH BÀY DỮ LIỆU BIẾN KHU VỰC (KV)")
print("Điều kiện: Nam, Dân tộc Kinh, DH1>=5.0, DH2>=4.0, DH3>=4.0")
print("="*70)
print(f"Tổng số học sinh thỏa điều kiện: {len(df_filtered)}")

# Kiểm tra nếu không có dữ liệu
if len(df_filtered) == 0:
    print("\nKhông có học sinh thỏa mãn điều kiện!")
else:
    # Tần số và tần suất
    freq = df_filtered['KV'].value_counts().sort_index()
    freq_percent = df_filtered['KV'].value_counts(normalize=True).sort_index() * 100

    print("\n--- Bảng tần số và tần suất ---")
    freq_table = pd.DataFrame({
        'Khu vực': freq.index,
        'Tần số': freq.values,
        'Tần suất (%)': freq_percent.values.round(2)
    })
    print(freq_table.to_string(index=False))

    # Hiển thị chi tiết dữ liệu
    print("\n--- Chi tiết dữ liệu ---")
    print(df_filtered[['STT', 'GT', 'DT', 'KV', 'DH1', 'DH2', 'DH3']].to_string(index=False))

    # Vẽ biểu đồ
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    labels = freq.index.tolist()
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12'][:len(labels)]

    # Biểu đồ cột
    bars = axes[0].bar(labels, freq.values, color=colors, edgecolor='black', linewidth=1.2)
    axes[0].set_xlabel('Khu vực (KV)', fontsize=12)
    axes[0].set_ylabel('Tần số (Số lượng)', fontsize=12)
    axes[0].set_title('Biểu đồ cột - Tần số KV\n(Nam, Kinh, DH1>=5, DH2>=4, DH3>=4)', 
                      fontsize=12, fontweight='bold')
    axes[0].grid(axis='y', alpha=0.3)

    # Thêm giá trị lên đầu cột
    for bar, val in zip(bars, freq.values):
        axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2, 
                     str(val), ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Biểu đồ tròn
    explode = [0.05] * len(labels)
    wedges, texts, autotexts = axes[1].pie(
        freq.values, 
        labels=labels, 
        autopct='%1.1f%%',
        explode=explode,
        colors=colors,
        startangle=90,
        shadow=True
    )
    axes[1].set_title('Biểu đồ tròn - Tần suất KV\n(Nam, Kinh, DH1>=5, DH2>=4, DH3>=4)', 
                      fontsize=12, fontweight='bold')

    for text in autotexts:
        text.set_fontsize(11)
        text.set_fontweight('bold')

    plt.tight_layout()
    plt.savefig('DuLieu/Phan2_Cau4_KV_Filtered.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("\nĐã lưu biểu đồ: DuLieu/Phan2_Cau4_KV_Filtered.png")
