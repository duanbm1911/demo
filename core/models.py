from django.db import models
from django.utils import timezone
from django.core.cache import cache
from tinymce.models import HTMLField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tên chương trình")
    description = HTMLField(verbose_name="Mô tả")
    date = models.DateTimeField(verbose_name="Ngày giờ biểu diễn")
    price_min = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Giá vé thấp nhất")
    price_max = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Giá vé cao nhất")
    icon = models.CharField(max_length=10, default="🎭", verbose_name="Icon")
    image = models.ImageField(upload_to='events/', blank=True, null=True, verbose_name="Hình ảnh")
    is_featured = models.BooleanField(default=False, verbose_name="Nổi bật")
    is_active = models.BooleanField(default=True, verbose_name="Hiển thị")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Chương trình"
        verbose_name_plural = "Chương trình biểu diễn"
        ordering = ['date']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('event_detail', args=[str(self.id)])

class Gallery(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tiêu đề")
    image = models.ImageField(upload_to='gallery/', verbose_name="Hình ảnh")
    description = models.TextField(blank=True, verbose_name="Mô tả")
    is_active = models.BooleanField(default=True, verbose_name="Hiển thị")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Thư viện"
        verbose_name_plural = "Thư viện ảnh"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            
            # Convert RGBA to RGB if needed
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = background
            
            # Resize image to max 1200x800
            max_size = (1200, 800)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Save to BytesIO
            output = BytesIO()
            img.save(output, format='JPEG', quality=85, optimize=True)
            output.seek(0)
            
            # Replace image file
            self.image = InMemoryUploadedFile(
                output, 'ImageField',
                f"{self.image.name.split('.')[0]}.jpg",
                'image/jpeg',
                sys.getsizeof(output), None
            )
        
        super().save(*args, **kwargs)

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Họ tên")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Số điện thoại")
    message = models.TextField(verbose_name="Nội dung")
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, verbose_name="Đã đọc")

    class Meta:
        verbose_name = "Liên hệ"
        verbose_name_plural = "Tin nhắn liên hệ"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email}"

class About(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tiêu đề")
    content = HTMLField(verbose_name="Nội dung")
    image = models.ImageField(upload_to='about/', blank=True, null=True, verbose_name="Hình ảnh")
    order = models.IntegerField(default=0, verbose_name="Thứ tự")
    is_active = models.BooleanField(default=True, verbose_name="Hiển thị")

    class Meta:
        verbose_name = "Giới thiệu"
        verbose_name_plural = "Nội dung giới thiệu"
        ordering = ['order']

    def __str__(self):
        return self.title


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, default="Hồ Gươm Opera", verbose_name="Tên website")
    site_title = models.CharField(max_length=200, default="Hồ Gươm Opera - Nhà hát Opera Hà Nội", verbose_name="Tiêu đề website")
    site_description = models.TextField(default="Trải nghiệm nghệ thuật opera đẳng cấp thế giới tại Hà Nội", verbose_name="Mô tả website")
    logo = models.ImageField(upload_to='site/', blank=True, null=True, verbose_name="Logo")
    favicon = models.ImageField(upload_to='site/', blank=True, null=True, verbose_name="Favicon")
    phone = models.CharField(max_length=20, default="0835.661.999", verbose_name="Số điện thoại")
    email = models.EmailField(default="contact@hoguomopera.com", verbose_name="Email")
    address = models.CharField(max_length=500, default="40 Hàng Bài, Cửa Nam, Hà Nội", verbose_name="Địa chỉ")
    zalo_phone = models.CharField(max_length=20, default="0835661999", verbose_name="Số Zalo")
    facebook_url = models.URLField(blank=True, verbose_name="Facebook URL")
    youtube_url = models.URLField(blank=True, verbose_name="YouTube URL")
    instagram_url = models.URLField(blank=True, verbose_name="Instagram URL")
    
    # SEO Fields
    keywords = models.CharField(max_length=500, blank=True, verbose_name="Từ khóa SEO", help_text="Các từ khóa cách nhau bởi dấu phẩy")
    og_image = models.ImageField(upload_to='site/', blank=True, null=True, verbose_name="Ảnh chia sẻ mạng xã hội", help_text="1200x630px")
    google_analytics = models.CharField(max_length=50, blank=True, verbose_name="Google Analytics ID", help_text="VD: G-XXXXXXXXXX")
    google_site_verification = models.CharField(max_length=100, blank=True, verbose_name="Google Site Verification")
    facebook_pixel = models.CharField(max_length=50, blank=True, verbose_name="Facebook Pixel ID")
    
    class Meta:
        verbose_name = "Cài đặt website"
        verbose_name_plural = "Cài đặt website"
    
    def __str__(self):
        return self.site_name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.delete('site_settings')
    
    @classmethod
    def get_settings(cls):
        settings = cache.get('site_settings')
        if not settings:
            settings = cls.objects.first()
            if not settings:
                settings = cls.objects.create()
            cache.set('site_settings', settings, 3600)
        return settings
