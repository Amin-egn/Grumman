from django.views import View
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# internal
from .models import TodoListModel, TodoItemModel
from .forms import TodoListForm


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
class AllBoardView(BaseView):
    """Projects View"""
    TEMPLATE = 'all_board.html'

    def get(self, request):
        all_board = TodoListModel.objects.all()
        form = TodoListForm()
        return self.render(request, all_board=all_board, form=form)

    def post(self, request):
        form = TodoListForm(request.POST)
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.person = request.user
            todo_list.save()
            messages.success(request, 'Board created successfully.')
            return redirect('all_board')

        return self.render(request, form=form)


@method_decorator(login_required, name='dispatch')
class DeleteBoardView(BaseView):
    """Delete Project View"""
    def post(self, request, pk):
        board = get_object_or_404(TodoListModel, pk=pk)
        board.delete()
        messages.info(request, 'Board deleted successfully.')
        return redirect('all_board')


class BoardTaskView(BaseView):
    """Board Task View"""
    TEMPLATE = 'board_details.html'

    def get(self, request, pk):
        board = get_object_or_404(TodoListModel, pk=pk)
        items = board.items.all()
        context = {
            'board': board,
            'items': items
        }
        return self.render(request, **context)

    def post(self, request, pk):
        pass
