# ==============================================================================
# BÀI 3: TÁCH CỘT NAME THÀNH firstName VÀ secondName
# ==============================================================================
# Xử lý tên cột tên Name, tách ra làm 2 cột: firstName và secondName.
# Lưu ý: Sau khi tách cột xong thì xóa luôn cột Name.
# ==============================================================================

import pandas as pd
import os

# Đường dẫn
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'Data')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'Output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

if __name__ == '__main__':
    print("=" * 80)
    print("BÀI 3: TÁCH CỘT NAME THÀNH firstName VÀ secondName")
    print("=" * 80)

    # Tải dữ liệu
    df = pd.read_csv(os.path.join(DATA_DIR, 'titanic_disaster.csv'))

    # ── Hiển thị trước khi tách ──
    print("\n📋 Dữ liệu cột Name trước khi tách (5 dòng đầu):")
    print(df[['PassengerId', 'Name']].head().to_string())

    # ── Tách cột Name ──
    # Format: "Braund, Mr. Owen Harris" 
    #   → firstName  = "Braund"              (phần trước dấu phẩy)
    #   → secondName = "Mr. Owen Harris"     (phần sau dấu phẩy)
    df['firstName'] = df['Name'].str.split(', ', n=1).str[0]
    df['secondName'] = df['Name'].str.split(', ', n=1).str[1]

    # Xóa cột Name
    df.drop('Name', axis=1, inplace=True)

    # ── Hiển thị sau khi tách ──
    print("\n📋 Dữ liệu sau khi tách (10 dòng đầu):")
    print(df[['PassengerId', 'firstName', 'secondName']].head(10).to_string())
    print(f"\n📌 Các cột hiện tại: {list(df.columns)}")

    # ── Export kết quả ──
    output_file = os.path.join(OUTPUT_DIR, 'bai3_split_name.csv')
    df.to_csv(output_file, index=False)
    print(f"\n✅ Đã export kết quả ra: Output/bai3_split_name.csv")
