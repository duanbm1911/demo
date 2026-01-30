from django.db import models
from django.core.cache import cache

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, default="Hồ Gươm Opera", verbose_name="Tên website")
    logo = models.ImageField(upload_to='site/', blank=True, null=True, verbose_name="Logo")
    phone = models.CharField(max_length=20, default="0835.661.999", verbose_name="Số điện thoại")
    email = models.EmailField(default="contact@hoguomopera.com", verbose_name="Email")
    address = models.CharField(max_length=500, default="40 Hàng Bài, Cửa Nam, Hà Nội", verbose_name="Địa chỉ")
    zalo_phone = models.CharField(max_length=20, default="0835661999", verbose_name="Số Zalo")
    
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
