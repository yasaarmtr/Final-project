# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from .forms import UserRegisterForm
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User



def register(request):
    if request.method == "POST":
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if password match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is already in use')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username,
                        password= password,
                        email = email,
                        first_name=first_name,
                        last_name= last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in' )
                    # return redirect('home')
                    user.save()
                    messages.success(request, 'You have registered and can log in')
                    return redirect('login')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'login.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now Logged In!')
            return redirect('index')
        else:
            messages.error(request, 'INVALID CREDENTIALS, try again...')
            return redirect('index')
    else:
        return render(request, 'home.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'you are Logged Out')
        return redirect('index')















# def home(request):
#     return render(request, 'homepage.html')

# def signin(request):
#     return render(request, 'signin.html')

# def signout(request):
#     return redirect('homepage.html')

# def register(request):
#     # if request.method == "POST":
#     #     form = UserRegisterForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         username = form.cleaned_data.get('username')
#     #         messages.success(request, f'Hi {username}, your account was created successfully')
#     #         return redirect('homepage')
#     # else:
#     #     form = UserRegisterForm()

#     # return render(request, 'register.html', {'form': form})
#     return render(request, 'register.html')

