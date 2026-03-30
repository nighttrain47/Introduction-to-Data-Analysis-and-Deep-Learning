# -*- coding: utf-8 -*-
"""
LAB 1: BÀI THỰC HÀNH THAO TÁC DỮ LIỆU
Thao tác dữ liệu điểm thi đại học của học sinh
"""

import pandas as pd
import numpy as np

# ============================================================================
# Câu 1: Xác định và phân loại dữ liệu định tính và định lượng
# ============================================================================
print("=" * 80)
print("CÂU 1: PHÂN LOẠI DỮ LIỆU ĐỊNH TÍNH VÀ ĐỊNH LƯỢNG")
print("=" * 80)

print("""
DỮ LIỆU ĐỊNH TÍNH (Categorical/Qualitative):
- GT (Giới tính): Giá trị F/M - Thang đo danh nghĩa (Nominal)
- DT (Dân tộc): Giá trị số đại diện cho dân tộc - Thang đo danh nghĩa (Nominal)
- KV (Khu vực): Giá trị 1, 2, 2NT - Thang đo danh nghĩa (Nominal)
- KT (Khối thi): Giá trị A, A1, B, C, D1 - Thang đo danh nghĩa (Nominal)

DỮ LIỆU ĐỊNH LƯỢNG (Numerical/Quantitative):
- STT: Số thứ tự - Thang đo định danh (Nominal, dùng để xác định)
- T1, L1, H1, S1, V1, X1, D1, N1: Điểm TB lớp 10 - Thang đo tỉ lệ (Ratio)
- T2, L2, H2, S2, V2, X2, D2, N2: Điểm TB lớp 11 - Thang đo tỉ lệ (Ratio)
- T6, L6, H6, S6, V6, X6, D6, N6: Điểm TB lớp 12 - Thang đo tỉ lệ (Ratio)
  (Lưu ý: Trong file dữ liệu, cột lớp 12 được đánh số T6 thay vì T3)
- DH1, DH2, DH3: Điểm thi đại học môn 1, 2, 3 - Thang đo tỉ lệ (Ratio)
""")

# ============================================================================
# Câu 2: Định nghĩa các thang đo phù hợp cho từng biến số
# ============================================================================
print("=" * 80)
print("CÂU 2: ĐỊNH NGHĨA CÁC THANG ĐO PHÙ HỢP")
print("=" * 80)

print("""
THANG ĐO CHO TỪNG BIẾN SỐ:

1. THANG ĐO DANH NGHĨA (Nominal Scale):
   - STT: Định danh học sinh
   - GT (Giới tính): F = Nữ, M = Nam
   - DT (Dân tộc): Mã số đại diện dân tộc
   - KV (Khu vực): 1, 2, 2NT (các khu vực ưu tiên khác nhau)
   - KT (Khối thi): A, A1, B, C, D1 (các khối thi khác nhau)

2. THANG ĐO TỈ LỆ (Ratio Scale):
   - Tất cả các biến điểm số (T1-T6, L1-L6, H1-H6, S1-S6, V1-V6, X1-X6, D1-D6, N1-N6)
   - Điểm thi đại học (DH1, DH2, DH3)
   - Đặc điểm: Có điểm 0 tuyệt đối, có thể so sánh tỉ lệ
""")

# ============================================================================
# Câu 3: Tải dữ liệu và in 10 dòng đầu/cuối
# ============================================================================
print("=" * 80)
print("CÂU 3: TẢI DỮ LIỆU VÀ IN 10 DÒNG ĐẦU/CUỐI")
print("=" * 80)

# Đọc dữ liệu từ file CSV
file_path = r"DuLieu\dulieuxettuyendaihoc.csv"
df = pd.read_csv(file_path)

print("\n--- Thông tin tổng quan về dữ liệu ---")
print(f"Số dòng: {len(df)}")
print(f"Số cột: {len(df.columns)}")
print(f"Danh sách cột: {list(df.columns)}")

print("\n--- 10 DÒNG ĐẦU TIÊN ---")
print(df.head(10))

print("\n--- 10 DÒNG CUỐI CÙNG ---")
print(df.tail(10))

# ============================================================================
# Câu 4: Thống kê và hiệu chỉnh dữ liệu thiếu cho cột Dân tộc (DT)
# ============================================================================
print("\n" + "=" * 80)
print("CÂU 4: XỬ LÝ DỮ LIỆU THIẾU CHO CỘT DÂN TỘC (DT)")
print("=" * 80)

print("\n--- Thống kê dữ liệu cột DT trước khi xử lý ---")
print(f"Số giá trị thiếu (NaN): {df['DT'].isna().sum()}")
print(f"Số giá trị riêng biệt (unique): {df['DT'].nunique()}")
print(f"Các giá trị riêng biệt: {df['DT'].unique()}")

# Bảng tần số và tần suất
print("\n--- Bảng tần số và tần suất cột DT ---")
freq_dt = df['DT'].value_counts(dropna=False)
freq_pct_dt = df['DT'].value_counts(dropna=False, normalize=True) * 100
freq_table_dt = pd.DataFrame({
    'Tần số': freq_dt,
    'Tần suất (%)': freq_pct_dt.round(2)
})
print(freq_table_dt)

# Thay thế dữ liệu thiếu bằng 0
df['DT'] = df['DT'].fillna(0)

print("\n--- Sau khi thay thế dữ liệu thiếu bằng 0 ---")
print(f"Số giá trị thiếu (NaN): {df['DT'].isna().sum()}")
print(f"Các giá trị riêng biệt: {df['DT'].unique()}")

# ============================================================================
# Câu 5: Thống kê và hiệu chỉnh dữ liệu thiếu cho biến T1 (dùng Mean)
# ============================================================================
print("\n" + "=" * 80)
print("CÂU 5: XỬ LÝ DỮ LIỆU THIẾU CHO BIẾN T1 (PHƯƠNG PHÁP MEAN)")
print("=" * 80)

print("\n--- Thống kê dữ liệu cột T1 trước khi xử lý ---")
print(f"Số giá trị thiếu (NaN): {df['T1'].isna().sum()}")
print(f"Giá trị trung bình (mean): {df['T1'].mean():.4f}")
print(f"Giá trị nhỏ nhất: {df['T1'].min()}")
print(f"Giá trị lớn nhất: {df['T1'].max()}")

# Bảng tần số và tần suất
print("\n--- Bảng tần số cột T1 ---")
freq_t1 = df['T1'].value_counts(dropna=False).sort_index()
print(freq_t1)

# Tính giá trị trung bình
mean_t1 = df['T1'].mean()
print(f"\nGiá trị Mean của T1: {mean_t1:.4f}")

# Thay thế dữ liệu thiếu bằng Mean
df['T1'] = df['T1'].fillna(mean_t1)

print("\n--- Sau khi thay thế dữ liệu thiếu bằng Mean ---")
print(f"Số giá trị thiếu (NaN): {df['T1'].isna().sum()}")

# ============================================================================
# Câu 6: Xử lý dữ liệu thiếu cho tất cả các biến điểm số còn lại
# ============================================================================
print("\n" + "=" * 80)
print("CÂU 6: XỬ LÝ DỮ LIỆU THIẾU CHO TẤT CẢ CÁC BIẾN ĐIỂM SỐ")
print("=" * 80)

# Danh sách các cột điểm số (trừ T1 đã xử lý)
# Lớp 10: T1, L1, H1, S1, V1, X1, D1, N1
# Lớp 11: T2, L2, H2, S2, V2, X2, D2, N2
# Lớp 12: T3-T5, L3-L5, H3-H5, S3-S5, V3-V5, X3-X5, D3-D5, N3-N5 (trong file là T6, L6...)
# Điểm đại học: DH1, DH2, DH3

# Lấy danh sách các cột điểm số từ file (loại trừ STT, GT, DT, KV, KT)
non_score_cols = ['STT', 'GT', 'DT', 'KV', 'KT']
score_cols = [col for col in df.columns if col not in non_score_cols]

print("Danh sách các cột điểm số cần xử lý:")
print(score_cols)

print("\n--- Thống kê dữ liệu thiếu trước khi xử lý ---")
missing_before = df[score_cols].isna().sum()
missing_before_filtered = missing_before[missing_before > 0]
if len(missing_before_filtered) > 0:
    print(missing_before_filtered)
else:
    print("Không có dữ liệu thiếu trong các cột điểm số!")

# Thay thế dữ liệu thiếu bằng Mean cho từng cột
for col in score_cols:
    if df[col].isna().sum() > 0:
        mean_val = df[col].mean()
        print(f"Cột {col}: Thay thế {df[col].isna().sum()} giá trị thiếu bằng Mean = {mean_val:.4f}")
        df[col] = df[col].fillna(mean_val)

print("\n--- Sau khi xử lý ---")
missing_after = df[score_cols].isna().sum().sum()
print(f"Tổng số giá trị thiếu còn lại trong các cột điểm số: {missing_after}")

# ============================================================================
# Câu 7: Tạo các biến TBM1, TBM2, TBM3
# ============================================================================
print("\n" + "=" * 80)
print("CÂU 7: TẠO CÁC BIẾN TBM1, TBM2, TBM3")
print("=" * 80)

print("""
Công thức: TBM = (T*2 + L + H + S + V*2 + X + D + N) / 10
""")

# Lớp 10 (suffix 1)
df['TBM1'] = (df['T1']*2 + df['L1'] + df['H1'] + df['S1'] + 
              df['V1']*2 + df['X1'] + df['D1'] + df['N1']) / 10

# Lớp 11 (suffix 2)
df['TBM2'] = (df['T2']*2 + df['L2'] + df['H2'] + df['S2'] + 
              df['V2']*2 + df['X2'] + df['D2'] + df['N2']) / 10

# Lớp 12 (suffix 6 trong file dữ liệu)
df['TBM3'] = (df['T6']*2 + df['L6'] + df['H6'] + df['S6'] + 
              df['V6']*2 + df['X6'] + df['D6'] + df['N6']) / 10

print("--- Thống kê TBM1, TBM2, TBM3 ---")
print(df[['TBM1', 'TBM2', 'TBM3']].describe())

print("\n--- 5 dòng đầu tiên của TBM ---")
print(df[['STT', 'TBM1', 'TBM2', 'TBM3']].head())

# ============================================================================
# Câu 8: Tạo các biến xếp loại XL1, XL2, XL3
# ============================================================================
print("\n" + "=" * 80)
print("CÂU 8: TẠO CÁC BIẾN XẾP LOẠI XL1, XL2, XL3")
print("=" * 80)

print("""
Quy tắc xếp loại:
- Nhỏ hơn 5.0: Yếu (Y)
- Từ 5.0 đến dưới 6.5: Trung bình (TB)
- Từ 6.5 đến dưới 8.0: Khá (K)
- Từ 8.0 đến dưới 9.0: Giỏi (G)
- Từ 9.0 trở lên: Xuất sắc (XS)
""")

def xep_loai(diem):
    """Hàm xếp loại dựa trên điểm trung bình"""
    if diem < 5.0:
        return 'Y'
    elif diem < 6.5:
        return 'TB'
    elif diem < 8.0:
        return 'K'
    elif diem < 9.0:
        return 'G'
    else:
        return 'XS'

df['XL1'] = df['TBM1'].apply(xep_loai)
df['XL2'] = df['TBM2'].apply(xep_loai)
df['XL3'] = df['TBM3'].apply(xep_loai)

print("--- Phân bố xếp loại ---")
print("\nXếp loại lớp 10 (XL1):")
print(df['XL1'].value_counts().sort_index())

print("\nXếp loại lớp 11 (XL2):")
print(df['XL2'].value_counts().sort_index())

print("\nXếp loại lớp 12 (XL3):")
print(df['XL3'].value_counts().sort_index())

print("\n--- 5 dòng đầu tiên của XL ---")
print(df[['STT', 'TBM1', 'XL1', 'TBM2', 'XL2', 'TBM3', 'XL3']].head())

# ============================================================================
# Câu 9: Tạo các biến US_TBM1, US_TBM2, US_TBM3 (Min-Max Normalization)
# ============================================================================
print("\n" + "=" * 80)
print("CÂU 9: CHUYỂN ĐỔI ĐIỂM SANG THANG 4 (MIN-MAX NORMALIZATION)")
print("=" * 80)

print("""
Công thức Min-Max Normalization:
US_TBM = (TBM - min) / (max - min) * (new_max - new_min) + new_min

Với thang điểm 10 VN (0-10) sang thang điểm 4 Mỹ (0-4):
US_TBM = (TBM - 0) / (10 - 0) * (4 - 0) + 0 = TBM * 4 / 10 = TBM * 0.4
""")

# Min-Max Normalization từ thang 10 sang thang 4
def min_max_normalize(value, old_min=0, old_max=10, new_min=0, new_max=4):
    return (value - old_min) / (old_max - old_min) * (new_max - new_min) + new_min

df['US_TBM1'] = df['TBM1'].apply(min_max_normalize)
df['US_TBM2'] = df['TBM2'].apply(min_max_normalize)
df['US_TBM3'] = df['TBM3'].apply(min_max_normalize)

print("--- Thống kê US_TBM1, US_TBM2, US_TBM3 (thang điểm 4) ---")
print(df[['US_TBM1', 'US_TBM2', 'US_TBM3']].describe())

print("\n--- So sánh điểm VN và Mỹ (5 dòng đầu) ---")
print(df[['STT', 'TBM1', 'US_TBM1', 'TBM2', 'US_TBM2', 'TBM3', 'US_TBM3']].head())

# ============================================================================
# Câu 10: Tạo biến kết quả xét tuyển (KQXT)
# ============================================================================
print("\n" + "=" * 80)
print("CÂU 10: TẠO BIẾN KẾT QUẢ XÉT TUYỂN (KQXT)")
print("=" * 80)

print("""
Quy tắc xét tuyển:
- Khối A, A1: (DH1*2 + DH2 + DH3) / 4 >= 5.0 -> Đậu (1), ngược lại Rớt (0)
- Khối B: (DH1 + DH2*2 + DH3) / 4 >= 5.0 -> Đậu (1), ngược lại Rớt (0)
- Khối khác: (DH1 + DH2 + DH3) / 3 >= 5.0 -> Đậu (1), ngược lại Rớt (0)
""")

def ket_qua_xet_tuyen(row):
    """Hàm tính kết quả xét tuyển dựa trên khối thi và điểm"""
    dh1, dh2, dh3 = row['DH1'], row['DH2'], row['DH3']
    kt = row['KT']
    
    if kt in ['A', 'A1']:
        diem_xet = (dh1 * 2 + dh2 + dh3) / 4
    elif kt == 'B':
        diem_xet = (dh1 + dh2 * 2 + dh3) / 4
    else:  # C, D1 và các khối khác
        diem_xet = (dh1 + dh2 + dh3) / 3
    
    return 1 if diem_xet >= 5.0 else 0

df['KQXT'] = df.apply(ket_qua_xet_tuyen, axis=1)

print("--- Thống kê kết quả xét tuyển ---")
print(f"Số học sinh đậu: {(df['KQXT'] == 1).sum()}")
print(f"Số học sinh rớt: {(df['KQXT'] == 0).sum()}")
print(f"Tỉ lệ đậu: {(df['KQXT'] == 1).sum() / len(df) * 100:.2f}%")

print("\n--- Kết quả theo khối thi ---")
print(df.groupby('KT')['KQXT'].agg(['sum', 'count', 'mean']).rename(
    columns={'sum': 'Đậu', 'count': 'Tổng', 'mean': 'Tỉ lệ đậu'}
))

print("\n--- 10 dòng đầu với kết quả xét tuyển ---")
print(df[['STT', 'KT', 'DH1', 'DH2', 'DH3', 'KQXT']].head(10))

# ============================================================================
# Câu 11: Lưu dữ liệu xuống file
# ============================================================================
print("\n" + "=" * 80)
print("CÂU 11: LƯU DỮ LIỆU XUỐNG FILE")
print("=" * 80)

output_path = r"DuLieu\processed_dulieuxettuyendaihoc.csv"
df.to_csv(output_path, index=False, encoding='utf-8')

print(f"Đã lưu dữ liệu vào file: {output_path}")
print(f"Số dòng: {len(df)}")
print(f"Số cột: {len(df.columns)}")
print(f"Danh sách cột: {list(df.columns)}")

# Hiển thị thông tin tổng quan của DataFrame cuối cùng
print("\n--- THÔNG TIN TỔNG QUAN CỦA DỮ LIỆU SAU KHI XỬ LÝ ---")
print(df.info())

print("\n" + "=" * 80)
print("HOÀN THÀNH LAB 1!")
print("=" * 80)
