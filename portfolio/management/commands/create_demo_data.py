from django.core.management.base import BaseCommand
from portfolio.models import DoctorProfile, PatientCase, CaseImage, BeforeAfterPair
from datetime import date, timedelta

import randomimport random

import osimport os



class Command(BaseCommand):class Command(BaseCommand):

    help = 'Create comprehensive demo data including cases and before/after images'    help = 'Create comprehensive demo data including cases and before/after images'

        

    def handle(self, *args, **options):    def handle(self, *args, **options):

        # Create default profile if none exists        # Create default profile if none exists

        profile, created = DoctorProfile.objects.get_or_create(        profile, created = DoctorProfile.objects.get_or_create(

            id=1,            id=1,

            defaults={            defaults={

                'site_title': 'Dr. Shahan',                'site_title': 'Dr. Shahan',

                'tagline': 'Expert Medical Care & Advanced Treatments',                'tagline': 'Expert Medical Care & Advanced Treatments',

                'bio': 'Providing exceptional medical care with years of experience in advanced treatment techniques. Specialized in wound care, plastic surgery, and reconstructive procedures with over a decade of proven results.',                'bio': 'Providing exceptional medical care with years of experience in advanced treatment techniques. Specialized in wound care, plastic surgery, and reconstructive procedures with over a decade of proven results.',

                'specialties': 'Wound Care, Plastic Surgery, Reconstructive Surgery, Dermatology',                'specialties': 'Wound Care, Plastic Surgery, Reconstructive Surgery, Dermatology',

                'services': 'Advanced Wound Care\nPlastic Surgery\nReconstructive Surgery\nSkin Treatments\nCosmetic Procedures\nScar Revision\nSkin Grafting',                'services': 'Advanced Wound Care\nPlastic Surgery\nReconstructive Surgery\nSkin Treatments\nCosmetic Procedures\nScar Revision\nSkin Grafting',

                'achievements': 'Board Certified Physician\n10+ Years Experience\n500+ Successful Cases\nExcellence in Patient Care\nAdvanced Training Certification\nFellowship in Reconstructive Surgery',                'achievements': 'Board Certified Physician\n10+ Years Experience\n500+ Successful Cases\nExcellence in Patient Care\nAdvanced Training Certification\nFellowship in Reconstructive Surgery',

                'phone': '+92-300-1234567',                'phone': '+1-555-0123',

                'email': 'contact@drshahan.com',                'email': 'dr.shahan@example.com',

                'address': 'Medical Plaza, Karachi, Pakistan',                'address': '123 Medical Center, Healthcare City, HC 12345',

                'is_live': True                'is_live': True

            }            }

        )        )

                

        if created:        if created:

            self.stdout.write(            self.stdout.write(

                self.style.SUCCESS(f'Successfully created profile: {profile.site_title}')                self.style.SUCCESS(f'Successfully created profile: {profile.site_title}')

            )            )

        else:        else:

            self.stdout.write(            self.stdout.write(

                self.style.WARNING('Profile already exists, updating...')                self.style.WARNING('Profile already exists, updating...')

            )            )

                        

        # Create demo cases without BeforeAfterPair objects for now        # Create demo cases without BeforeAfterPair objects for now

        demo_cases = [        demo_cases = [

            {            {

                'title': 'Complex Wound Healing - Diabetic Foot Ulcer',                'title': 'Complex Wound Healing - Diabetic Foot Ulcer',

                'description': 'Advanced treatment of chronic diabetic foot ulcer using innovative wound care techniques and growth factors. This case demonstrates the effectiveness of modern wound care protocols.',                'description': 'Advanced treatment of chronic diabetic foot ulcer using innovative wound care techniques and growth factors. This case demonstrates the effectiveness of modern wound care protocols.',

                'category': 'wound-care'                'category': 'wound-care'

            },            },

            {            {

                'title': 'Facial Reconstruction After Trauma',                'title': 'Facial Reconstruction After Trauma',

                'description': 'Complete facial reconstruction following motor vehicle accident with excellent aesthetic and functional results. Multi-stage procedure with outstanding outcome.',                'description': 'Complete facial reconstruction following motor vehicle accident with excellent aesthetic and functional results. Multi-stage procedure with outstanding outcome.',

                'category': 'reconstructive'                'category': 'reconstructive'

            },            },

            {            {

                'title': 'Burn Scar Revision and Skin Grafting',                'title': 'Burn Scar Revision and Skin Grafting',

                'description': 'Comprehensive scar revision and skin grafting for burn victim with remarkable restoration of function and appearance. Advanced techniques for optimal healing.',                'description': 'Comprehensive scar revision and skin grafting for burn victim with remarkable restoration of function and appearance. Advanced techniques for optimal healing.',

                'category': 'burn-care'                'category': 'burn-care'

            },            },

            {            {

                'title': 'Pressure Ulcer Stage IV Treatment',                'title': 'Pressure Ulcer Stage IV Treatment',

                'description': 'Successful healing of stage IV pressure ulcer using advanced debridement and tissue regeneration techniques. Complete healing achieved.',                'description': 'Successful healing of stage IV pressure ulcer using advanced debridement and tissue regeneration techniques. Complete healing achieved.',

                'category': 'wound-care'                'category': 'wound-care'

            },            },

            {            {

                'title': 'Post-Surgical Wound Complication',                'title': 'Post-Surgical Wound Complication',

                'description': 'Treatment of complex post-surgical wound dehiscence with complete healing and minimal scarring. Expert wound management protocols.',                'description': 'Treatment of complex post-surgical wound dehiscence with complete healing and minimal scarring. Expert wound management protocols.',

                'category': 'wound-care'                'category': 'wound-care'

            }            }

        ]        ]

                

        cases_created = 0        cases_created = 0

                

        for case_data in demo_cases:        for case_data in demo_cases:

            # Create case            # Create case

            case, case_created = PatientCase.objects.get_or_create(            case, case_created = PatientCase.objects.get_or_create(

                profile=profile,                profile=profile,

                title=case_data['title'],                title=case_data['title'],

                defaults={                defaults={

                    'description': case_data['description'],                    'description': case_data['description'],

                    'category': case_data['category'],                    'category': case_data['category'],

                    'consent_to_publish': True                    'consent_to_publish': True

                }                }

            )            )

                        

            if case_created:            if case_created:

                cases_created += 1                cases_created += 1

                

        self.stdout.write(        self.stdout.write(

            self.style.SUCCESS(            self.style.SUCCESS(

                f'Demo data creation complete!\n'                f'Demo data creation complete!\n'

                f'- Profile: {"Created" if created else "Updated"}\n'                f'- Profile: {"Created" if created else "Updated"}\n'

                f'- Cases created: {cases_created}\n'                f'- Cases created: {cases_created}\n'

                f'- Ready for demo! (Images can be added via admin panel)\n'                f'- Ready for demo! (Images can be added via admin panel)\n'

                f'- Visit /admin/ to add before/after images'                f'- Visit /admin/ to add before/after images'

            )            )

        )        )