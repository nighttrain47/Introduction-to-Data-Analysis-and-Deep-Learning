# ==============================================================================
# BÀI 1: LOAD DỮ LIỆU VÀ HIỂN THỊ 10 DÒNG ĐẦU TIÊN
# ==============================================================================
# Viết hàm load_data() để tải dữ liệu lên ứng dụng.
# Sau đó, hiển thị ra màn hình 10 dòng đầu tiên.
# ==============================================================================

import pandas as pd
import os

# Đường dẫn
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'Data')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'Output')
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_data(filepath):
    """
    Hàm tải dữ liệu từ file CSV.
    
    Parameters:
        filepath (str): Đường dẫn đến file CSV
        
    Returns:
        pd.DataFrame: DataFrame chứa dữ liệu
    """
    df = pd.read_csv(filepath)
    return df


if __name__ == '__main__':
    print("=" * 80)
    print("BÀI 1: LOAD DỮ LIỆU VÀ HIỂN THỊ 10 DÒNG ĐẦU TIÊN")
    print("=" * 80)

    # Tải dữ liệu
    filepath = os.path.join(DATA_DIR, 'titanic_disaster.csv')
    df = load_data(filepath)

    # Hiển thị 10 dòng đầu tiên
    print("\n📋 10 dòng đầu tiên của dữ liệu:")
    print(df.head(10).to_string())

    print(f"\n📊 Kích thước dữ liệu: {df.shape[0]} dòng x {df.shape[1]} cột")
    print(f"\n📌 Các cột: {list(df.columns)}")
    print(f"\n📌 Kiểu dữ liệu:")
    print(df.dtypes)

    # Export kết quả
    output_file = os.path.join(OUTPUT_DIR, 'bai1_head10.csv')
    df.head(10).to_csv(output_file, index=False)
    print(f"\n✅ Đã export 10 dòng đầu ra file: {output_file}")

    # Lưu toàn bộ dữ liệu gốc để các bài sau dùng
    df.to_csv(os.path.join(OUTPUT_DIR, 'step0_original.csv'), index=False)
    print(f"✅ Đã lưu dữ liệu gốc vào: Output/step0_original.csv")
