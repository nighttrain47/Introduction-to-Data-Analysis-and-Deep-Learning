# -*- coding: utf-8 -*-
"""
Phần 5 - Câu 3: Khảo sát tương quan giữa biến DH1 theo biến T1
- Nhận xét giá trị Covariance hoặc Correlation
- Vẽ biểu đồ Scatter thể hiện liên hệ của biến phụ thuộc DH1 theo biến độc lập T1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

print("="*80)
print("KHẢO SÁT TƯƠNG QUAN GIỮA BIẾN DH1 VÀ BIẾN T1")
print("="*80)

# Tính Covariance và Correlation
DH1 = df['DH1']
T1 = df['T1']

# Covariance
covariance = np.cov(T1, DH1)[0, 1]

# Correlation (Pearson)
correlation, p_value = stats.pearsonr(T1, DH1)

# Thống kê
print("\n--- Thống kê mô tả ---")
print(f"T1: Mean = {T1.mean():.4f}, Std = {T1.std():.4f}")
print(f"DH1: Mean = {DH1.mean():.4f}, Std = {DH1.std():.4f}")

print("\n--- Covariance và Correlation ---")
print(f"Hiệp phương sai (Covariance): {covariance:.4f}")
print(f"Hệ số tương quan Pearson (r): {correlation:.4f}")
print(f"P-value: {p_value:.6f}")

# Nhận xét
print("\n--- Nhận xét ---")
if abs(correlation) < 0.3:
    strength = "yếu"
elif abs(correlation) < 0.7:
    strength = "trung bình"
else:
    strength = "mạnh"

direction = "thuận (dương)" if correlation > 0 else "nghịch (âm)"

print(f"Hệ số tương quan r = {correlation:.4f} cho thấy mối tương quan {strength} và {direction}.")
print(f"P-value = {p_value:.6f} {'< 0.05' if p_value < 0.05 else '>= 0.05'}")
if p_value < 0.05:
    print("=> Tương quan có ý nghĩa thống kê ở mức α = 0.05")
else:
    print("=> Tương quan không có ý nghĩa thống kê ở mức α = 0.05")

# Vẽ biểu đồ
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Biểu đồ Scatter
axes[0].scatter(T1, DH1, alpha=0.6, c='#3498db', edgecolors='black', linewidth=0.5)

# Thêm đường hồi quy
z = np.polyfit(T1, DH1, 1)
p = np.poly1d(z)
x_line = np.linspace(T1.min(), T1.max(), 100)
axes[0].plot(x_line, p(x_line), "r--", linewidth=2, label=f'y = {z[0]:.3f}x + {z[1]:.3f}')

axes[0].set_xlabel('T1 (Điểm Toán lần 1)', fontsize=12)
axes[0].set_ylabel('DH1 (Điểm ĐH lần 1)', fontsize=12)
axes[0].set_title(f'Scatter Plot: DH1 vs T1\nr = {correlation:.4f}, p = {p_value:.4f}', 
                  fontsize=13, fontweight='bold')
axes[0].legend(fontsize=10)
axes[0].grid(True, alpha=0.3)

# Thêm text annotation
textstr = f'Covariance: {covariance:.4f}\nCorrelation: {correlation:.4f}\nP-value: {p_value:.6f}'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
axes[0].text(0.05, 0.95, textstr, transform=axes[0].transAxes, fontsize=10,
             verticalalignment='top', bbox=props)

# Biểu đồ Scatter với heatmap density
from scipy.stats import gaussian_kde
xy = np.vstack([T1, DH1])
z_density = gaussian_kde(xy)(xy)
idx = z_density.argsort()
x_sorted, y_sorted, z_sorted = T1.iloc[idx], DH1.iloc[idx], z_density[idx]

scatter = axes[1].scatter(x_sorted, y_sorted, c=z_sorted, s=50, cmap='viridis', alpha=0.8)
plt.colorbar(scatter, ax=axes[1], label='Mật độ')

axes[1].set_xlabel('T1 (Điểm Toán lần 1)', fontsize=12)
axes[1].set_ylabel('DH1 (Điểm ĐH lần 1)', fontsize=12)
axes[1].set_title('Scatter Plot với Mật độ điểm', fontsize=13, fontweight='bold')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('DuLieu/Phan5_Cau3_Correlation_DH1_T1.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nĐã lưu biểu đồ: DuLieu/Phan5_Cau3_Correlation_DH1_T1.png")
