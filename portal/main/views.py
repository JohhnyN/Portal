from django.views.generic import TemplateView
from .models import HeaderImage, UsefulLink


class HomePageView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["header_image"] = HeaderImage.objects.filter(is_active=True).first()
        context["useful_links"] = UsefulLink.objects.filter(is_active=True)
        return context
