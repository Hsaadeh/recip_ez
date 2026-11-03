from app.settings import MEDIA_URL


def template_context(request):
    kwargs = {
        "media_url": MEDIA_URL
    }
    return kwargs
