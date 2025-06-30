import qrcode
from io import BytesIO
from django.core.files import File
from django.db import models
from django.contrib.auth.models import User
import uuid

class QRCode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.SlugField(unique=True)
    target_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    scan_count = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    qr_image = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        # Only generate QR code if one doesn't already exist
        if not self.qr_image:
            qr = qrcode.make(f'https://yourdomain.com/{self.code}')
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            self.qr_image.save(f'qr_{self.code}.png', File(buffer), save=False)
        super().save(*args, **kwargs)
