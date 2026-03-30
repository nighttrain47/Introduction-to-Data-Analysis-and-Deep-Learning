# ==============================================================
# Fashion-MNIST Deep Neural Network - Nhận dạng quần áo thời trang
# ==============================================================
# Sử dụng PyTorch xây dựng mạng nơ-ron sâu (DNN) để phân loại
# 10 loại quần áo, giày dép từ bộ dữ liệu Fashion-MNIST
# ==============================================================

import os
import sys
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for saving plots
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

# ========================
# 1. CÀI ĐẶT CHUNG
# ========================

# Đường dẫn
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'Data')
GRAPH_DIR = os.path.join(BASE_DIR, 'Graph')
MODEL_DIR = os.path.join(BASE_DIR, 'Model')

os.makedirs(GRAPH_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

# Thiết lập seed cho reproducibility
SEED = 42
torch.manual_seed(SEED)
np.random.seed(SEED)

# Thiết bị huấn luyện
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"🖥️  Thiết bị sử dụng: {DEVICE}")

# Tên các class trong Fashion-MNIST
CLASS_NAMES = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]

# Hyperparameters
BATCH_SIZE = 128
EPOCHS = 20
LEARNING_RATE = 0.001
VAL_SPLIT = 0.1  # 10% cho validation

# ========================
# 2. TẢI VÀ CHUẨN BỊ DỮ LIỆU
# ========================

print("\n📦 Đang tải dữ liệu Fashion-MNIST...")

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))  # Normalize về [-1, 1]
])

# Tải dataset
full_train_dataset = datasets.FashionMNIST(
    root=DATA_DIR, train=True, download=False, transform=transform
)
test_dataset = datasets.FashionMNIST(
    root=DATA_DIR, train=False, download=False, transform=transform
)

# Chia train/validation
val_size = int(VAL_SPLIT * len(full_train_dataset))
train_size = len(full_train_dataset) - val_size
train_dataset, val_dataset = random_split(
    full_train_dataset, [train_size, val_size],
    generator=torch.Generator().manual_seed(SEED)
)

# DataLoader
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, num_workers=0)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=0)
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False, num_workers=0)

print(f"✅ Tập huấn luyện: {train_size} mẫu")
print(f"✅ Tập validation: {val_size} mẫu")
print(f"✅ Tập kiểm tra:   {len(test_dataset)} mẫu")

# ===================================
# 3. PHÂN TÍCH VÀ TRỰC QUAN HÓA DỮ LIỆU
# ===================================

print("\n📊 Đang tạo đồ thị phân tích dữ liệu...")

# --- Tải dữ liệu gốc (không normalize) để vẽ ---
raw_transform = transforms.ToTensor()
raw_dataset = datasets.FashionMNIST(
    root=DATA_DIR, train=True, download=False, transform=raw_transform
)

# --- 3.1: Hiển thị mẫu ảnh từ mỗi class ---
fig, axes = plt.subplots(2, 5, figsize=(14, 6))
fig.suptitle('Mẫu ảnh từ mỗi lớp trong Fashion-MNIST', fontsize=16, fontweight='bold')

for class_idx in range(10):
    # Tìm ảnh đầu tiên thuộc class này
    for img, label in raw_dataset:
        if label == class_idx:
            row, col = class_idx // 5, class_idx % 5
            axes[row, col].imshow(img.squeeze(), cmap='gray')
            axes[row, col].set_title(CLASS_NAMES[class_idx], fontsize=11, fontweight='bold')
            axes[row, col].axis('off')
            break

plt.tight_layout()
plt.savefig(os.path.join(GRAPH_DIR, 'sample_images.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  ✅ Đã lưu: Graph/sample_images.png")

# --- 3.2: Phân phối số lượng mẫu theo class ---
all_labels = [label for _, label in raw_dataset]
label_counts = np.bincount(all_labels)

fig, ax = plt.subplots(figsize=(12, 6))
colors = sns.color_palette('viridis', 10)
bars = ax.bar(CLASS_NAMES, label_counts, color=colors, edgecolor='white', linewidth=0.8)
ax.set_title('Phân phối số lượng mẫu theo lớp (Tập huấn luyện)', fontsize=14, fontweight='bold')
ax.set_xlabel('Lớp', fontsize=12)
ax.set_ylabel('Số lượng mẫu', fontsize=12)
ax.set_ylim(0, max(label_counts) * 1.15)

# Thêm số liệu lên mỗi cột
for bar, count in zip(bars, label_counts):
    ax.text(bar.get_x() + bar.get_width() / 2., bar.get_height() + 100,
            f'{count}', ha='center', va='bottom', fontweight='bold', fontsize=10)

plt.xticks(rotation=35, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(GRAPH_DIR, 'class_distribution.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  ✅ Đã lưu: Graph/class_distribution.png")

# --- 3.3: Thống kê pixel ---
# Tính mean/std pixel cho từng class
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

class_means = []
class_stds = []
for class_idx in range(10):
    class_images = []
    for img, label in raw_dataset:
        if label == class_idx:
            class_images.append(img.numpy())
            if len(class_images) >= 200:  # Lấy 200 mẫu để tính nhanh
                break
    class_images = np.array(class_images)
    class_means.append(class_images.mean())
    class_stds.append(class_images.std())

# Mean pixel
axes[0].barh(CLASS_NAMES, class_means, color=sns.color_palette('coolwarm', 10), edgecolor='white')
axes[0].set_title('Giá trị pixel trung bình theo lớp', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Mean Pixel Value', fontsize=11)

# Std pixel
axes[1].barh(CLASS_NAMES, class_stds, color=sns.color_palette('magma', 10), edgecolor='white')
axes[1].set_title('Độ lệch chuẩn pixel theo lớp', fontsize=13, fontweight='bold')
axes[1].set_xlabel('Std Pixel Value', fontsize=11)

plt.tight_layout()
plt.savefig(os.path.join(GRAPH_DIR, 'pixel_statistics.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  ✅ Đã lưu: Graph/pixel_statistics.png")

# ========================
# 4. XÂY DỰNG MÔ HÌNH DNN
# ========================

print("\n🧠 Xây dựng mô hình Deep Neural Network...")


class FashionDNN(nn.Module):
    """
    Mạng nơ-ron sâu cho bài toán Fashion-MNIST

    Kiến trúc:
        Input (784) → FC(512) → BN → ReLU → Dropout(0.3)
                     → FC(256) → BN → ReLU → Dropout(0.3)
                     → FC(128) → BN → ReLU → Dropout(0.2)
                     → FC(10)   → Output
    """

    def __init__(self):
        super(FashionDNN, self).__init__()

        self.network = nn.Sequential(
            # Flatten
            nn.Flatten(),

            # Hidden Layer 1: 784 → 512
            nn.Linear(28 * 28, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(0.3),

            # Hidden Layer 2: 512 → 256
            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.3),

            # Hidden Layer 3: 256 → 128
            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(0.2),

            # Output Layer: 128 → 10
            nn.Linear(128, 10)
        )

    def forward(self, x):
        return self.network(x)


model = FashionDNN().to(DEVICE)

# In kiến trúc mô hình
print(f"\n{'='*50}")
print("KIẾN TRÚC MÔ HÌNH")
print(f"{'='*50}")
print(model)
total_params = sum(p.numel() for p in model.parameters())
trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f"\n📐 Tổng số tham số: {total_params:,}")
print(f"📐 Tham số huấn luyện: {trainable_params:,}")

# Loss function và Optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=3)

# ========================
# 5. HUẤN LUYỆN MÔ HÌNH
# ========================

print(f"\n🚀 Bắt đầu huấn luyện ({EPOCHS} epochs)...")
print(f"{'='*70}")

train_losses = []
val_losses = []
train_accs = []
val_accs = []
best_val_acc = 0.0


def train_one_epoch(model, loader, criterion, optimizer, device):
    """Huấn luyện 1 epoch"""
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * images.size(0)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    avg_loss = running_loss / total
    accuracy = 100.0 * correct / total
    return avg_loss, accuracy


def evaluate(model, loader, criterion, device):
    """Đánh giá trên tập validation/test"""
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)

            running_loss += loss.item() * images.size(0)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    avg_loss = running_loss / total
    accuracy = 100.0 * correct / total
    return avg_loss, accuracy


# Training loop
for epoch in range(1, EPOCHS + 1):
    train_loss, train_acc = train_one_epoch(model, train_loader, criterion, optimizer, DEVICE)
    val_loss, val_acc = evaluate(model, val_loader, criterion, DEVICE)

    train_losses.append(train_loss)
    val_losses.append(val_loss)
    train_accs.append(train_acc)
    val_accs.append(val_acc)

    # Learning rate scheduling
    scheduler.step(val_loss)

    # Lưu model tốt nhất
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        torch.save(model.state_dict(), os.path.join(MODEL_DIR, 'fashion_mnist_model.pth'))

    print(f"  Epoch [{epoch:2d}/{EPOCHS}] │ "
          f"Train Loss: {train_loss:.4f} │ Train Acc: {train_acc:.2f}% │ "
          f"Val Loss: {val_loss:.4f} │ Val Acc: {val_acc:.2f}%"
          f"{' ⭐' if val_acc >= best_val_acc else ''}")

print(f"\n✅ Best Validation Accuracy: {best_val_acc:.2f}%")
print(f"✅ Model đã lưu: Model/fashion_mnist_model.pth")

# ========================
# 6. VẼ ĐỒ THỊ HUẤN LUYỆN
# ========================

print("\n📈 Đang tạo đồ thị huấn luyện...")

epochs_range = range(1, EPOCHS + 1)

# --- 6.1: Loss Curve ---
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(epochs_range, train_losses, 'b-o', linewidth=2, markersize=5, label='Train Loss', alpha=0.8)
ax.plot(epochs_range, val_losses, 'r-s', linewidth=2, markersize=5, label='Validation Loss', alpha=0.8)
ax.fill_between(epochs_range, train_losses, alpha=0.1, color='blue')
ax.fill_between(epochs_range, val_losses, alpha=0.1, color='red')
ax.set_title('Đồ thị Loss qua các Epoch', fontsize=14, fontweight='bold')
ax.set_xlabel('Epoch', fontsize=12)
ax.set_ylabel('Loss', fontsize=12)
ax.legend(fontsize=11, loc='upper right')
ax.grid(True, alpha=0.3)
ax.set_xticks(range(1, EPOCHS + 1))
plt.tight_layout()
plt.savefig(os.path.join(GRAPH_DIR, 'loss_curve.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  ✅ Đã lưu: Graph/loss_curve.png")

# --- 6.2: Accuracy Curve ---
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(epochs_range, train_accs, 'g-o', linewidth=2, markersize=5, label='Train Accuracy', alpha=0.8)
ax.plot(epochs_range, val_accs, 'm-s', linewidth=2, markersize=5, label='Validation Accuracy', alpha=0.8)
ax.fill_between(epochs_range, train_accs, alpha=0.1, color='green')
ax.fill_between(epochs_range, val_accs, alpha=0.1, color='magenta')
ax.set_title('Đồ thị Accuracy qua các Epoch', fontsize=14, fontweight='bold')
ax.set_xlabel('Epoch', fontsize=12)
ax.set_ylabel('Accuracy (%)', fontsize=12)
ax.legend(fontsize=11, loc='lower right')
ax.grid(True, alpha=0.3)
ax.set_xticks(range(1, EPOCHS + 1))
plt.tight_layout()
plt.savefig(os.path.join(GRAPH_DIR, 'accuracy_curve.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  ✅ Đã lưu: Graph/accuracy_curve.png")

# ========================
# 7. ĐÁNH GIÁ TRÊN TẬP TEST
# ========================

print("\n🧪 Đánh giá mô hình trên tập test...")

# Load model tốt nhất
model.load_state_dict(torch.load(os.path.join(MODEL_DIR, 'fashion_mnist_model.pth'), weights_only=True))
model.eval()

test_loss, test_acc = evaluate(model, test_loader, criterion, DEVICE)
print(f"\n📊 Test Loss: {test_loss:.4f}")
print(f"📊 Test Accuracy: {test_acc:.2f}%")

# Thu thập tất cả predictions
all_preds = []
all_labels = []

with torch.no_grad():
    for images, labels in test_loader:
        images = images.to(DEVICE)
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        all_preds.extend(predicted.cpu().numpy())
        all_labels.extend(labels.numpy())

all_preds = np.array(all_preds)
all_labels = np.array(all_labels)

# Classification Report
print(f"\n{'='*60}")
print("CLASSIFICATION REPORT")
print(f"{'='*60}")
print(classification_report(all_labels, all_preds, target_names=CLASS_NAMES))

# --- 7.1: Confusion Matrix ---
cm = confusion_matrix(all_labels, all_preds)

fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=CLASS_NAMES, yticklabels=CLASS_NAMES,
            linewidths=0.5, linecolor='gray',
            annot_kws={'size': 10})
ax.set_title('Ma trận nhầm lẫn (Confusion Matrix)', fontsize=14, fontweight='bold')
ax.set_xlabel('Nhãn dự đoán', fontsize=12)
ax.set_ylabel('Nhãn thực tế', fontsize=12)
plt.xticks(rotation=35, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(GRAPH_DIR, 'confusion_matrix.png'), dpi=150, bbox_inches='tight')
plt.close()
print("\n  ✅ Đã lưu: Graph/confusion_matrix.png")

# ========================
# 8. DỰ ĐOÁN MẪU
# ========================

print("\n🔍 Tạo đồ thị dự đoán mẫu...")

# Lấy một batch từ test
raw_test = datasets.FashionMNIST(
    root=DATA_DIR, train=False, download=False, transform=raw_transform
)

fig, axes = plt.subplots(3, 5, figsize=(16, 10))
fig.suptitle('Kết quả dự đoán trên tập test', fontsize=16, fontweight='bold')

# Random indices
np.random.seed(SEED)
indices = np.random.choice(len(test_dataset), 15, replace=False)

for i, idx in enumerate(indices):
    row, col = i // 5, i % 5
    ax = axes[row, col]

    # Ảnh gốc (không normalize)
    raw_img, true_label = raw_test[idx]
    ax.imshow(raw_img.squeeze(), cmap='gray')

    pred_label = all_preds[idx]
    is_correct = pred_label == true_label

    title_color = 'green' if is_correct else 'red'
    title = f"Thật: {CLASS_NAMES[true_label]}\nDự đoán: {CLASS_NAMES[pred_label]}"
    ax.set_title(title, fontsize=9, color=title_color, fontweight='bold')
    ax.axis('off')

    # Viền đỏ nếu sai
    if not is_correct:
        for spine in ax.spines.values():
            spine.set_edgecolor('red')
            spine.set_linewidth(3)
            spine.set_visible(True)

plt.tight_layout()
plt.savefig(os.path.join(GRAPH_DIR, 'prediction_samples.png'), dpi=150, bbox_inches='tight')
plt.close()
print("  ✅ Đã lưu: Graph/prediction_samples.png")

# ========================
# 9. TỔNG KẾT
# ========================

print(f"\n{'='*60}")
print("📋 TỔNG KẾT")
print(f"{'='*60}")
print(f"  🏗️  Mô hình: DNN 3 hidden layers (512→256→128)")
print(f"  📐 Tổng tham số: {total_params:,}")
print(f"  🎯 Test Accuracy: {test_acc:.2f}%")
print(f"  📉 Test Loss: {test_loss:.4f}")
print(f"\n  📊 Các đồ thị đã lưu trong folder Graph/:")
print(f"     1. sample_images.png      - Mẫu ảnh từ mỗi lớp")
print(f"     2. class_distribution.png - Phân phối dữ liệu")
print(f"     3. pixel_statistics.png   - Thống kê pixel")
print(f"     4. loss_curve.png         - Đồ thị Loss")
print(f"     5. accuracy_curve.png     - Đồ thị Accuracy")
print(f"     6. confusion_matrix.png   - Ma trận nhầm lẫn")
print(f"     7. prediction_samples.png - Kết quả dự đoán mẫu")
print(f"\n  💾 Model đã lưu: Model/fashion_mnist_model.pth")
print(f"{'='*60}")
