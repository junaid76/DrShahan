from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import DoctorProfile, BeforeAfterPair

def home(request):
    # Create profile data directly for demo
    context = {
        'profile': {
            'site_title': 'Dr. Shahan',
            'tagline': 'Expert Medical Care & Advanced Treatments',
            'bio': 'Providing exceptional medical care with years of experience in advanced treatment techniques.',
            'specialties': 'Wound Care, Plastic Surgery, Reconstructive Surgery',
            'services': 'Advanced Wound Care\nPlastic Surgery\nReconstructive Surgery\nSkin Treatments',
            'achievements': 'Board Certified Physician\n10+ Years Experience\n500+ Successful Cases\nExcellence in Patient Care',
            'phone': '+1-555-0123',
            'email': 'dr.shahan@example.com',
            'address': '123 Medical Center, Healthcare City',
        },
        'featured_pairs': []  # Empty for now
    }
    
    try:
        return render(request, 'portfolio/home.html', context)
    except Exception as e:
        # Ultimate fallback - return simple HTML
        return HttpResponse(f'''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Dr. Shahan Medical Portfolio</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container py-5">
                <div class="text-center">
                    <h1 class="display-4 text-primary">Dr. Shahan</h1>
                    <p class="lead">Expert Medical Care & Advanced Treatments</p>
                    <p>Providing exceptional medical care with years of experience.</p>
                    <a href="/admin/" class="btn btn-primary">Admin Panel</a>
                </div>
            </div>
            <footer class="bg-light py-4 mt-5">
                <div class="container text-center">
                    <p class="mb-0">📞 +1-555-0123 | ✉️ dr.shahan@example.com</p>
                </div>
            </footer>
        </body>
        </html>
        ''')

def gallery(request):
    try:
        profile = DoctorProfile.objects.first()
        if not profile:
            profile = DoctorProfile.objects.create(
                site_title='Dr. Shahan',
                tagline='Expert Medical Care & Advanced Treatments',
                bio='Medical Portfolio',
                is_live=True
            )
        
        pairs = BeforeAfterPair.objects.filter(
            case__profile=profile, publish=True, case__consent_to_publish=True
        ).select_related('case').order_by('-id')
        
        return render(request, 'portfolio/gallery.html', {'profile': profile, 'pairs': pairs})
    except Exception as e:
        return HttpResponse('<h1>Gallery Coming Soon</h1><a href="/">Back to Home</a>')

def public_pair(request, token):
    try:
        pair = get_object_or_404(BeforeAfterPair, public_token=token, publish=True, case__consent_to_publish=True)
        profile = pair.case.profile
        return render(request, 'portfolio/pair.html', {'profile': profile, 'pair': pair})
    except Exception as e:
        return HttpResponse('<h1>Case Not Found</h1><a href="/">Back to Home</a>')