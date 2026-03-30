# ==============================================================================
# BÀI 11: LOẠI BỎ DỮ LIỆU THỪA GIỮA TẬP TRAIN VÀ TEST
# ==============================================================================
# Loại bỏ dữ liệu thừa đối với các hành khách xuất hiện trong cả 2 tập
# dữ liệu huấn luyện (train.csv) và đánh giá (test.csv).
# Ưu tiên giữ lại dữ liệu trong tập huấn luyện.
# ==============================================================================

import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

# Đường dẫn
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'Data')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'Output')
os.makedirs(OUTPUT_DIR, exist_ok=True)

if __name__ == '__main__':
    print("=" * 80)
    print("BÀI 11: LOẠI BỎ DỮ LIỆU THỪA GIỮA TẬP TRAIN VÀ TEST")
    print("=" * 80)

    # ── Tải dữ liệu gốc ──
    train_df = pd.read_csv(os.path.join(DATA_DIR, 'train.csv'))
    test_df = pd.read_csv(os.path.join(DATA_DIR, 'test.csv'))

    print(f"\n📊 Kích thước ban đầu:")
    print(f"  Train: {train_df.shape[0]} dòng x {train_df.shape[1]} cột")
    print(f"  Test : {test_df.shape[0]} dòng x {test_df.shape[1]} cột")

    # ── Xác định các cột chung giữa 2 tập ──
    common_cols = [col for col in train_df.columns if col in test_df.columns]
    print(f"\n📌 Các cột chung: {common_cols}")

    # ── Tìm hành khách trùng lặp ──
    # Sử dụng tổ hợp nhiều cột để xác định chính xác cùng 1 hành khách
    # (chỉ so sánh Name sẽ sai vì có thể trùng tên nhưng khác người)
    match_cols = ['Name', 'Sex', 'Ticket', 'Fare']
    print(f"\n🔍 Kiểm tra trùng lặp dựa trên các cột: {match_cols}")

    # Merge để tìm hành khách trùng
    duplicates = test_df.merge(train_df[match_cols], on=match_cols, how='inner')
    print(f"   → Số hành khách trùng lặp (cùng Name + Sex + Ticket + Fare): {len(duplicates)}")

    # Kiểm tra thêm trùng theo PassengerId
    dup_by_id = test_df[test_df['PassengerId'].isin(train_df['PassengerId'])]
    print(f"   → Số hành khách trùng PassengerId: {len(dup_by_id)}")

    # Kiểm tra trùng chỉ theo Name (để so sánh)
    dup_by_name = test_df[test_df['Name'].isin(train_df['Name'])]
    print(f"   → Số hành khách trùng Name (chỉ tham khảo): {len(dup_by_name)}")

    if len(dup_by_name) > 0:
        print("\n📋 Hành khách trùng tên (kiểm tra xem có phải cùng 1 người không):")
        for name in dup_by_name['Name'].values:
            train_row = train_df[train_df['Name'] == name][['PassengerId', 'Name', 'Age', 'Ticket', 'Fare']].iloc[0]
            test_row = test_df[test_df['Name'] == name][['PassengerId', 'Name', 'Age', 'Ticket', 'Fare']].iloc[0]
            print(f"\n  Tên: {name}")
            print(f"    Train → ID: {train_row['PassengerId']}, Age: {train_row['Age']}, "
                  f"Ticket: {train_row['Ticket']}, Fare: {train_row['Fare']}")
            print(f"    Test  → ID: {test_row['PassengerId']}, Age: {test_row['Age']}, "
                  f"Ticket: {test_row['Ticket']}, Fare: {test_row['Fare']}")
            is_same = (train_row['Ticket'] == test_row['Ticket'] and train_row['Fare'] == test_row['Fare'])
            print(f"    → {'CÙNG 1 NGƯỜI → Loại bỏ khỏi test' if is_same else 'KHÁC NGƯỜI (khác Ticket/Fare) → Giữ lại'}")

    # ── Loại bỏ dữ liệu trùng ──
    # Ưu tiên giữ lại dữ liệu trong tập huấn luyện
    # → Loại bỏ các hành khách trùng thực sự ra khỏi tập test
    if len(duplicates) > 0:
        # Lấy index các hành khách trùng trong test
        test_dup_idx = test_df.merge(train_df[match_cols], on=match_cols, how='inner', indicator=True).index
        test_cleaned = test_df.drop(test_dup_idx)
        print(f"\n⚠️  Đã loại bỏ {len(test_dup_idx)} hành khách trùng lặp khỏi tập test.")
    else:
        test_cleaned = test_df.copy()
        print(f"\n✅ Không có hành khách trùng lặp thực sự giữa 2 tập dữ liệu.")

    print(f"\n📊 Kích thước SAU KHI xử lý:")
    print(f"  Train: {train_df.shape[0]} dòng x {train_df.shape[1]} cột (giữ nguyên)")
    print(f"  Test : {test_cleaned.shape[0]} dòng x {test_cleaned.shape[1]} cột "
          f"(đã loại {test_df.shape[0] - test_cleaned.shape[0]} dòng trùng)")

    # ── Export kết quả ──
    train_output = os.path.join(OUTPUT_DIR, 'bai11_train_final.csv')
    test_output = os.path.join(OUTPUT_DIR, 'bai11_test_final.csv')

    train_df.to_csv(train_output, index=False)
    test_cleaned.to_csv(test_output, index=False)

    print(f"\n✅ Đã export tập train: Output/bai11_train_final.csv")
    print(f"✅ Đã export tập test (đã xử lý): Output/bai11_test_final.csv")
