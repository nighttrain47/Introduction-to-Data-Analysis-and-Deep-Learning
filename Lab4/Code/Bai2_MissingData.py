# ==============================================================================
# BÀI 2: THỐNG KÊ DỮ LIỆU THIẾU VÀ TRỰC QUAN HÓA BẰNG HEAT MAP
# ==============================================================================
# Thống kê dữ liệu thiếu trên các biến số và trực quan hóa dữ liệu thiếu
# bằng biểu đồ (Heat map).
# Nhận xét về tình trạng thiếu dữ liệu Age, Cabin và Embarked.
# ==============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# Đường dẫn
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'Data')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'Output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

if __name__ == '__main__':
    print("=" * 80)
    print("BÀI 2: THỐNG KÊ DỮ LIỆU THIẾU VÀ TRỰC QUAN HÓA BẰNG HEAT MAP")
    print("=" * 80)

    # Tải dữ liệu
    df = pd.read_csv(os.path.join(DATA_DIR, 'titanic_disaster.csv'))

    # ── Thống kê dữ liệu thiếu ──
    print("\n📊 Thống kê dữ liệu thiếu trên các biến số:")
    missing_data = pd.DataFrame({
        'Số lượng thiếu': df.isnull().sum(),
        'Phần trăm (%)': (df.isnull().sum() / len(df) * 100).round(2)
    })
    missing_all = missing_data.copy()
    missing_data = missing_data[missing_data['Số lượng thiếu'] > 0].sort_values(
        'Phần trăm (%)', ascending=False
    )
    print(missing_data)

    # ── Trực quan hóa bằng Heat map ──
    plt.figure(figsize=(14, 8))
    sns.heatmap(df.isnull(), yticklabels=False, cbar=True, cmap='viridis')
    plt.title('Heat Map - Dữ liệu thiếu trên toàn bộ dataset', fontsize=16, fontweight='bold')
    plt.xlabel('Các cột dữ liệu', fontsize=12)
    plt.ylabel('Các dòng dữ liệu', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'bai2_heatmap_missing.png'), dpi=150, bbox_inches='tight')
    plt.show()

    # ── Nhận xét ──
    nhan_xet = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    NHẬN XÉT VỀ TÌNH TRẠNG THIẾU DỮ LIỆU                   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  1. Age: Thiếu khoảng 19.87% (177/891 giá trị).                            ║
║     → Đây là mức thiếu vừa phải, có thể xử lý bằng phương pháp            ║
║       thay thế (imputation) như trung bình, trung vị hoặc theo nhóm.       ║
║                                                                              ║
║  2. Cabin: Thiếu khoảng 77.10% (687/891 giá trị).                          ║
║     → Đây là mức thiếu RẤT CAO. Phần lớn hành khách không có thông        ║
║       tin cabin, đặc biệt là hành khách hạng thấp (hạng 3).               ║
║     → Có thể trích xuất ký tự đầu (loại cabin) và thay NaN = "Unknown".   ║
║                                                                              ║
║  3. Embarked: Thiếu rất ít, chỉ 2 giá trị (0.22%).                        ║
║     → Dễ dàng xử lý bằng giá trị phổ biến nhất (mode).                    ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
    print(nhan_xet)

    # ── Export kết quả ──
    missing_all.to_csv(os.path.join(OUTPUT_DIR, 'bai2_missing_stats.csv'))
    print(f"✅ Đã export thống kê thiếu ra: Output/bai2_missing_stats.csv")
    print(f"✅ Đã export Heat map ra: Output/bai2_heatmap_missing.png")
