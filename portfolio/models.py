

# Create your models here.
from uuid import uuid4
from django.db import models

class DoctorProfile(models.Model):
    site_title = models.CharField(max_length=120, default="Dr. Shahan")
    tagline = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    specialties = models.CharField(max_length=250, blank=True)  # e.g., "Wound Care, Plastic Surgery"
    achievements = models.TextField(blank=True)  # simple bulleted text (one per line)
    services = models.TextField(blank=True)      # simple bulleted text
    hero_image = models.ImageField(upload_to='brand/', blank=True, null=True)
    logo = models.ImageField(upload_to='brand/', blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=250, blank=True)
    site_domain = models.CharField(max_length=150, blank=True)  # e.g., "drshahan.com"
    is_live = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.site_title

class PatientCase(models.Model):
    profile = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='cases')
    title = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=80, blank=True)  # e.g., "Diabetic Foot"
    consent_to_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Case #{self.id}"

class CaseImage(models.Model):
    PRE = 'PRE'; POST = 'POST'
    TYPES = [(PRE, 'Pre-op'), (POST, 'Post-op')]
    case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='cases/%Y/%m/')
    image_type = models.CharField(max_length=4, choices=TYPES)
    caption = models.CharField(max_length=200, blank=True)
    taken_at = models.DateTimeField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class BeforeAfterPair(models.Model):
    case = models.ForeignKey(PatientCase, on_delete=models.CASCADE, related_name='pairs')
    pre_image = models.ForeignKey(CaseImage, on_delete=models.CASCADE, related_name='as_pre')
    post_image = models.ForeignKey(CaseImage, on_delete=models.CASCADE, related_name='as_post')
    publish = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    public_token = models.UUIDField(default=uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        super().clean()
        
        if self.pre_image and self.pre_image.image_type != 'PRE':
            raise ValidationError({'pre_image': 'Pre-image must have image_type "PRE"'})
        
        if self.post_image and self.post_image.image_type != 'POST':
            raise ValidationError({'post_image': 'Post-image must have image_type "POST"'})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)