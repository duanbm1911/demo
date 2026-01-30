# Hướng dẫn sử dụng Admin Panel

## Đăng nhập Admin

1. Tạo superuser (chỉ làm 1 lần):
```bash
python3 manage.py createsuperuser
```

2. Truy cập: http://localhost:8000/admin/

## Quản lý Chương trình (Events)

### Thêm chương trình mới:
1. Vào **Chương trình biểu diễn** → **Thêm Chương trình**
2. Điền thông tin:
   - **Tên chương trình**: Tên vở opera/nhạc kịch
   - **Icon**: Emoji (🎭, 🎼, 🎵, 🎹, 🎪, 🎺)
   - **Hình ảnh**: Upload ảnh poster (không bắt buộc)
   - **Mô tả**: Sử dụng editor để format text (bold, italic, list, v.v.)
   - **Ngày giờ biểu diễn**: Chọn ngày và giờ
   - **Giá vé**: Nhập giá thấp nhất và cao nhất
   - **Nổi bật**: Tick để hiển thị trang chủ (chỉ chọn 3 chương trình)
   - **Hiển thị**: Tick để kích hoạt

### Chỉnh sửa:
- Click vào tên chương trình trong danh sách
- Sửa thông tin và Save

### Xóa:
- Chọn checkbox các chương trình cần xóa
- Chọn "Delete selected" → Go

## Quản lý Thư viện (Gallery)

### Thêm ảnh:
1. Vào **Thư viện ảnh** → **Thêm Thư viện**
2. Upload hình ảnh
3. Nhập tiêu đề và mô tả
4. Tick **Hiển thị** để kích hoạt

## Quản lý Liên hệ (Contact)

- Xem tin nhắn từ khách hàng
- Đánh dấu **Đã đọc** khi xử lý xong
- Không thể chỉnh sửa nội dung (chỉ đọc)

## Quản lý Giới thiệu (About)

### Thêm/sửa nội dung:
1. Vào **Nội dung giới thiệu**
2. Sử dụng editor để viết nội dung với format đẹp
3. Upload hình ảnh minh họa (không bắt buộc)
4. Đặt **Thứ tự** để sắp xếp (số nhỏ hiển thị trước)
5. Tick **Hiển thị** để kích hoạt

## Tips

### Editor (CKEditor):
- **Bold**: Ctrl+B
- **Italic**: Ctrl+I
- **Link**: Ctrl+K
- **List**: Click nút bullet/number
- **Upload ảnh**: Click icon ảnh trong editor

### Hiển thị trang chủ:
- Chỉ chọn 3 chương trình **Nổi bật**
- Các chương trình khác vẫn hiển thị ở trang Chương trình

### Quản lý hình ảnh:
- Kích thước khuyến nghị: 800x600px
- Format: JPG, PNG
- Dung lượng: < 2MB

### Sắp xếp:
- **Events**: Tự động sắp xếp theo ngày
- **Gallery**: Mới nhất hiển thị trước
- **About**: Theo thứ tự đã đặt

## Lưu ý

- Tất cả thay đổi có hiệu lực ngay lập tức
- Không cần restart server
- Không cần sửa code HTML
- Backup database định kỳ: `python3 manage.py dumpdata > backup.json`
