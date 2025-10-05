from django.core.management.base import BaseCommand
from portfolio.models import DoctorProfile

class Command(BaseCommand):
    help = 'Create sample data for demo'
    
    def handle(self, *args, **options):
        # Create default profile if none exists
        if not DoctorProfile.objects.exists():
            profile = DoctorProfile.objects.create(
                site_title='Dr. Shahan',
                tagline='Expert Medical Care & Advanced Treatments',
                bio='Providing exceptional medical care with years of experience in advanced treatment techniques. Specialized in wound care, plastic surgery, and reconstructive procedures.',
                specialties='Wound Care, Plastic Surgery, Reconstructive Surgery',
                services='Advanced Wound Care\nPlastic Surgery\nReconstructive Surgery\nSkin Treatments\nCosmetic Procedures',
                achievements='Board Certified Physician\n10+ Years Experience\n500+ Successful Cases\nExcellence in Patient Care\nAdvanced Training Certification',
                phone='+1-555-0123',
                email='dr.shahan@example.com',
                address='123 Medical Center, Healthcare City, HC 12345',
                is_live=True
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created profile: {profile.site_title}')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Profile already exists')
            )