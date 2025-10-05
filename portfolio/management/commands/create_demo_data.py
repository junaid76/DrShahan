from django.core.management.base import BaseCommand
from portfolio.models import DoctorProfile, PatientCase, CaseImage, BeforeAfterPair
from datetime import date, timedelta
import random
import os

class Command(BaseCommand):
    help = 'Create comprehensive demo data including cases and before/after images'
    
    def handle(self, *args, **options):
        # Create default profile if none exists
        profile, created = DoctorProfile.objects.get_or_create(
            id=1,
            defaults={
                'site_title': 'Dr. Shahan',
                'tagline': 'Expert Medical Care & Advanced Treatments',
                'bio': 'Providing exceptional medical care with years of experience in advanced treatment techniques. Specialized in wound care, plastic surgery, and reconstructive procedures with over a decade of proven results.',
                'specialties': 'Wound Care, Plastic Surgery, Reconstructive Surgery, Dermatology',
                'services': 'Advanced Wound Care\nPlastic Surgery\nReconstructive Surgery\nSkin Treatments\nCosmetic Procedures\nScar Revision\nSkin Grafting',
                'achievements': 'Board Certified Physician\n10+ Years Experience\n500+ Successful Cases\nExcellence in Patient Care\nAdvanced Training Certification\nFellowship in Reconstructive Surgery',
                'phone': '+1-555-0123',
                'email': 'dr.shahan@example.com',
                'address': '123 Medical Center, Healthcare City, HC 12345',
                'is_live': True
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created profile: {profile.site_title}')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Profile already exists, updating...')
            )
            
        # Create demo cases without BeforeAfterPair objects for now
        demo_cases = [
            {
                'title': 'Complex Wound Healing - Diabetic Foot Ulcer',
                'description': 'Advanced treatment of chronic diabetic foot ulcer using innovative wound care techniques and growth factors. This case demonstrates the effectiveness of modern wound care protocols.',
                'category': 'wound-care'
            },
            {
                'title': 'Facial Reconstruction After Trauma',
                'description': 'Complete facial reconstruction following motor vehicle accident with excellent aesthetic and functional results. Multi-stage procedure with outstanding outcome.',
                'category': 'reconstructive'
            },
            {
                'title': 'Burn Scar Revision and Skin Grafting',
                'description': 'Comprehensive scar revision and skin grafting for burn victim with remarkable restoration of function and appearance. Advanced techniques for optimal healing.',
                'category': 'burn-care'
            },
            {
                'title': 'Pressure Ulcer Stage IV Treatment',
                'description': 'Successful healing of stage IV pressure ulcer using advanced debridement and tissue regeneration techniques. Complete healing achieved.',
                'category': 'wound-care'
            },
            {
                'title': 'Post-Surgical Wound Complication',
                'description': 'Treatment of complex post-surgical wound dehiscence with complete healing and minimal scarring. Expert wound management protocols.',
                'category': 'wound-care'
            }
        ]
        
        cases_created = 0
        
        for case_data in demo_cases:
            # Create case
            case, case_created = PatientCase.objects.get_or_create(
                profile=profile,
                title=case_data['title'],
                defaults={
                    'description': case_data['description'],
                    'category': case_data['category'],
                    'consent_to_publish': True
                }
            )
            
            if case_created:
                cases_created += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Demo data creation complete!\n'
                f'- Profile: {"Created" if created else "Updated"}\n'
                f'- Cases created: {cases_created}\n'
                f'- Ready for demo! (Images can be added via admin panel)\n'
                f'- Visit /admin/ to add before/after images'
            )
        )