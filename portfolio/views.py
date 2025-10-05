from django.shortcuts import render, get_object_or_404
from .models import DoctorProfile, BeforeAfterPair

def _current_profile(request):
    host = request.get_host().split(':')[0]
    profile = DoctorProfile.objects.filter(site_domain__iexact=host, is_live=True).first()
    if not profile:
        profile = DoctorProfile.objects.filter(is_live=True).first()
    
    # If no profile exists, create a default one
    if not profile:
        profile = DoctorProfile.objects.create(
            site_title='Dr. Shahan',
            tagline='Expert Medical Care & Advanced Treatments',
            bio='Providing exceptional medical care with years of experience in advanced treatment techniques.',
            specialties='Wound Care, Plastic Surgery, Reconstructive Surgery',
            services='Advanced Wound Care\nPlastic Surgery\nReconstructive Surgery\nSkin Treatments',
            achievements='Board Certified Physician\n10+ Years Experience\n500+ Successful Cases\nExcellence in Patient Care',
            phone='+1-555-0123',
            email='dr.shahan@example.com',
            address='123 Medical Center, Healthcare City',
            is_live=True
        )
    
    return profile

def home(request):
    try:
        profile = _current_profile(request)
        pairs = BeforeAfterPair.objects.filter(
            case__profile=profile, publish=True, case__consent_to_publish=True, featured=True
        ).select_related('case')[:12] if profile else []
        return render(request, 'portfolio/home.html', {'profile': profile, 'featured_pairs': pairs})
    except Exception as e:
        # Fallback for any errors
        profile = DoctorProfile.objects.first()
        if not profile:
            profile = DoctorProfile.objects.create(
                site_title='Dr. Shahan',
                tagline='Expert Medical Care & Advanced Treatments',
                bio='Welcome to our medical portfolio.',
                is_live=True
            )
        return render(request, 'portfolio/home.html', {'profile': profile, 'featured_pairs': []})

def gallery(request):
    try:
        profile = _current_profile(request)
        pairs = BeforeAfterPair.objects.filter(
            case__profile=profile, publish=True, case__consent_to_publish=True
        ).select_related('case').order_by('-id') if profile else []
        return render(request, 'portfolio/gallery.html', {'profile': profile, 'pairs': pairs})
    except Exception as e:
        profile = _current_profile(request)
        return render(request, 'portfolio/gallery.html', {'profile': profile, 'pairs': []})

def public_pair(request, token):
    try:
        pair = get_object_or_404(BeforeAfterPair, public_token=token, publish=True, case__consent_to_publish=True)
        profile = pair.case.profile
        return render(request, 'portfolio/pair.html', {'profile': profile, 'pair': pair})
    except Exception as e:
        profile = _current_profile(request)
        return render(request, 'portfolio/home.html', {'profile': profile, 'featured_pairs': []})