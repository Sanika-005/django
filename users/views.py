from re import U
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .forms import SignUpForm,UserUpdateForm,ProfileUpdateForm
# from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from users.tokens import account_activation_token
# from django.contrib.auth.models import User
# from django.http import HttpResponse

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save(commit=False)
            # user.is_active = False
            # user.save()
            # current_site = get_current_site(request)
            # mail_subject = 'Activate your blog account.'
            # message = render_to_string('blog/acc_active_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token':account_activation_token.make_token(user),
            # })
            # to_email = form.cleaned_data.get('email')
            # email = EmailMessage(
            #             mail_subject, message, to=[to_email]
            # )
            # email.send()
            return redirect('users-login')
    else:
        form = SignUpForm()
    context = {
        'form':form
    }
    return render(request,'users/sign_up.html',context)

# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=id)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return redirect('users-login')
#     else:
#         return HttpResponse('Activation link is invalid!')

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)