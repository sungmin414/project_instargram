from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from members.forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # 인증 성공시
            login(request,user)
            return redirect('posts:post-list')
        else:
            # 인증 실패시
            pass

    else:
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'members/login.html', context)