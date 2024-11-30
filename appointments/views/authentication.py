from django.contrib.auth.forms import AuthenticationForm 
from django.shortcuts import render, redirect
from django.contrib.auth import login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
    else:
        form = AuthenticationForm()  # Render a new form for GET requests

    return render(request, 'appointments/login.html', {'form': form})


# logout view

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return render(request, 'appointments/logout.html')
    return redirect('login') 