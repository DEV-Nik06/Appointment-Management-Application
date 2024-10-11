from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from ..forms import UserRegistrationForm

# Registration View
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create groups if they don't exist
            Group.objects.get_or_create(name='Student')
            Group.objects.get_or_create(name='Staff')
            

            # Assign user to the appropriate group based on the selected role
            role = request.POST.get('role')
            valid_roles = ['staff', 'student']
            if role in valid_roles:
                group, _ = Group.objects.get_or_create(name=role.capitalize())
                group.user_set.add(user)

                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login')
            else:
                messages.error(request, 'Invalid role selected.')
                return redirect('register')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    return render(request, 'appointments/register.html', {'form': form})
