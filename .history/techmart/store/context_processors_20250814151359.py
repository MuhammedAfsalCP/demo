from .models import SiteTheme

def site_theme(request):
    theme = SiteTheme.objects.first()  # assumes you have only one theme
    return {
        'site_theme': theme
    }
