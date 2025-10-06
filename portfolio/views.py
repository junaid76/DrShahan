from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import DoctorProfile, BeforeAfterPair, PatientCase

def home(request):
    try:
        # Get profile (no automatic demo data creation)
        profile = DoctorProfile.objects.first()
        if not profile:
            # No profile exists - show empty template (admin can create profile)
            profile = None
            
        # Get ONLY the BeforeAfterPair objects you created in admin
        featured_pairs = BeforeAfterPair.objects.filter(
            publish=True,
            featured=True,
            case__consent_to_publish=True
        ).select_related('case', 'pre_image', 'post_image').distinct()
        
        # Debug: Print what we found
        print(f"Found {featured_pairs.count()} featured pairs")
        for pair in featured_pairs:
            print(f"Pair: {pair.case.title} - {pair.pre_image.image} -> {pair.post_image.image}")
        
        # Get cases for backup display
        featured_cases = PatientCase.objects.filter(
            consent_to_publish=True
        )[:6]
            
        # Create context
        context = {
            'profile': profile, 
            'featured_pairs': featured_pairs,
            'featured_cases': featured_cases,
            'has_admin_data': featured_pairs.exists()
        }
        
        return render(request, 'portfolio/home.html', context)
        
    except Exception as e:
        # Log the error for debugging
        print(f"Template rendering error: {e}")
        import traceback
        traceback.print_exc()
        
        # Beautiful fallback HTML that matches your current view
        return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Dr. Shahan Medical Portfolio</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" rel="stylesheet">
            <style>
                .hero-section { 
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    color: white; 
                    min-height: 100vh; 
                    display: flex; 
                    align-items: center; 
                }
                .glass-card { 
                    background: rgba(255,255,255,0.1); 
                    backdrop-filter: blur(10px); 
                    border-radius: 20px; 
                    border: 1px solid rgba(255,255,255,0.2); 
                }
            </style>
        </head>
        <body>
            <section class="hero-section">
                <div class="container">
                    <div class="row justify-content-center">
                        <div class="col-lg-8 text-center">
                            <div class="glass-card p-5">
                                <i class="bi bi-heart-pulse fs-1 mb-4"></i>
                                <h1 class="display-4 fw-bold mb-3">Dr. Shahan</h1>
                                <p class="lead mb-4">Expert Medical Care & Advanced Treatments</p>
                                <p class="fs-5 mb-4">Providing exceptional medical care with years of experience.</p>
                                <div class="mt-4">
                                    <p><i class="bi bi-telephone me-2"></i>+1-555-0123</p>
                                    <p><i class="bi bi-envelope me-2"></i>dr.shahan@example.com</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </body>
        </html>
        """)

def gallery(request):
    try:
        profile = DoctorProfile.objects.first()
        
        # Get all published BeforeAfterPair objects (not just featured ones)
        pairs = BeforeAfterPair.objects.filter(
            publish=True,
            case__consent_to_publish=True
        ).select_related('case', 'pre_image', 'post_image').distinct().order_by('-created_at')
        
        # Debug: Print what we found
        print(f"Gallery found {pairs.count()} pairs")
        for pair in pairs:
            print(f"Gallery Pair: {pair.case.title} - {pair.pre_image.image} -> {pair.post_image.image}")
        
        return render(request, 'portfolio/gallery.html', {
            'profile': profile,
            'pairs': pairs  # Now using actual BeforeAfterPair objects
        })
    except Exception as e:
        print(f"Gallery error: {e}")
        import traceback
        traceback.print_exc()
        return HttpResponse('<h1>Gallery - Loading Error</h1>')

def pair_detail(request, pair_id):
    try:
        pair = get_object_or_404(BeforeAfterPair, id=pair_id, publish=True)
        return render(request, 'portfolio/pair.html', {'pair': pair})
    except Exception as e:
        print(f"Pair detail error: {e}")
        return HttpResponse('<h1>Case Details - Loading Error</h1>')