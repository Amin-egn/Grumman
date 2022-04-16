from django.views import View
from django.shortcuts import render


class BaseView(View):
    """Base View"""
    TEMPLATE = None

    def render(self, request, template=None, **kwargs):
        template = template or self.TEMPLATE
        return render(request, template, kwargs)


def home_view(request):
    return render(request, 'vitrine.html')
