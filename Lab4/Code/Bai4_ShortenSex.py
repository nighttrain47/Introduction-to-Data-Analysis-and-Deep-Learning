# ==============================================================================
# BÀI 4: RÚT GỌN KÍCH THƯỚC DỮ LIỆU TRÊN CỘT SEX
# ==============================================================================
# Xử lý rút gọn kích thước dữ liệu trên cột Sex:
# male → M và female → F
# ==============================================================================

import pandas as pd
import os

# Đường dẫn
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'Data')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'Output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

if __name__ == '__main__':
    print("=" * 80)
    print("BÀI 4: RÚT GỌN KÍCH THƯỚC DỮ LIỆU TRÊN CỘT SEX")
    print("=" * 80)

    # Tải dữ liệu từ bài 3
    df = pd.read_csv(os.path.join(OUTPUT_DIR, 'bai3_split_name.csv'))

    # ── Trước khi rút gọn ──
    print("\n📋 Giá trị cột Sex TRƯỚC khi rút gọn:")
    print(df['Sex'].value_counts())

    # ── Thay thế ──
    df['Sex'] = df['Sex'].replace({'male': 'M', 'female': 'F'})

    # ── Sau khi rút gọn ──
    print("\n📋 Giá trị cột Sex SAU khi rút gọn:")
    print(df['Sex'].value_counts())

    print("\n📋 5 dòng đầu:")
    print(df[['PassengerId', 'Sex', 'firstName']].head().to_string())

    # ── Export kết quả ──
    output_file = os.path.join(OUTPUT_DIR, 'bai4_shorten_sex.csv')
    df.to_csv(output_file, index=False)
    print(f"\n✅ Đã export kết quả ra: Output/bai4_shorten_sex.csv")
