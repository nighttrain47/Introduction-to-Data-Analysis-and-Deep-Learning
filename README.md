# 📊 Nhập Môn Phân Tích Dữ Liệu Và Học Sâu

## 👤 Thông Tin Sinh Viên

| Thông tin | Chi tiết |
|-----------|----------|
| **Họ và tên** | **Kiều Thiện Bảo** |
| **Mã số sinh viên** | **2374802010034** |
| **Môn học** | Nhập Môn Phân Tích Dữ Liệu Và Học Sâu |

---

## 📁 Cấu Trúc Thư Mục

```
📦 Root
├── 📂 Lab1/                    → Thao tác dữ liệu cơ bản với Pandas
├── 📂 Lab2/                    → Trực quan hóa & thống kê mô tả
├── 📂 Lab3/                    → Tiền xử lý & làm sạch dữ liệu
├── 📂 Lab4/                    → Xử lý dữ liệu Titanic
├── 📂 Lab5/                    → (Chưa có nội dung)
├── 📂 Lab6_TrainModel/         → Huấn luyện mô hình Deep Learning (Fashion-MNIST)
├── 📂 Lab7/                    → Phân tích văn bản với NLTK
├── 📂 DuLieu/                  → Dữ liệu dùng chung cho các bài tập
├── 📂 Slide_BaiGiang_PhantichDuLieu_HocSau/  → Slide bài giảng
└── 📄 BaiTapThucHanh_NhapMon_PhanTichDuLieu_HocSau.pdf → Đề bài tập
```

---

## 🔬 Tổng Quan Các Bài Tập

### 📘 Lab 1: Thao Tác Dữ Liệu Cơ Bản Với Pandas

**Dữ liệu:** `dulieuxettuyendaihoc.csv` — Bộ dữ liệu xét tuyển đại học gồm thông tin cá nhân (giới tính, dân tộc, khu vực, khối thi) và điểm số các môn học từ lớp 10 đến lớp 12 cùng điểm thi đại học.

**Thư viện sử dụng:** `pandas`

| Câu | Tên bài | Mô tả |
|:---:|---------|-------|
| 1 | Phân loại dữ liệu | Xác định và phân loại các biến thành dữ liệu **định tính** (Nominal: GT, DT, KV, KT) và **định lượng** (Ratio: các biến điểm số). |
| 2 | Thang đo | Định nghĩa thang đo phù hợp cho từng biến: **Danh nghĩa** (Nominal) cho các biến phân loại, **Khoảng** (Interval) cho các biến điểm số. |
| 3 | Tải dữ liệu | Đọc file CSV bằng `pd.read_csv()` và hiển thị 10 dòng đầu/cuối để khảo sát dữ liệu. |
| 4 | Xử lý thiếu DT | Xử lý dữ liệu thiếu cho cột **Dân tộc (DT)** bằng cách điền giá trị `0` cho các giá trị NaN. |
| 5 | Xử lý thiếu T1 | Thống kê bảng tần số biến T1 và thay thế dữ liệu thiếu bằng **giá trị trung bình (Mean)**. |
| 6 | Xử lý thiếu toàn bộ | Mở rộng xử lý missing values cho **tất cả các biến điểm số** bằng phương pháp Mean. |
| 7 | Tạo TBM | Tạo biến điểm **trung bình môn (TBM1, TBM2, TBM3)** cho 3 năm học theo công thức có trọng số: `TBM = (T×2 + L + H + S + V×2 + X + D + N) / 10`. |
| 8 | Xếp loại | Tạo biến **xếp loại (XL1, XL2, XL3)** dựa trên TBM: Yếu (< 5.0), Trung bình (5.0–6.5), Khá (6.5–8.0), Giỏi (8.0–9.0), Xuất sắc (≥ 9.0). |
| 9 | Chuẩn hóa Min-Max | Chuyển đổi điểm từ **thang 10 VN sang thang 4 Mỹ** bằng Min-Max Normalization, tạo US_TBM1, US_TBM2, US_TBM3. |
| 10 | Kết quả xét tuyển | Tạo biến **KQXT** (Kết quả xét tuyển) dựa trên điểm thi ĐH theo từng khối thi (A, A1, B, C, D1) với công thức khác nhau. |
| 11 | Lưu file | Tổng hợp toàn bộ pipeline xử lý (câu 4–10) và **xuất file** `processed_dulieuxettuyendaihoc.csv`. |

---

### 📗 Lab 2: Trực Quan Hóa & Thống Kê Mô Tả

**Dữ liệu:** `processed_dulieuxettuyendaihoc.csv` — Dữ liệu đã qua xử lý ở Lab 1.

**Thư viện sử dụng:** `pandas`, `numpy`, `matplotlib`, `scipy`

Lab 2 được chia thành **5 phần lớn** với tổng cộng **27 bài tập**:

#### Phần 1: Sắp xếp dữ liệu (5 câu)
Sắp xếp dữ liệu điểm các môn theo thứ tự tăng dần/giảm dần, giúp khảo sát phân bố và xác định vùng giá trị.

#### Phần 2: Bảng tần số & Biểu đồ cơ bản (5 câu)
Lập **bảng tần số, tần suất** cho các biến định tính (GT, KV, KT, XL) và vẽ:
- **Biểu đồ cột** (bar chart) thể hiện tần số
- **Biểu đồ tròn** (pie chart) thể hiện tần suất

#### Phần 3: Biểu đồ nâng cao — Unstacked & Stacked (7 câu)
Trực quan hóa dữ liệu đa chiều với:
- **Biểu đồ cột nhóm (Unstacked/Grouped bar chart):** So sánh phân bố xếp loại theo giới tính, khu vực.
- **Biểu đồ cột chồng (Stacked bar chart):** Hiển thị tổng thể và tỷ lệ phân bố bên trong.
- Lọc dữ liệu theo điều kiện (học sinh nữ, nam, theo khu vực) trước khi vẽ.

#### Phần 4: Biểu đồ đường (5 câu)
Vẽ **biểu đồ đường (Line chart)** — dạng Simple, Multiple và Compound — để theo dõi xu hướng phân bố tần số của các biến điểm số (T1, L1, H1,...).

#### Phần 5: Thống kê mô tả & Khảo sát phân phối (5 câu)
Phân tích sâu cho từng biến điểm số, bao gồm:
- **Thống kê mô tả:** Mean, Median, Mode, Variance, Std, Q1/Q2/Q3, IQR
- **Box-Plot:** Xác định outliers, phân vị, khoảng trải giữa
- **Histogram + Density curve:** Hình dáng phân phối
- **QQ-Plot:** Kiểm chứng phân phối chuẩn
- **Kiểm định thống kê:** Shapiro-Wilk, Kolmogorov-Smirnov
- **Nhận xét:** Skewness (độ lệch), Kurtosis (độ nhọn), kết luận phân phối

---

### 📙 Lab 3: Tiền Xử Lý & Làm Sạch Dữ Liệu

**Dữ liệu:** `patient_heart_rate.csv` — Dữ liệu nhịp tim bệnh nhân (dữ liệu "bẩn" cần làm sạch).

**Thư viện sử dụng:** `pandas`, `re` (regex)

Lab 3 xử lý **12 vấn đề thực tế** trong Data Cleaning:

| Vấn đề | Tên bài | Mô tả |
|:------:|---------|-------|
| 1 | Thêm header | File CSV không có dòng tiêu đề → Gán header thủ công cho DataFrame. |
| 2 | Tách tên | Tách cột Name thành **First Name** và **Last Name**. |
| 3 | Chuẩn hóa Weight | Xử lý lẫn lộn đơn vị **kgs** và **lbs** → Chuyển tất cả về **kg** (1 lbs = 0.453592 kg). |
| 4 | Xóa dòng rỗng | Phát hiện và loại bỏ các **dòng hoàn toàn rỗng** (NaN toàn bộ cột). |
| 5 | Xóa trùng lặp | Phát hiện và loại bỏ các **bản ghi trùng lặp** (duplicate rows). |
| 6 | Xử lý Non-ASCII | Phát hiện và xử lý **ký tự đặc biệt Non-ASCII** trong dữ liệu. |
| 7 | Missing Age & Weight | Xử lý missing values cho Age và Weight: điền Mean nếu thiếu một cột, xóa nếu thiếu cả hai. |
| 8 | Phân ra cột | Tách một cột chứa nhiều thông tin thành **nhiều cột riêng biệt**. |
| 11 | Missing Pulse Rate | Xử lý dữ liệu thiếu cho các cột **nhịp tim** (m0006, m0612, m1218,...). |
| 12 | Lưu file | Lưu dữ liệu đã làm sạch hoàn chỉnh ra file `patient_heart_rate_clean.csv`. |

---

### 📕 Lab 4: Xử Lý Dữ Liệu Titanic

**Dữ liệu:** `titanic_disaster.csv` — Bộ dữ liệu thảm họa Titanic nổi tiếng (891 hành khách, 12 biến).

**Thư viện sử dụng:** `pandas`, `numpy`, `matplotlib`, `seaborn`

Lab 4 thực hiện **pipeline xử lý và Feature Engineering** hoàn chỉnh trên dữ liệu Titanic:

| Bài | Tên bài | Mô tả |
|:---:|---------|-------|
| 1 | Load data | Viết hàm `load_data()` để tải và hiển thị 10 dòng đầu tiên. |
| 2 | Missing data | Thống kê dữ liệu thiếu và trực quan hóa bằng **Heat map**. Nhận xét về Age (19.87% thiếu), Cabin (77.10% thiếu), Embarked (0.22% thiếu). |
| 3 | Split Name | Tách cột **Name** thành **firstName** và **secondName** (dựa trên dấu phẩy). |
| 4 | Shorten Sex | Rút gọn cột **Sex**: `male → M`, `female → F`. |
| 5 | Handle Missing Age | Vẽ **Box-Plot** phân phối tuổi theo hạng vé (Pclass), thay thế Age thiếu bằng **trung bình theo nhóm Pclass**. |
| 6 | Age Group | Tạo biến **Agegroup** theo thang đo thứ tự: Kid (≤12), Teen (12–18), Adult (18–60), Older (>60). |
| 7 | Name Prefix | Trích xuất **danh xưng** (Mr, Mrs, Miss, Master,...) từ secondName. |
| 8 | Family Size | Tạo biến **familySize** = 1 + SibSp + Parch (số thành viên gia đình đi cùng). |
| 9 | Alone | Tạo biến **Alone**: `1` nếu familySize = 1 (đi một mình), `0` nếu đi theo nhóm. Trực quan hóa bằng Pie chart & so sánh tỷ lệ sống sót. |
| 10 | Type Cabin | Trích xuất **loại cabin (typeCabin)** từ ký tự đầu tiên cột Cabin, gán `"Unknown"` cho giá trị thiếu. |
| 11 | Remove Duplicate | Kiểm tra và loại bỏ **dữ liệu trùng lặp** giữa tập Train và Test bằng cách so sánh đa cột (Name, Sex, Ticket, Fare). |

> 💡 **Đặc điểm nổi bật:** Các bài trong Lab 4 được thiết kế theo **pipeline tuần tự** — mỗi bài đọc kết quả từ bài trước, tạo thành quy trình xử lý dữ liệu liên tục và chuyên nghiệp.

---

### 📓 Lab 6: Huấn Luyện Mô Hình Deep Learning — Fashion-MNIST

**Dữ liệu:** Fashion-MNIST (60,000 ảnh train + 10,000 ảnh test, 28×28 pixel, 10 lớp quần áo).

**Thư viện sử dụng:** `PyTorch`, `torchvision`, `matplotlib`, `seaborn`, `sklearn`

#### Mô hình: Deep Neural Network (DNN)

```
Kiến trúc:
  Input (784) → FC(512) → BatchNorm → ReLU → Dropout(0.3)
              → FC(256) → BatchNorm → ReLU → Dropout(0.3)
              → FC(128) → BatchNorm → ReLU → Dropout(0.2)
              → FC(10)  → Output (10 classes)
```

#### Nội dung thực hiện:

| Giai đoạn | Mô tả |
|-----------|-------|
| **1. Chuẩn bị dữ liệu** | Tải Fashion-MNIST, chia train/validation (90/10), normalize về [-1, 1], tạo DataLoader. |
| **2. Phân tích dữ liệu** | Hiển thị mẫu ảnh từ mỗi lớp, phân bố số lượng mẫu, thống kê pixel (mean/std) theo lớp. |
| **3. Xây dựng mô hình** | DNN 3 hidden layers (512→256→128) với BatchNorm + Dropout để chống overfitting. |
| **4. Huấn luyện** | 20 epochs, Adam optimizer (lr=0.001), CrossEntropyLoss, ReduceLROnPlateau scheduler. Lưu model tốt nhất. |
| **5. Đánh giá** | Classification Report, Confusion Matrix, đồ thị Loss/Accuracy theo epoch. |
| **6. Dự đoán mẫu** | Hiển thị 15 ảnh random từ tập test với nhãn thực vs dự đoán. |

#### Validation Tool

Script `Validation/validate.py` cho phép:
- 🎲 Random ảnh từ tập test để kiểm tra
- 📌 Chọn ảnh theo index cụ thể
- 🖼️ Nhập ảnh bên ngoài để mô hình nhận diện (tự động resize, đảo nền, normalize)

#### Kết quả đầu ra:

```
📂 Graph/
├── sample_images.png        → Mẫu ảnh từ mỗi lớp
├── class_distribution.png   → Phân phối dữ liệu
├── pixel_statistics.png     → Thống kê pixel
├── loss_curve.png           → Đồ thị Loss
├── accuracy_curve.png       → Đồ thị Accuracy
├── confusion_matrix.png     → Ma trận nhầm lẫn
└── prediction_samples.png   → Kết quả dự đoán mẫu

📂 Model/
└── fashion_mnist_model.pth  → Mô hình đã huấn luyện
```

---

### 📒 Lab 7: Phân Tích Dữ Liệu Văn Bản Với NLTK

**Thư viện sử dụng:** `NLTK` (Natural Language Toolkit)

Lab 7 thực hiện **13 bài tập** xoay quanh các kỹ thuật NLP cơ bản:

#### Nhóm 1: Khám Phá Corpus (Bài 1)

| Bài | Mô tả |
|:---:|-------|
| 1 | Liệt kê tất cả corpus trong **Gutenberg** (kho ngữ liệu văn học cổ điển tiếng Anh). |

#### Nhóm 2: Stopwords (Bài 2–5)

| Bài | Mô tả |
|:---:|-------|
| 2 | Liệt kê danh sách **stopwords** theo nhiều ngôn ngữ khác nhau (English, French, German,...). |
| 3 | Kiểm tra chi tiết stopwords: hiển thị 10 stopword đầu tiên và số lượng cho mỗi ngôn ngữ. |
| 4 | **Loại bỏ stopwords** từ một văn bản mẫu bằng tokenization + filtering. |
| 5 | **Tùy chỉnh bộ stopwords:** Giữ lại các từ phủ định (not, no, nor, never,...) để bảo toàn ngữ nghĩa khi lọc. |

#### Nhóm 3: WordNet — Từ điển ngữ nghĩa (Bài 6–10)

| Bài | Mô tả |
|:---:|-------|
| 6 | Tìm **định nghĩa (definition)** và **ví dụ (examples)** của một từ thông qua WordNet Synsets. |
| 7 | Tìm tập hợp **từ đồng nghĩa (synonyms)** và **trái nghĩa (antonyms)** cho các từ: good, happy, fast. |
| 8 | Tổng quan về **bộ POS tag** (Part-of-Speech), chi tiết từng tag, sử dụng **biểu thức chính quy** để lọc tag theo nhóm (Noun, Verb, Adjective). |
| 9 | **So sánh ngữ nghĩa danh từ:** Tính Wu-Palmer Similarity và Path Similarity cho các cặp danh từ (dog–cat, car–bicycle, book–library). |
| 10 | **So sánh ngữ nghĩa động từ:** Tính độ tương đồng cho các cặp động từ (run–walk, eat–drink, write–read). |

#### Nhóm 4: Phân tích tên riêng — Names Corpus (Bài 11–13)

| Bài | Mô tả |
|:---:|-------|
| 11 | Thống kê **số lượng tên nam và nữ** trong kho ngữ liệu Names (male.txt, female.txt). |
| 12 | In **15 kết hợp ngẫu nhiên** tên nam và nữ với nhãn giới tính. |
| 13 | Trích xuất **ký tự cuối cùng** của mỗi tên, thống kê phân bổ theo giới tính, tìm top 5 chữ cái cuối phổ biến nhất ở tên nam và nữ. |

---

## 🗂️ Dữ Liệu Sử Dụng

| File | Mô tả | Lab |
|------|-------|:---:|
| `dulieuxettuyendaihoc.csv` | Dữ liệu xét tuyển đại học (điểm học lực + điểm thi ĐH) | 1, 2 |
| `processed_dulieuxettuyendaihoc.csv` | Dữ liệu đã qua xử lý (thêm TBM, XL, US_TBM, KQXT) | 2 |
| `patient_heart_rate.csv` | Dữ liệu nhịp tim bệnh nhân (dữ liệu bẩn) | 3 |
| `titanic_disaster.csv` | Dữ liệu thảm họa Titanic | 4 |
| `Fashion-MNIST` | Bộ ảnh quần áo 28×28 pixel (60k+10k) | 6 |
| NLTK Corpora | Gutenberg, Stopwords, WordNet, Names | 7 |

---

## 🛠️ Công Nghệ & Thư Viện

| Thư viện | Mục đích | Lab |
|----------|----------|:---:|
| `pandas` | Xử lý, biến đổi dữ liệu dạng bảng | 1, 2, 3, 4 |
| `numpy` | Tính toán số học, mảng đa chiều | 2, 6 |
| `matplotlib` | Trực quan hóa dữ liệu (biểu đồ tĩnh) | 2, 4, 6 |
| `seaborn` | Trực quan hóa thống kê nâng cao | 4, 6 |
| `scipy` | Kiểm định thống kê (Shapiro-Wilk, KS-test) | 2 |
| `PyTorch` | Xây dựng và huấn luyện mô hình Deep Learning | 6 |
| `torchvision` | Tải và xử lý dữ liệu ảnh (Fashion-MNIST) | 6 |
| `scikit-learn` | Classification Report, Confusion Matrix | 6 |
| `NLTK` | Xử lý ngôn ngữ tự nhiên (NLP) | 7 |
| `Pillow (PIL)` | Xử lý ảnh đầu vào cho validation | 6 |

---

## 🚀 Hướng Dẫn Chạy

### Yêu cầu
- Python 3.8+
- Cài đặt thư viện:

```bash
pip install pandas numpy matplotlib seaborn scipy torch torchvision scikit-learn nltk Pillow
```

### Chạy từng Lab

```bash
# Lab 1
cd Lab1/BT
python cau1_phan_loai_du_lieu.py
python cau11_luu_file.py        # Chạy toàn bộ pipeline

# Lab 2
cd Lab2
python Phan1_Cau1.py            # Chạy từng file riêng lẻ

# Lab 3
cd Lab3
python vande1_them_header.py    # Chạy từng vấn đề

# Lab 4
cd Lab4/Code
python Bai1_LoadData.py         # Chạy tuần tự từ Bai1 → Bai11

# Lab 6
cd Lab6_TrainModel
python Model/fashion_mnist_dnn.py       # Huấn luyện mô hình
python Validation/validate.py           # Kiểm tra mô hình
python Validation/validate.py --random 9  # Random 9 ảnh test

# Lab 7
cd Lab7
python bai1.py                  # Chạy từng bài riêng lẻ
```

---

## 📚 Tài Liệu Tham Khảo

Các slide bài giảng trong thư mục `Slide_BaiGiang_PhantichDuLieu_HocSau/`:

| Slide | Nội dung |
|-------|----------|
| `Phan1_Pandas_Numpy_Matplotlib.pdf` | Pandas, NumPy, Matplotlib cơ bản |
| `TrucQuanHoaDuLieu_Histogram.pdf` | Trực quan hóa: Histogram |
| `CacDoDo_DoThiBoxPlot.pdf` | Các đại lượng thống kê & Box-Plot |
| `HoiQuy.pdf` | Phân tích hồi quy |
| `KiemDinhPTHoiQuy_docthem.pdf` | Kiểm định phương trình hồi quy |
| `PhanTichAnh_OPenCV.pdf` | Phân tích ảnh với OpenCV |
| `PhanTichDuLieuVanBan_NLTK.pdf` | Phân tích văn bản với NLTK |
| `NeuralNetwork.pdf` | Mạng nơ-ron nhân tạo |
| `Tensorflow.pdf` | TensorFlow / Deep Learning |

---

> **Ghi chú:** Repository này chứa toàn bộ bài tập thực hành của sinh viên **Kiều Thiện Bảo** (MSSV: **2374802010034**) cho môn học *Nhập Môn Phân Tích Dữ Liệu Và Học Sâu*. Mỗi lab được tổ chức trong thư mục riêng, mỗi bài tập là một file Python độc lập có thể chạy riêng lẻ.
