# Cập nhật cài đặt liên hệ (Zalo & Điện thoại)

## Tình trạng hiện tại

Hệ thống đã được cấu hình để lấy số điện thoại và Zalo từ **Site Settings** thay vì hardcode.

### Các trường đã có trong model SiteSettings:

- `phone`: Số điện thoại hiển thị (mặc định: "0835.661.999")
- `zalo_phone`: Số Zalo để chat (mặc định: "0835661999")

## Cách cập nhật

### 1. Qua Django Admin

1. Truy cập: `http://your-domain/admin/`
2. Đăng nhập với tài khoản admin
3. Vào mục **"Cài đặt website"** (Site Settings)
4. Cập nhật các trường:
   - **Số điện thoại**: Số hiển thị trên website (có thể có dấu chấm, ví dụ: 0835.661.999)
   - **Số Zalo**: Số dùng cho link Zalo (không có dấu chấm, ví dụ: 0835661999)
5. Nhấn **"Lưu"**

### 2. Các vị trí sử dụng

#### Header (Hiển thị thông tin liên hệ)
```html
<div>📞 {{ site_settings.phone }}</div>
```

#### Footer (Hiển thị thông tin liên hệ)
```html
<p>📞 {{ site_settings.phone }}</p>
```

#### Nút gọi điện (Floating button)
```html
<a href="tel:{{ site_settings.phone }}" class="call-button">
```

#### Nút chat Zalo (Floating button)
```html
<a href="https://zalo.me/{{ site_settings.zalo_phone }}" target="_blank" class="zalo-button">
```

## Lưu ý

- Số điện thoại (`phone`) có thể chứa dấu chấm hoặc khoảng trắng để hiển thị đẹp
- Số Zalo (`zalo_phone`) nên chỉ chứa số, không có ký tự đặc biệt
- Sau khi cập nhật, cache sẽ tự động được xóa và thay đổi có hiệu lực ngay lập tức
- Chỉ có thể có 1 bản ghi Site Settings duy nhất trong hệ thống

## Kiểm tra

Sau khi cập nhật, kiểm tra:
1. Header có hiển thị đúng số điện thoại không
2. Footer có hiển thị đúng số điện thoại không
3. Nút "Gọi ngay" có mở đúng số điện thoại không
4. Nút "Chat Zalo" có mở đúng link Zalo không
