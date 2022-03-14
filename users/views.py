from unicodedata import name
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.generic import ListView, DetailView, TemplateView

User = get_user_model()

# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_type = request.POST['user_type']
        password = request.POST['password']
        password2 = request.POST['password2']

        # username validation
        check_users = ['admin', 'css', 'js', 'authenticate', 'login', 'logout', 'administrator', 'root', 'email',
                       'user', 'join', 'sql', 'static', 'python', 'delete', 'sex', 'sexy']

        if username in check_users:
            messages.error(request, 'Your Username, ' + username + ', Is Not Acceptable. Please Use Another Username')
            return render(request, 'users/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Your Username, ' + username + ', Already Exists. Please Try Another Username')
            return render(request, 'users/signup.html')


        # email validation
        email = email.strip().lower()
        if ("@" not in email) or (email[-4:] not in ".com.org.edu.gov.net"):
            messages.error(request, 'Your Email, ' + email + ', Is Invalid!!!')
            return render(request, 'users/signup.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Your Email, ' + email + ', Already Exists. Please Try Another Email')
            return render(request, 'users/signup.html')


        # password validation
        if password != password2:
            messages.error(request, "Your Passwords Don't match")
            return render(request, 'users/signup.html')


        User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=user_type)
        user = User.objects.get(username=username, user_type=user_type)
        context = {
            'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name, 'user_type': user_type
        }
        return render(request, 'user/signup_success.html', context)
    return render(request, 'users/signup.html')


class DoctorListView(ListView):
    template_name = 'users/team.html'
    queryset = User.objects.all()


class DoctorDetailView(DetailView):
    template_name = 'users/team_details.html'
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["doctors", 'user'] = User.objects.all()
        return context


