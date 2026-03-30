# ==============================================================
# Fashion-MNIST Validation Script
# ==============================================================
# Cho phép:
#   1. Bỏ ảnh bên ngoài vào để mô hình nhận diện
#   2. Chọn index hoặc random từ tập test để kiểm tra
#   3. Xuất ảnh so sánh kết quả
# ==============================================================
# Cách sử dụng:
#   python Validation/validate.py                        → Random 1 ảnh từ test set
#   python Validation/validate.py --index 42             → Lấy ảnh index 42 từ test set
#   python Validation/validate.py --image path/to/image  → Nhận diện ảnh bên ngoài
#   python Validation/validate.py --random 9             → Random 9 ảnh từ test set
# ==============================================================

import os
import sys
import argparse
import numpy as np
import torch
import torch.nn as nn
from torchvision import datasets, transforms
from PIL import Image
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ========================
# CẤU HÌNH
# ========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'Data')
MODEL_PATH = os.path.join(BASE_DIR, 'Model', 'fashion_mnist_model.pth')
VALIDATION_DIR = os.path.join(BASE_DIR, 'Validation')
OUTPUT_DIR = os.path.join(VALIDATION_DIR, 'results')

os.makedirs(OUTPUT_DIR, exist_ok=True)

CLASS_NAMES = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]

CLASS_NAMES_VI = [
    'Áo thun', 'Quần dài', 'Áo kéo', 'Váy đầm', 'Áo khoác',
    'Dép sandal', 'Áo sơ mi', 'Giày thể thao', 'Túi xách', 'Bốt cổ ngắn'
]


# ========================
# MÔ HÌNH
# ========================

class FashionDNN(nn.Module):
    def __init__(self):
        super(FashionDNN, self).__init__()
        self.network = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        return self.network(x)


def load_model():
    """Tải mô hình đã huấn luyện"""
    if not os.path.exists(MODEL_PATH):
        print(f"❌ Không tìm thấy model tại: {MODEL_PATH}")
        print("   Hãy chạy Model/fashion_mnist_dnn.py trước để huấn luyện!")
        sys.exit(1)

    model = FashionDNN()
    model.load_state_dict(torch.load(MODEL_PATH, map_location='cpu', weights_only=True))
    model.eval()
    print(f"✅ Đã tải model từ: {MODEL_PATH}")
    return model


# ========================
# TIỀN XỬ LÝ ẢNH
# ========================

def preprocess_external_image(image_path):
    """
    Tiền xử lý ảnh bên ngoài thành tensor 28x28 grayscale
    - Chuyển sang grayscale
    - Resize về 28x28
    - Đảo ngược nếu nền trắng (Fashion-MNIST có nền đen)
    - Normalize
    """
    if not os.path.exists(image_path):
        print(f"❌ Không tìm thấy ảnh: {image_path}")
        sys.exit(1)

    # Đọc và chuyển grayscale
    img = Image.open(image_path).convert('L')
    original_img = img.copy()

    # Resize về 28x28
    img = img.resize((28, 28), Image.LANCZOS)

    # Chuyển sang numpy
    img_array = np.array(img, dtype=np.float32)

    # Tự động phát hiện nền: nếu trung bình pixel > 127 → nền trắng → đảo ngược
    if img_array.mean() > 127:
        img_array = 255.0 - img_array
        print("  ℹ️  Phát hiện nền trắng → đã đảo ngược (nền đen như Fashion-MNIST)")

    # Normalize về [0, 1] rồi chuẩn hóa
    img_array = img_array / 255.0

    # Chuyển thành tensor và normalize giống lúc train
    tensor = torch.FloatTensor(img_array).unsqueeze(0).unsqueeze(0)  # [1, 1, 28, 28]
    tensor = (tensor - 0.5) / 0.5  # Normalize về [-1, 1]

    return tensor, img_array, original_img


# ========================
# DỰ ĐOÁN
# ========================

def predict(model, tensor):
    """Dự đoán class và xác suất"""
    with torch.no_grad():
        outputs = model(tensor)
        probabilities = torch.softmax(outputs, dim=1)
        confidence, predicted = torch.max(probabilities, 1)

    return predicted.item(), confidence.item(), probabilities.squeeze().numpy()


def create_result_image_external(original_img, processed_img, pred_class, confidence, probs, save_path):
    """Tạo ảnh kết quả cho ảnh bên ngoài"""
    fig = plt.figure(figsize=(16, 5))
    gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 2])

    # Ảnh gốc
    ax1 = fig.add_subplot(gs[0])
    ax1.imshow(original_img, cmap='gray')
    ax1.set_title('Ảnh gốc (Input)', fontsize=13, fontweight='bold')
    ax1.axis('off')

    # Ảnh sau xử lý (28x28)
    ax2 = fig.add_subplot(gs[1])
    ax2.imshow(processed_img, cmap='gray')
    ax2.set_title(f'Sau xử lý (28×28)', fontsize=13, fontweight='bold')
    ax2.axis('off')

    # Biểu đồ xác suất
    ax3 = fig.add_subplot(gs[2])
    colors = ['#2ecc71' if i == pred_class else '#95a5a6' for i in range(10)]
    bars = ax3.barh(range(10), probs * 100, color=colors, edgecolor='white', height=0.7)
    ax3.set_yticks(range(10))
    ax3.set_yticklabels([f'{CLASS_NAMES[i]}\n({CLASS_NAMES_VI[i]})' for i in range(10)], fontsize=9)
    ax3.set_xlabel('Xác suất (%)', fontsize=11)
    ax3.set_title('Kết quả dự đoán', fontsize=13, fontweight='bold')
    ax3.set_xlim(0, 105)
    ax3.invert_yaxis()

    # Thêm % lên mỗi bar
    for i, (bar, prob) in enumerate(zip(bars, probs)):
        if prob > 0.01:
            ax3.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
                     f'{prob * 100:.1f}%', va='center', fontsize=9,
                     fontweight='bold' if i == pred_class else 'normal')

    fig.suptitle(
        f'🎯 Kết quả: {CLASS_NAMES[pred_class]} ({CLASS_NAMES_VI[pred_class]}) — Độ tin cậy: {confidence * 100:.1f}%',
        fontsize=14, fontweight='bold', y=1.02
    )

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  📸 Đã lưu kết quả: {save_path}")


def create_result_image_dataset(images, true_labels, pred_classes, confidences, all_probs, save_path, n):
    """Tạo ảnh kết quả cho nhiều ảnh từ dataset"""
    cols = min(n, 5)
    rows = (n + cols - 1) // cols

    fig, axes = plt.subplots(rows, cols, figsize=(4 * cols, 5 * rows))
    if rows == 1 and cols == 1:
        axes = np.array([[axes]])
    elif rows == 1:
        axes = axes.reshape(1, -1)
    elif cols == 1:
        axes = axes.reshape(-1, 1)

    fig.suptitle('Kết quả kiểm tra trên tập dữ liệu Fashion-MNIST', fontsize=16, fontweight='bold')

    for i in range(rows * cols):
        ax = axes[i // cols, i % cols]
        if i < n:
            img = images[i]
            true_label = true_labels[i]
            pred_label = pred_classes[i]
            conf = confidences[i]
            is_correct = true_label == pred_label

            ax.imshow(img, cmap='gray')

            # Tiêu đề: thật vs dự đoán
            title = (
                f"Thật: {CLASS_NAMES[true_label]}\n"
                f"Đoán: {CLASS_NAMES[pred_label]} ({conf * 100:.1f}%)"
            )
            title_color = '#2ecc71' if is_correct else '#e74c3c'
            ax.set_title(title, fontsize=10, fontweight='bold', color=title_color)

            # Viền
            border_color = '#2ecc71' if is_correct else '#e74c3c'
            for spine in ax.spines.values():
                spine.set_edgecolor(border_color)
                spine.set_linewidth(3)
                spine.set_visible(True)

            # Icon đúng/sai
            icon = '✅' if is_correct else '❌'
            ax.text(1, 1, icon, fontsize=16, transform=ax.transAxes,
                    ha='right', va='top')
        ax.set_xticks([])
        ax.set_yticks([])

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  📸 Đã lưu kết quả: {save_path}")


# ========================
# CHẾ ĐỘ KIỂM TRA
# ========================

def validate_external_image(model, image_path):
    """Kiểm tra ảnh bên ngoài"""
    print(f"\n🖼️  Đang nhận diện ảnh: {image_path}")

    tensor, processed_img, original_img = preprocess_external_image(image_path)
    pred_class, confidence, probs = predict(model, tensor)

    print(f"\n{'='*50}")
    print(f"  🎯 Kết quả:     {CLASS_NAMES[pred_class]} ({CLASS_NAMES_VI[pred_class]})")
    print(f"  📊 Độ tin cậy:  {confidence * 100:.1f}%")
    print(f"{'='*50}")

    # Top 3
    top3_indices = np.argsort(probs)[::-1][:3]
    print("\n  📋 Top 3 dự đoán:")
    for rank, idx in enumerate(top3_indices, 1):
        print(f"     {rank}. {CLASS_NAMES[idx]:15s} ({CLASS_NAMES_VI[idx]:15s}) — {probs[idx] * 100:.1f}%")

    # Lưu ảnh kết quả
    img_name = os.path.splitext(os.path.basename(image_path))[0]
    save_path = os.path.join(OUTPUT_DIR, f'result_{img_name}.png')
    create_result_image_external(original_img, processed_img, pred_class, confidence, probs, save_path)


def validate_from_dataset(model, index=None, count=1):
    """Kiểm tra từ tập test dataset"""
    # Tải dataset gốc (không normalize) để hiển thị
    raw_transform = transforms.ToTensor()
    test_dataset = datasets.FashionMNIST(
        root=DATA_DIR, train=False, download=False, transform=raw_transform
    )

    # Transform cho model
    model_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    test_dataset_norm = datasets.FashionMNIST(
        root=DATA_DIR, train=False, download=False, transform=model_transform
    )

    total = len(test_dataset)

    if index is not None:
        # Chế độ chọn index cụ thể
        if index < 0 or index >= total:
            print(f"❌ Index phải trong khoảng [0, {total - 1}]")
            sys.exit(1)
        indices = [index]
        print(f"\n📌 Kiểm tra ảnh index={index} từ tập test")
    else:
        # Chế độ random
        indices = np.random.choice(total, count, replace=False).tolist()
        print(f"\n🎲 Random {count} ảnh từ tập test (tổng {total} ảnh)")

    images = []
    true_labels = []
    pred_classes = []
    confidences = []
    all_probs = []

    for idx in indices:
        raw_img, true_label = test_dataset[idx]
        norm_img, _ = test_dataset_norm[idx]

        tensor = norm_img.unsqueeze(0)  # [1, 1, 28, 28]
        pred_class, confidence, probs = predict(model, tensor)

        images.append(raw_img.squeeze().numpy())
        true_labels.append(true_label)
        pred_classes.append(pred_class)
        confidences.append(confidence)
        all_probs.append(probs)

        is_correct = pred_class == true_label
        icon = '✅' if is_correct else '❌'
        print(f"  {icon} [{idx:5d}] Thật: {CLASS_NAMES[true_label]:15s} → "
              f"Đoán: {CLASS_NAMES[pred_class]:15s} ({confidence * 100:.1f}%)")

    # Thống kê
    correct = sum(1 for t, p in zip(true_labels, pred_classes) if t == p)
    print(f"\n  📊 Kết quả: {correct}/{len(indices)} đúng ({correct / len(indices) * 100:.1f}%)")

    # Lưu ảnh kết quả
    if len(indices) == 1:
        save_name = f'result_index_{indices[0]}.png'
    else:
        save_name = f'result_random_{count}.png'

    save_path = os.path.join(OUTPUT_DIR, save_name)
    create_result_image_dataset(images, true_labels, pred_classes, confidences, all_probs, save_path, len(indices))


# ========================
# MAIN
# ========================

def main():
    parser = argparse.ArgumentParser(
        description='Fashion-MNIST Validation - Kiểm tra mô hình nhận diện quần áo',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ sử dụng:
  python Validation/validate.py                          → Random 1 ảnh từ test set
  python Validation/validate.py --random 9               → Random 9 ảnh từ test set
  python Validation/validate.py --index 42               → Lấy ảnh index 42 từ test set
  python Validation/validate.py --image anh_ao.png       → Nhận diện ảnh bên ngoài
  python Validation/validate.py --image Validation/input → Nhận diện tất cả ảnh trong folder
        """
    )

    parser.add_argument('--image', '-i', type=str,
                        help='Đường dẫn tới ảnh hoặc folder ảnh bên ngoài')
    parser.add_argument('--index', '-idx', type=int, default=None,
                        help='Index của ảnh trong tập test (0-9999)')
    parser.add_argument('--random', '-r', type=int, default=1,
                        help='Số lượng ảnh random từ tập test (mặc định: 1)')

    args = parser.parse_args()

    print("=" * 60)
    print("  🔍 FASHION-MNIST VALIDATION TOOL")
    print("=" * 60)

    model = load_model()

    if args.image:
        path = args.image
        if os.path.isdir(path):
            # Nhận diện tất cả ảnh trong folder
            extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp')
            image_files = [f for f in os.listdir(path) if f.lower().endswith(extensions)]
            if not image_files:
                print(f"❌ Không tìm thấy ảnh trong folder: {path}")
                sys.exit(1)
            print(f"\n📂 Tìm thấy {len(image_files)} ảnh trong {path}")
            for img_file in sorted(image_files):
                validate_external_image(model, os.path.join(path, img_file))
        else:
            validate_external_image(model, path)
    elif args.index is not None:
        validate_from_dataset(model, index=args.index)
    else:
        validate_from_dataset(model, count=args.random)

    print(f"\n{'='*60}")
    print(f"  📂 Kết quả lưu tại: {OUTPUT_DIR}")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
