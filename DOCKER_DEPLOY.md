# Docker Deployment Guide

## Yêu cầu

- Docker
- Docker Compose

## Cài đặt Docker (Ubuntu/Debian)

```bash
# Cài Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Cài Docker Compose
sudo apt-get install docker-compose-plugin

# Thêm user vào docker group
sudo usermod -aG docker $USER
```

## Deploy

### 1. Build và chạy containers

```bash
cd /home/coder/workspace/webapp

# Build và start
docker-compose up -d --build
```

### 2. Kiểm tra logs

```bash
# Xem logs tất cả services
docker-compose logs -f

# Xem logs Django
docker-compose logs -f web

# Xem logs Nginx
docker-compose logs -f nginx
```

### 3. Truy cập

- **Website**: http://localhost
- **Admin**: http://localhost/admin
  - Username: `admin`
  - Password: `admin123`

### 4. Quản lý

```bash
# Stop containers
docker-compose stop

# Start containers
docker-compose start

# Restart containers
docker-compose restart

# Stop và xóa containers
docker-compose down

# Stop và xóa containers + volumes (XÓA DATABASE!)
docker-compose down -v
```

## Tạo superuser mới

```bash
docker-compose exec web python manage.py createsuperuser
```

## Chạy migrations

```bash
docker-compose exec web python manage.py migrate
```

## Collect static files

```bash
docker-compose exec web python manage.py collectstatic --noinput
```

## Backup Database

```bash
# Backup
docker-compose exec db pg_dump -U opera_user opera_db > backup.sql

# Restore
docker-compose exec -T db psql -U opera_user opera_db < backup.sql
```

## Production Deployment

### 1. Cập nhật environment variables

Sửa file `docker-compose.yml`:

```yaml
environment:
  - DEBUG=False
  - SECRET_KEY=your-very-long-random-secret-key-here
  - ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
  - DATABASE_URL=postgresql://opera_user:strong_password@db:5432/opera_db
```

### 2. Cập nhật PostgreSQL password

```yaml
environment:
  POSTGRES_PASSWORD: strong_password_here
```

### 3. Setup domain và SSL

Sửa `nginx.conf`:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    # Redirect to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;
    
    ssl_certificate /etc/nginx/ssl/cert.pem;
    ssl_certificate_key /etc/nginx/ssl/key.pem;
    
    # ... rest of config
}
```

### 4. Sử dụng Let's Encrypt (Certbot)

```bash
# Cài Certbot
sudo apt-get install certbot python3-certbot-nginx

# Lấy SSL certificate
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

## Monitoring

### Xem resource usage

```bash
docker stats
```

### Xem running containers

```bash
docker-compose ps
```

## Troubleshooting

### Container không start

```bash
# Xem logs
docker-compose logs web

# Rebuild
docker-compose up -d --build --force-recreate
```

### Database connection error

```bash
# Kiểm tra database container
docker-compose ps db

# Restart database
docker-compose restart db
```

### Static files không load

```bash
# Collect static lại
docker-compose exec web python manage.py collectstatic --noinput

# Restart nginx
docker-compose restart nginx
```

## Cấu trúc

```
webapp/
├── docker-compose.yml      # Docker Compose config
├── Dockerfile             # Django container
├── nginx.conf             # Nginx config
├── entrypoint.sh          # Startup script
└── requirements.txt       # Python dependencies
```

## Volumes

- `postgres_data`: PostgreSQL database
- `static_volume`: Static files (CSS, JS)
- `media_volume`: User uploads

## Ports

- `80`: Nginx (HTTP)
- `8000`: Django/Gunicorn (internal)
- `5432`: PostgreSQL (internal)

## Security Notes

1. Đổi `SECRET_KEY` trong production
2. Đổi PostgreSQL password
3. Set `DEBUG=False`
4. Cấu hình `ALLOWED_HOSTS` đúng domain
5. Sử dụng HTTPS (SSL/TLS)
6. Backup database định kỳ
