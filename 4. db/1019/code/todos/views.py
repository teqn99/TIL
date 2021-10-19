from django.shortcuts import redirect, render
from todos.forms import TodoForm
from .models import Todo 
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    # todos = Todo.objects.all()
    # 위 코드의 문제 : test1, test2의 todo를 서로 볼 수 있음
    # 로그인한 사람의 todo만 보이도록 수정할 것

    #본인이 작성한 todo만 보이도록 설정
    todos = request.user.todo_set.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)


def new(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/new.html', context)