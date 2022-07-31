from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
# Create your views here.

@login_required
def dashboard(request):
    return render(
        request,
        'account/dashboard.html',
        {'section': 'dashboard'}
    )

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            ctx = {'new_user': new_user}
            return render(
                request,
                'registration/register_done.html',
                ctx
            )
    else:
        user_form = UserRegistrationForm()
    ctx = {'user_form': user_form}    
    return render(
        request,
        'registration/register.html',
        ctx
    )