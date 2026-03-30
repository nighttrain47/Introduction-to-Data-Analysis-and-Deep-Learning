# -*- coding: utf-8 -*-
"""
Phần 5 - Câu 1: Mô tả và khảo sát phân phối cho biến T1
- Mô tả độ tập trung và phân tán của dữ liệu T1
- Vẽ biểu đồ Box-Plot và xác định các đại lượng
- Mô tả hình dáng lệch của phân phối T1
- Vẽ biểu đồ Histogram biểu thị hình dáng phân phối
- Mô tả các đặc trưng của phân phối, mức độ lệch và nhọn
- Kiểm chứng phân phối chuẩn QQ-Plot
- Nhận xét và đánh giá về phân phối của T1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import scipy.stats as st

# Đọc dữ liệu
df = pd.read_csv('DuLieu/processed_dulieuxettuyendaihoc.csv')

T1 = df['T1']

print("="*80)
print("MÔ TẢ VÀ KHẢO SÁT PHÂN PHỐI CHO BIẾN T1 (ĐIỂM TOÁN LẦN 1)")
print("="*80)

# 1. Mô tả độ tập trung và phân tán
print("\n" + "="*60)
print("1. ĐỘ TẬP TRUNG VÀ PHÂN TÁN CỦA DỮ LIỆU T1")
print("="*60)

# Các đại lượng thống kê
n = len(T1)
mean = T1.mean()
median = T1.median()
mode = T1.mode().values[0] if len(T1.mode()) > 0 else np.nan
std = T1.std()
var = T1.var()
min_val = T1.min()
max_val = T1.max()
range_val = max_val - min_val
q1 = T1.quantile(0.25)
q2 = T1.quantile(0.50)  # Median
q3 = T1.quantile(0.75)
iqr = q3 - q1

print(f"Số quan sát (n): {n}")
print(f"Giá trị nhỏ nhất (Min): {min_val:.4f}")
print(f"Giá trị lớn nhất (Max): {max_val:.4f}")
print(f"Khoảng biến thiên (Range): {range_val:.4f}")
print(f"\nĐộ tập trung:")
print(f"  Trung bình (Mean): {mean:.4f}")
print(f"  Trung vị (Median): {median:.4f}")
print(f"  Mode: {mode:.4f}")
print(f"\nĐộ phân tán:")
print(f"  Phương sai (Variance): {var:.4f}")
print(f"  Độ lệch chuẩn (Std): {std:.4f}")
print(f"\nCác phân vị:")
print(f"  Q1 (25%): {q1:.4f}")
print(f"  Q2 (50%): {q2:.4f}")
print(f"  Q3 (75%): {q3:.4f}")
print(f"  IQR (Q3-Q1): {iqr:.4f}")

# 2. Mô tả hình dáng lệch
print("\n" + "="*60)
print("2. HÌNH DÁNG LỆCH CỦA PHÂN PHỐI T1")
print("="*60)

skewness = T1.skew()
kurtosis = T1.kurtosis()

print(f"Độ lệch (Skewness): {skewness:.4f}")
if skewness > 0:
    print("  -> Phân phối lệch phải (đuôi dài bên phải)")
elif skewness < 0:
    print("  -> Phân phối lệch trái (đuôi dài bên trái)")
else:
    print("  -> Phân phối đối xứng")

print(f"\nĐộ nhọn (Kurtosis): {kurtosis:.4f}")
if kurtosis > 0:
    print("  -> Phân phối nhọn hơn phân phối chuẩn (leptokurtic)")
elif kurtosis < 0:
    print("  -> Phân phối bẹt hơn phân phối chuẩn (platykurtic)")
else:
    print("  -> Độ nhọn tương đương phân phối chuẩn (mesokurtic)")

# So sánh Mean và Median
print(f"\nSo sánh Mean và Median:")
print(f"  Mean - Median = {mean - median:.4f}")
if mean > median:
    print("  -> Mean > Median: Phân phối có khả năng lệch phải")
elif mean < median:
    print("  -> Mean < Median: Phân phối có khả năng lệch trái")
else:
    print("  -> Mean ≈ Median: Phân phối có khả năng đối xứng")

# 3. Vẽ biểu đồ
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 3.1 Box-Plot
bp = axes[0, 0].boxplot(T1, vert=True, patch_artist=True)
bp['boxes'][0].set_facecolor('#3498db')
axes[0, 0].set_ylabel('Điểm T1', fontsize=11)
axes[0, 0].set_title('Box-Plot của biến T1', fontsize=13, fontweight='bold')
axes[0, 0].grid(axis='y', alpha=0.3)

# Đánh dấu các đại lượng trên boxplot
axes[0, 0].axhline(q1, color='orange', linestyle='--', linewidth=1, alpha=0.7)
axes[0, 0].axhline(q2, color='red', linestyle='-', linewidth=2, alpha=0.7)
axes[0, 0].axhline(q3, color='orange', linestyle='--', linewidth=1, alpha=0.7)

# Thêm nhãn
textstr = f'Min: {min_val:.2f}\nQ1: {q1:.2f}\nQ2: {q2:.2f}\nQ3: {q3:.2f}\nMax: {max_val:.2f}\nIQR: {iqr:.2f}'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
axes[0, 0].text(1.15, 0.5, textstr, transform=axes[0, 0].transAxes, fontsize=10,
                verticalalignment='center', bbox=props)

# 3.2 Histogram với đường cong phân phối
axes[0, 1].hist(T1, bins=15, density=True, color='#3498db', edgecolor='black', alpha=0.7, label='Histogram')

# Thêm đường cong phân phối chuẩn
xmin, xmax = axes[0, 1].get_xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, mean, std)
axes[0, 1].plot(x, p, 'r-', linewidth=2, label='Normal Distribution')

axes[0, 1].axvline(mean, color='green', linestyle='--', linewidth=2, label=f'Mean = {mean:.2f}')
axes[0, 1].axvline(median, color='orange', linestyle='--', linewidth=2, label=f'Median = {median:.2f}')
axes[0, 1].set_xlabel('Điểm T1', fontsize=11)
axes[0, 1].set_ylabel('Mật độ (Density)', fontsize=11)
axes[0, 1].set_title('Histogram của biến T1', fontsize=13, fontweight='bold')
axes[0, 1].legend(fontsize=9)
axes[0, 1].grid(axis='y', alpha=0.3)

# 3.3 QQ-Plot
stats.probplot(T1, dist="norm", plot=axes[1, 0])
axes[1, 0].set_title('QQ-Plot - Kiểm tra phân phối chuẩn', fontsize=13, fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)

# 3.4 Biểu đồ phân phối tích lũy
sorted_T1 = np.sort(T1)
cumulative = np.arange(1, len(sorted_T1) + 1) / len(sorted_T1)
axes[1, 1].plot(sorted_T1, cumulative, marker='.', linestyle='-', color='#3498db')
axes[1, 1].set_xlabel('Điểm T1', fontsize=11)
axes[1, 1].set_ylabel('Tần suất tích lũy', fontsize=11)
axes[1, 1].set_title('Đồ thị phân phối tích lũy (CDF)', fontsize=13, fontweight='bold')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('DuLieu/Phan5_Cau1_T1_Distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# 4. Kiểm định phân phối chuẩn
print("\n" + "="*60)
print("3. KIỂM ĐỊNH PHÂN PHỐI CHUẨN")
print("="*60)

# Shapiro-Wilk test
stat_sw, p_sw = stats.shapiro(T1)
print(f"\nShapiro-Wilk Test:")
print(f"  Statistic: {stat_sw:.4f}")
print(f"  P-value: {p_sw:.4f}")
if p_sw > 0.05:
    print("  -> Kết luận: Không bác bỏ H0, dữ liệu có thể tuân theo phân phối chuẩn (α=0.05)")
else:
    print("  -> Kết luận: Bác bỏ H0, dữ liệu KHÔNG tuân theo phân phối chuẩn (α=0.05)")

# Kolmogorov-Smirnov test
stat_ks, p_ks = stats.kstest(T1, 'norm', args=(mean, std))
print(f"\nKolmogorov-Smirnov Test:")
print(f"  Statistic: {stat_ks:.4f}")
print(f"  P-value: {p_ks:.4f}")
if p_ks > 0.05:
    print("  -> Kết luận: Không bác bỏ H0, dữ liệu có thể tuân theo phân phối chuẩn (α=0.05)")
else:
    print("  -> Kết luận: Bác bỏ H0, dữ liệu KHÔNG tuân theo phân phối chuẩn (α=0.05)")

# 5. Nhận xét và đánh giá
print("\n" + "="*60)
print("4. NHẬN XÉT VÀ ĐÁNH GIÁ VỀ PHÂN PHỐI CỦA T1")
print("="*60)
print(f"""
1. Độ tập trung:
   - Điểm trung bình T1 là {mean:.2f}, cho thấy mức điểm trung bình khá.
   - Trung vị ({median:.2f}) gần với trung bình, cho thấy phân phối khá đối xứng.

2. Độ phân tán:
   - Độ lệch chuẩn là {std:.2f}, cho thấy mức độ biến động vừa phải.
   - Khoảng biến thiên từ {min_val:.2f} đến {max_val:.2f}.

3. Hình dáng phân phối:
   - Skewness = {skewness:.4f}: Phân phối {'lệch phải' if skewness > 0 else 'lệch trái' if skewness < 0 else 'đối xứng'}
   - Kurtosis = {kurtosis:.4f}: Phân phối {'nhọn hơn' if kurtosis > 0 else 'bẹt hơn' if kurtosis < 0 else 'tương đương'} phân phối chuẩn

4. Kiểm định phân phối chuẩn:
   - Dựa trên QQ-Plot và các kiểm định thống kê, phân phối của T1 
     {'có thể' if p_sw > 0.05 else 'không'} tuân theo phân phối chuẩn.
""")

print("\nĐã lưu biểu đồ: DuLieu/Phan5_Cau1_T1_Distribution.png")
