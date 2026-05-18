from .models import Profile

def profile(request):
    return {
        'site_profile': Profile.objects.first()
    }