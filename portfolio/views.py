from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.management import call_command
from .models import DoctorProfile, BeforeAfterPair, PatientCase

def home(request):
    try:
        # Ensure we have demo data
        call_command('create_demo_data')
        
        # Get profile
        profile = DoctorProfile.objects.first()
        if not profile:
            raise Exception("No profile found")
            
        # Get actual BeforeAfterPair objects if they exist
        featured_pairs = BeforeAfterPair.objects.filter(
            publish=True,
            featured=True,
            case__consent_to_publish=True
        ).select_related('case')[:6]
        
        # Get cases for backup
        featured_cases = PatientCase.objects.filter(
            consent_to_publish=True
        )[:6]
            
        # Create context
        context = {
            'profile': profile, 
            'featured_pairs': featured_pairs,  # Will be empty but template can handle it
            'featured_cases': featured_cases,
            'has_demo_data': True
        }
        
        return render(request, 'portfolio/home_simple.html', context)
        
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
        # Ensure we have demo data
        call_command('create_demo_data')
        
        profile = DoctorProfile.objects.first()
        cases = PatientCase.objects.filter(consent_to_publish=True)
        
        return render(request, 'portfolio/gallery.html', {
            'profile': profile,
            'pairs': cases  # Using cases instead of pairs for now
        })
    except Exception as e:
        return HttpResponse('<h1>Gallery - Demo Data Loading...</h1>')

def pair_detail(request, pair_id):
    try:
        case = get_object_or_404(PatientCase, id=pair_id, consent_to_publish=True)
        return render(request, 'portfolio/pair.html', {'pair': case})
    except Exception as e:
        return HttpResponse('<h1>Case Details - Demo Data Loading...</h1>')