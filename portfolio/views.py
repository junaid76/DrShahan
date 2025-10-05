from django.shortcuts import render, get_object_or_404
from .models import DoctorProfile, BeforeAfterPair

def _current_profile(request):
    host = request.get_host().split(':')[0]
    profile = DoctorProfile.objects.filter(site_domain__iexact=host, is_live=True).first()
    return profile or DoctorProfile.objects.filter(is_live=True).first()

def home(request):
    profile = _current_profile(request)
    pairs = BeforeAfterPair.objects.filter(
        case__profile=profile, publish=True, case__consent_to_publish=True, featured=True
    ).select_related('case')[:12]
    return render(request, 'portfolio/home.html', {'profile': profile, 'featured_pairs': pairs})

def gallery(request):
    profile = _current_profile(request)
    pairs = BeforeAfterPair.objects.filter(
        case__profile=profile, publish=True, case__consent_to_publish=True
    ).select_related('case').order_by('-id')
    return render(request, 'portfolio/gallery.html', {'profile': profile, 'pairs': pairs})

def public_pair(request, token):
    pair = get_object_or_404(BeforeAfterPair, public_token=token, publish=True, case__consent_to_publish=True)
    profile = pair.case.profile
    return render(request, 'portfolio/pair.html', {'profile': profile, 'pair': pair})