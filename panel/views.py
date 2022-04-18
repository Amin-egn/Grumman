from django.views import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# internal
from .models import TodoListModel


class BaseView(View):
    """Base View"""
    TEMPLATE = None

    def render(self, request, template=None, **kwargs):
        template = template or self.TEMPLATE
        return render(request, template, kwargs)


class HomeView(BaseView):
    """Home View"""
    TEMPLATE = 'vitrine.html'

    def get(self, request):
        return self.render(request)


@method_decorator(login_required, name='dispatch')
class ProjectsView(BaseView):
    """Projects View"""
    TEMPLATE = 'projects.html'

    def get(self, request):
        todo_list = TodoListModel.objects.all()
        return self.render(request, todo_list=todo_list)


@method_decorator(login_required, name='dispatch')
class NewProjectView(BaseView):
    """New Project View"""
    TEMPLATE = 'project_add.html'

    def get(self, request):
        return self.render(request)