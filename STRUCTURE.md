# Cấu trúc dự án - Tên thư mục chung chung

## Thư mục `core`

Thư mục `core` là tên chung chung có thể sử dụng cho mọi dự án Django.

### Lý do chọn tên `core`:
- ✅ **Chung chung**: Phù hợp với mọi loại dự án
- ✅ **Ngắn gọn**: Dễ nhớ, dễ gõ
- ✅ **Phổ biến**: Được sử dụng rộng rãi trong cộng đồng Django
- ✅ **Ý nghĩa**: Thể hiện đây là phần lõi của ứng dụng

### Các tên thay thế khác:
- `app` - Đơn giản nhất
- `main` - Phần chính
- `base` - Nền tảng
- `common` - Chung
- `website` - Cho web app
- `api` - Cho REST API

### Cấu trúc:
```
webapp/
├── core/                   # App chính (tên chung chung)
│   ├── models.py          # Database models
│   ├── views.py           # Business logic
│   ├── admin.py           # Admin interface
│   ├── urls.py            # URL routing
│   └── templates/core/    # HTML templates
├── static/                # CSS, JS, images
├── media/                 # User uploads
└── webapp/                # Project settings
```

### Khi nào tạo app mới:
- Khi có module độc lập (blog, shop, forum)
- Khi muốn tái sử dụng code cho dự án khác
- Khi team lớn, chia theo chức năng

### Với dự án nhỏ:
- Chỉ cần 1 app `core` là đủ
- Đơn giản, dễ quản lý
- Phù hợp cho MVP, prototype
