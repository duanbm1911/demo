# Hồ Gươm Opera - Website Nhà hát Opera

Dự án Django chuyên nghiệp cho website Nhà hát Opera Hồ Gươm với trang quản trị admin đầy đủ tính năng.

## Tính năng

### Website công khai:
- **Trang chủ**: Hiển thị 3 chương trình nổi bật
- **Giới thiệu**: Thông tin về nhà hát (quản lý qua admin)
- **Chương trình**: Danh sách tất cả chương trình biểu diễn
- **Media**: Thư viện ảnh
- **Liên hệ**: Form liên hệ với validation

### Admin Panel (Không cần sửa HTML):
- **Quản lý Chương trình**: 
  - Thêm/sửa/xóa events
  - Upload hình ảnh poster
  - Editor WYSIWYG cho mô tả
  - Đánh dấu nổi bật (hiển thị trang chủ)
  - Quản lý giá vé, ngày giờ
  
- **Quản lý Thư viện**: 
  - Upload và quản lý hình ảnh
  - Preview ảnh trong admin
  
- **Quản lý Liên hệ**: 
  - Xem tin nhắn từ khách hàng
  - Đánh dấu đã đọc
  
- **Quản lý Giới thiệu**: 
  - Editor WYSIWYG cho nội dung
  - Upload hình ảnh
  - Sắp xếp thứ tự hiển thị

## Cài đặt

### 1. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 2. Chạy migrations (đã có sẵn)
```bash
python3 manage.py migrate
```

### 3. Tạo superuser
```bash
python3 manage.py createsuperuser
```
Nhập username, email, password

### 4. Load dữ liệu mẫu (optional)
```bash
python3 manage.py load_sample_data
```

### 5. Chạy server
```bash
python3 manage.py runserver
```

Truy cập:
- **Website**: http://localhost:8000/
- **Admin**: http://localhost:8000/admin/

## Cấu trúc dự án

```
webapp/
├── opera/                  # App chính
│   ├── models.py          # Models: Event, Gallery, Contact, About
│   ├── views.py           # Views cho các trang
│   ├── admin.py           # Admin panel với editor
│   ├── urls.py            # URL routing
│   └── templates/         # Templates HTML
├── static/                # Static files
│   ├── css/
│   │   └── style.css     # CSS chính (tách riêng)
│   └── js/
│       └── main.js       # JavaScript (tách riêng)
├── media/                 # User uploaded files
├── webapp/                # Settings dự án
└── manage.py
```

## Sử dụng Admin

Xem file [ADMIN_GUIDE.md](ADMIN_GUIDE.md) để biết chi tiết cách sử dụng admin panel.

### Tóm tắt:
1. Đăng nhập `/admin/`
2. Thêm/sửa chương trình với editor WYSIWYG
3. Upload hình ảnh trực tiếp
4. Đánh dấu "Nổi bật" để hiển thị trang chủ
5. Mọi thay đổi có hiệu lực ngay lập tức

## Models

### Event (Chương trình)
- title, description (RichText), date
- price_min, price_max
- icon, image
- is_featured, is_active

### Gallery (Thư viện)
- title, image, description
- is_active

### Contact (Liên hệ)
- name, email, phone, message
- is_read

### About (Giới thiệu)
- title, content (RichText), image
- order, is_active

## Production Deployment

1. Đổi `DEBUG = False`
2. Cấu hình `ALLOWED_HOSTS`
3. Sử dụng PostgreSQL
4. Chạy `python3 manage.py collectstatic`
5. Cấu hình Nginx + Gunicorn
6. Setup SSL certificate

## Dependencies

- Django 5.0+
- Pillow (xử lý ảnh)
- django-ckeditor (WYSIWYG editor)

## Liên hệ

- Email: contact@hoguomopera.com
- Phone: 0835.661.999
