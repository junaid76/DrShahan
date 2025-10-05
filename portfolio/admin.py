from django.contrib import admin
from .models import DoctorProfile, PatientCase, CaseImage, BeforeAfterPair

@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('site_title', 'site_domain', 'is_live', 'phone', 'email')
    search_fields = ('site_title','site_domain')

class CaseImageInline(admin.TabularInline):
    model = CaseImage
    extra = 0

class PairInline(admin.TabularInline):
    model = BeforeAfterPair
    fk_name = 'case'
    extra = 0

@admin.register(PatientCase)
class PatientCaseAdmin(admin.ModelAdmin):
    list_display = ('title','profile','category','consent_to_publish','created_at')
    list_filter = ('consent_to_publish','category')
    search_fields = ('title','profile__site_title')
    inlines = [CaseImageInline, PairInline]

@admin.register(BeforeAfterPair)
class BeforeAfterPairAdmin(admin.ModelAdmin):
    list_display = ('case','publish','featured','created_at')
    list_filter = ('publish','featured')