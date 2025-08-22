from .models import SiteTheme
from .models import SiteTheme, SiteLogo, FooterLink, Category

def site_theme(request):
    theme = SiteTheme.objects.first()  # assumes you have only one theme
    return {
        'site_theme': theme
    }

def site_settings(request):
    return {
        'site_theme': SiteTheme.objects.first(),
        'site_logo': SiteLogo.objects.first() if 'SiteLogo' in locals() else None,
        'nav_links': Category.objects.all(),  # example: use categories as nav links
        'footer_links': FooterLink.objects.all(),
    }