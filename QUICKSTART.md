# Quick Start Guide

## Chạy Development Server

### Cách 1: Sử dụng script (Khuyến nghị)
```bash
cd /home/coder/workspace/webapp
./run.sh
```

### Cách 2: Chạy thủ công
```bash
cd /home/coder/workspace/webapp

# Nếu dùng virtual environment
source /home/coder/workspace/.venv/bin/activate

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy migrations
python manage.py migrate

# Load dữ liệu mẫu (nếu chưa có)
python manage.py load_sample_data

# Chạy server
python manage.py runserver 0.0.0.0:8000
```

## Truy cập

- **Website**: http://localhost:8000/
- **Admin**: http://localhost:8000/admin/

## Tạo Admin User

```bash
python manage.py createsuperuser
```

## Chạy với Docker

```bash
cd /home/coder/workspace/webapp

# Build và start
docker-compose up -d --build

# Xem logs
docker-compose logs -f

# Stop
docker-compose down
```

## Cấu trúc URL

- `/` - Trang chủ
- `/about/` - Giới thiệu
- `/events/` - Danh sách chương trình
- `/events/<id>/` - Chi tiết chương trình
- `/gallery/` - Thư viện ảnh
- `/contact/` - Liên hệ
- `/admin/` - Quản trị

## Troubleshooting

### Lỗi: ModuleNotFoundError
```bash
pip install -r requirements.txt
```

### Lỗi: Database
```bash
python manage.py migrate
```

### Lỗi: Static files không load
```bash
python manage.py collectstatic --noinput
```

### Reset database
```bash
rm db.sqlite3
python manage.py migrate
python manage.py load_sample_data
python manage.py createsuperuser
```
