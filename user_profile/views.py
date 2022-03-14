from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
import string
import random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# Create your views here.
@login_required(login_url='/login/')
def CreateUserProfile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            # try:
            password = User.objects.make_random_password()
            username = profile.name.split()[0] + id_generator()
            user = User.objects.create(username=username, user_type="P")
            user.set_password(password)
            user.save_base(raw=True)
            profile.user = user
            profile.save()
            return redirect('appointment:r_dashboard')
        
    else:
        form = ProfileUpdateForm()
    return render(request, 'user_profile/profile_create.html', {'form': form})
