from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def register_request(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account for {username} was created!')
			login(request, user)
			return redirect('msg_app:home')
		else:
			for msg in form.error_messages:
				messages.error(request, f'{msg}: {form.error_messages[msg]}')
	form = UserRegistrationForm()
	return render(request=request,
				  template_name='users/register.html',
				  context={'form': form})


def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():

			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)

			if user is not None:
				messages.success(request, f'You were successfuly logged in as {username}!')
				login(request, user)
				return redirect('msg_app:home')
			else:
				messages.error(request, 'Invalid username or password!')
		else:
			for msg in form.error_messages:
				messages.error(request, f'{msg}: {form.error_messages[msg]}')

	form = AuthenticationForm()
	return render(request=request,
				  template_name='users/login.html',
				  context={'form': form}
				  )

def logout_request(request):
	logout(request)

	messages.info(request, f'You were logged out successfuly!')

	return redirect('msg_app:home')