# Hướng dẫn SEO cho Website Django

## ✅ Đã cài đặt

### 1. Meta Tags SEO
- Title, Description, Keywords
- Open Graph (Facebook, social media)
- Google Site Verification

### 2. Công cụ Marketing
- **Google Analytics**: Theo dõi lượng truy cập
- **Facebook Pixel**: Theo dõi chuyển đổi quảng cáo Facebook

### 3. Sitemap & Robots
- **Sitemap.xml**: `/sitemap.xml` - Giúp Google index trang
- **Robots.txt**: `/robots.txt` - Hướng dẫn search engines

## 📝 Cách sử dụng

### Bước 1: Cập nhật thông tin SEO
Vào **Admin** → **Cài đặt website** → **SEO & Marketing**:

1. **Từ khóa SEO**: 
   ```
   opera hà nội, nhà hát opera, biểu diễn opera, vé opera, hồ gươm opera
   ```

2. **Ảnh chia sẻ mạng xã hội**: Upload ảnh 1200x630px

3. **Google Analytics ID**: 
   - Tạo tài khoản tại: https://analytics.google.com
   - Lấy ID dạng: `G-XXXXXXXXXX`
   - Nhập vào trường "Google Analytics ID"

4. **Google Site Verification**:
   - Vào: https://search.google.com/search-console
   - Chọn "Add property" → Nhập domain
   - Chọn phương thức "HTML tag"
   - Copy mã verification và paste vào

5. **Facebook Pixel ID**:
   - Vào: https://business.facebook.com/events_manager
   - Tạo Pixel mới
   - Copy ID (dạng số) và paste vào

### Bước 2: Chạy Migration
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Bước 3: Submit lên Google
1. Truy cập: https://search.google.com/search-console
2. Submit sitemap: `https://your-domain.com/sitemap.xml`

### Bước 4: Tối ưu nội dung
- Viết tiêu đề hấp dẫn cho mỗi chương trình
- Mô tả chi tiết, có từ khóa
- Upload ảnh chất lượng cao
- Cập nhật nội dung thường xuyên

## 🎯 Quảng cáo

### Google Ads
1. Tạo tài khoản: https://ads.google.com
2. Chạy quảng cáo tìm kiếm với từ khóa:
   - "vé opera hà nội"
   - "nhà hát opera"
   - "biểu diễn opera"

### Facebook Ads
1. Tạo tài khoản: https://business.facebook.com
2. Chạy quảng cáo với mục tiêu:
   - Traffic (Lưu lượng truy cập)
   - Conversions (Chuyển đổi)
3. Pixel đã được cài đặt sẽ theo dõi hiệu quả

### Zalo Ads
1. Tạo tài khoản: https://ads.zalo.me
2. Chạy quảng cáo tiếp cận người dùng Việt Nam

## 📊 Theo dõi hiệu quả

### Google Analytics
- Xem số lượt truy cập
- Nguồn traffic (Google, Facebook, Direct)
- Trang được xem nhiều nhất
- Thời gian ở lại trang

### Facebook Pixel
- Theo dõi số người xem trang
- Số người liên hệ
- Tối ưu quảng cáo dựa trên hành vi

## 🔍 Checklist SEO

- [ ] Cập nhật từ khóa SEO
- [ ] Upload ảnh Open Graph (1200x630px)
- [ ] Cài đặt Google Analytics
- [ ] Verify Google Search Console
- [ ] Submit sitemap.xml
- [ ] Cài đặt Facebook Pixel
- [ ] Viết mô tả hấp dẫn cho tất cả trang
- [ ] Tối ưu tốc độ website
- [ ] Đảm bảo mobile-friendly
- [ ] Cập nhật nội dung thường xuyên

## 💡 Tips
- Cập nhật chương trình mới thường xuyên
- Chia sẻ nội dung lên mạng xã hội
- Thu thập đánh giá từ khách hàng
- Tạo blog về opera (nếu có thời gian)
- Liên kết với các trang uy tín
