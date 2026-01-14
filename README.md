# 💻 TechMart - Nền tảng Thương mại Điện tử Đồ công nghệ Toàn diện

**TechMart** là một ứng dụng Web mua sắm thiết bị công nghệ hiện đại, được xây dựng trên nền tảng **Python Flask**. Dự án cung cấp một hệ thống thương mại điện tử hoàn chỉnh từ khâu duyệt sản phẩm, tương tác cộng đồng cho đến quy trình đặt hàng và quản trị viên (Admin Dashboard).

---

## 🌟 Tính năng nổi bật

### 1. Trải nghiệm người dùng (Customer Experience)
* **Trang chủ hiện đại:** Banner chuyên nghiệp, phân loại sản phẩm theo trạng thái "Sản phẩm mới" (New) và "Sản phẩm giảm giá" (Sale).
* **Duyệt & Tìm kiếm:** * Tìm kiếm sản phẩm nhanh theo từ khóa.
    * **Bộ lọc nâng cao:** Lọc theo danh mục (Laptop, Phone, Tablet...) và **khoảng giá (Price Range)** bằng thanh trượt trực quan.
* **Chi tiết sản phẩm:** * Tính toán phần trăm giảm giá tự động.
    * Hệ thống **Bình luận đa cấp** (cho phép trả lời bình luận).
    * Hệ thống **Emoji Reactions** (Thích, Tim, Wow, ✨...) tăng tính tương tác.
    * Đánh giá sao (Rating) cho từng sản phẩm.
* **Giỏ hàng & Thanh toán:** Cập nhật số lượng thời gian thực, tính tổng tiền và hỗ trợ nhiều phương thức thanh toán (COD, Chuyển khoản).

### 2. Quản lý Tài khoản (User Management)
* **Xác thực:** Đăng ký, Đăng nhập, Đổi mật khẩu và Quên mật khẩu.
* **Hồ sơ cá nhân:** Quản lý thông tin tài khoản và hệ thống **Sổ địa chỉ** linh hoạt (Thêm/Sửa/Xóa nhiều địa chỉ nhận hàng).
* **Lịch sử đơn hàng:** Theo dõi tiến độ đơn hàng qua 5 trạng thái với giao diện Timeline trực quan.

### 3. Hệ thống Quản trị (Admin Panel)
* **Bảng điều khiển 4 trong 1:** Quản lý Sản phẩm, Đơn hàng, Người dùng và Bình luận trong một giao diện duy nhất.
* **Xử lý đơn hàng:** Cập nhật trạng thái giao hàng hoặc hủy đơn kèm lý do chi tiết.
* **Quản lý kho:** Thêm mới sản phẩm với tính năng upload hình ảnh, thiết lập giá Sale/New.

---

## 🛠 Công nghệ sử dụng

* **Backend:** Python 3.x, Flask Framework.
* **Database:** SQLAlchemy ORM (Gồm 7 bảng liên kết: `User`, `Category`, `Product`, `Order`, `OrderItem`, `Comment`, `Reaction`, `Address`).
* **Bảo mật:** `Flask-Login` (Quản lý phiên), `Flask-Bcrypt` (Mã hóa mật khẩu), `Flask-WTF` (Bảo mật Form).
* **Frontend:** HTML5, CSS3 (Custom Design), JS Vanilla, Bootstrap 5, FontAwesome 6.

---

## 📂 Cấu trúc thư mục dự án

```text
LapTrinhWebCongNghe/
├── app/
│   ├── static/          # CSS custom, JS xử lý Emoji, Images sản phẩm
│   ├── templates/       # Hệ thống template Jinja2 (auth, admin, cart, main)
│   ├── models.py        # Định nghĩa Database Schema & OrderStatus Enum
│   ├── utils.py         # Hàm hỗ trợ: Định dạng tiền, % giảm giá, Seed data
│   └── __init__.py      # Khởi tạo Flask Application Factory
├── app.py               # Điểm khởi chạy chính (Main Entry)
└── requirements.txt     # Danh sách thư viện phụ thuộc
⚙️ Hướng dẫn cài đặt
Clone dự án:

Bash

git clone [https://github.com/NguyenVanHai16/LapTrinhWebCongNghe.git](https://github.com/NguyenVanHai16/LapTrinhWebCongNghe.git)
cd LapTrinhWebCongNghe
Khởi tạo môi trường ảo:

Bash

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Cài đặt thư viện:

Bash

pip install flask flask-sqlalchemy flask-login flask-bcrypt flask-wtf email-validator
Khởi chạy ứng dụng:

Bash

python app.py
Truy cập địa chỉ: http://localhost:5001

📊 Quy trình xử lý Đơn hàng
Hệ thống quản lý trạng thái đơn hàng theo luồng: Chờ xác nhận ➔ Đã xác nhận ➔ Chờ lấy hàng ➔ Đang giao hàng ➔ Đã giao hàng (Hoặc Đã hủy).
