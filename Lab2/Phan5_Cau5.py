# -*- coding: utf-8 -*-
"""
Phần 5 - Câu 5: Khảo sát tương quan giữa các biến DH1, DH2, DH3
- Nhận xét ma trận hiệp phương sai hoặc ma trận tương quan
- Vẽ biểu đồ Scatter giữa các biến
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

print("="*80)
print("KHẢO SÁT TƯƠNG QUAN GIỮA CÁC BIẾN DH1, DH2, DH3")
print("="*80)

# Chọn các biến
dh_vars = ['DH1', 'DH2', 'DH3']
df_dh = df[dh_vars]

# 1. Ma trận hiệp phương sai
print("\n--- Ma trận Hiệp phương sai (Covariance Matrix) ---")
cov_matrix = df_dh.cov()
print(cov_matrix.round(4))

# 2. Ma trận tương quan
print("\n--- Ma trận Tương quan (Correlation Matrix) ---")
corr_matrix = df_dh.corr()
print(corr_matrix.round(4))

# 3. P-value cho từng cặp
print("\n--- P-value cho từng cặp biến ---")
pairs = [('DH1', 'DH2'), ('DH1', 'DH3'), ('DH2', 'DH3')]
for var1, var2 in pairs:
    r, p = stats.pearsonr(df[var1], df[var2])
    print(f"{var1} vs {var2}: r = {r:.4f}, p-value = {p:.6f}")
    
    if abs(r) < 0.3:
        strength = "yếu"
    elif abs(r) < 0.7:
        strength = "trung bình"
    else:
        strength = "mạnh"
    
    direction = "thuận" if r > 0 else "nghịch"
    sig = "có" if p < 0.05 else "không có"
    print(f"  => Tương quan {strength}, {direction}, {sig} ý nghĩa thống kê (α=0.05)")

# 4. Nhận xét
print("\n--- Nhận xét tổng quan ---")
print("""
Dựa trên ma trận tương quan:
- Các biến DH1, DH2, DH3 đều thể hiện điểm thi đại học ở các lần/môn khác nhau
- Cần xem xét mức độ tương quan giữa chúng để hiểu mối liên hệ giữa các điểm số
""")

# 5. Vẽ biểu đồ
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Hàng 1: Scatter plots giữa các cặp biến
colors = ['#3498db', '#e74c3c', '#2ecc71']

# DH1 vs DH2
r12, p12 = stats.pearsonr(df['DH1'], df['DH2'])
axes[0, 0].scatter(df['DH1'], df['DH2'], alpha=0.6, c=colors[0], edgecolors='black', linewidth=0.5)
z = np.polyfit(df['DH1'], df['DH2'], 1)
p = np.poly1d(z)
x_line = np.linspace(df['DH1'].min(), df['DH1'].max(), 100)
axes[0, 0].plot(x_line, p(x_line), "r--", linewidth=2)
axes[0, 0].set_xlabel('DH1', fontsize=11)
axes[0, 0].set_ylabel('DH2', fontsize=11)
axes[0, 0].set_title(f'DH1 vs DH2\nr = {r12:.4f}', fontsize=12, fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)

# DH1 vs DH3
r13, p13 = stats.pearsonr(df['DH1'], df['DH3'])
axes[0, 1].scatter(df['DH1'], df['DH3'], alpha=0.6, c=colors[1], edgecolors='black', linewidth=0.5)
z = np.polyfit(df['DH1'], df['DH3'], 1)
p = np.poly1d(z)
x_line = np.linspace(df['DH1'].min(), df['DH1'].max(), 100)
axes[0, 1].plot(x_line, p(x_line), "r--", linewidth=2)
axes[0, 1].set_xlabel('DH1', fontsize=11)
axes[0, 1].set_ylabel('DH3', fontsize=11)
axes[0, 1].set_title(f'DH1 vs DH3\nr = {r13:.4f}', fontsize=12, fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)

# DH2 vs DH3
r23, p23 = stats.pearsonr(df['DH2'], df['DH3'])
axes[0, 2].scatter(df['DH2'], df['DH3'], alpha=0.6, c=colors[2], edgecolors='black', linewidth=0.5)
z = np.polyfit(df['DH2'], df['DH3'], 1)
p = np.poly1d(z)
x_line = np.linspace(df['DH2'].min(), df['DH2'].max(), 100)
axes[0, 2].plot(x_line, p(x_line), "r--", linewidth=2)
axes[0, 2].set_xlabel('DH2', fontsize=11)
axes[0, 2].set_ylabel('DH3', fontsize=11)
axes[0, 2].set_title(f'DH2 vs DH3\nr = {r23:.4f}', fontsize=12, fontweight='bold')
axes[0, 2].grid(True, alpha=0.3)

# Hàng 2: Ma trận tương quan heatmap và pair plot
# Ma trận tương quan heatmap
im = axes[1, 0].imshow(corr_matrix, cmap='RdYlBu_r', vmin=-1, vmax=1)
axes[1, 0].set_xticks(range(len(dh_vars)))
axes[1, 0].set_yticks(range(len(dh_vars)))
axes[1, 0].set_xticklabels(dh_vars)
axes[1, 0].set_yticklabels(dh_vars)
axes[1, 0].set_title('Ma trận Tương quan', fontsize=12, fontweight='bold')

# Thêm giá trị vào ô
for i in range(len(dh_vars)):
    for j in range(len(dh_vars)):
        text = axes[1, 0].text(j, i, f'{corr_matrix.iloc[i, j]:.3f}',
                               ha="center", va="center", color="black", fontsize=11)

fig.colorbar(im, ax=axes[1, 0], shrink=0.8)

# Ma trận hiệp phương sai heatmap
im2 = axes[1, 1].imshow(cov_matrix, cmap='YlOrRd')
axes[1, 1].set_xticks(range(len(dh_vars)))
axes[1, 1].set_yticks(range(len(dh_vars)))
axes[1, 1].set_xticklabels(dh_vars)
axes[1, 1].set_yticklabels(dh_vars)
axes[1, 1].set_title('Ma trận Hiệp phương sai', fontsize=12, fontweight='bold')

# Thêm giá trị vào ô
for i in range(len(dh_vars)):
    for j in range(len(dh_vars)):
        text = axes[1, 1].text(j, i, f'{cov_matrix.iloc[i, j]:.3f}',
                               ha="center", va="center", color="black", fontsize=11)

fig.colorbar(im2, ax=axes[1, 1], shrink=0.8)

# Boxplot so sánh 3 biến
bp = axes[1, 2].boxplot([df['DH1'], df['DH2'], df['DH3']], labels=['DH1', 'DH2', 'DH3'], 
                         patch_artist=True)
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
axes[1, 2].set_ylabel('Điểm', fontsize=11)
axes[1, 2].set_title('So sánh phân phối DH1, DH2, DH3', fontsize=12, fontweight='bold')
axes[1, 2].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('DuLieu/Phan5_Cau5_Correlation_DH.png', dpi=300, bbox_inches='tight')
plt.show()

# Vẽ pair plot với seaborn
try:
    fig3 = plt.figure(figsize=(10, 10))
    
    # Tạo pair plot thủ công
    pair_axes = [[None, None, None], [None, None, None], [None, None, None]]
    
    for i, var1 in enumerate(dh_vars):
        for j, var2 in enumerate(dh_vars):
            ax = fig3.add_subplot(3, 3, i*3 + j + 1)
            
            if i == j:
                # Histogram trên đường chéo
                ax.hist(df[var1], bins=15, color=colors[i], edgecolor='black', alpha=0.7)
                ax.set_xlabel(var1 if i == 2 else '')
            else:
                # Scatter plot
                ax.scatter(df[var2], df[var1], alpha=0.5, c=colors[i], s=30)
                
            if j == 0:
                ax.set_ylabel(var1)
            if i == 2:
                ax.set_xlabel(var2)
    
    fig3.suptitle('Pair Plot: DH1, DH2, DH3', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('DuLieu/Phan5_Cau5_PairPlot_DH.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print("\nĐã lưu biểu đồ: DuLieu/Phan5_Cau5_PairPlot_DH.png")
    
except Exception as e:
    print(f"\nLỗi khi vẽ pair plot: {e}")

print("\nĐã lưu biểu đồ: DuLieu/Phan5_Cau5_Correlation_DH.png")
