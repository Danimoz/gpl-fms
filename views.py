from django.shortcuts import render, redirect
from .forms import StaffUserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = StaffUserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            department = form.cleaned_data.get('department')

            messages.success(request, f'Account created for {username} in {department}!')
            return redirect('login')
    else:
        form = StaffUserCreationForm()


    return render(request, 'pages/register.html', {'form': form})