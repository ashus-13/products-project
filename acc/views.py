from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
	if request.method =='POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username = request.POST['username'])
				return render(request, 'acc/sign.html', {'error':'Username already Exist'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])	
				#auth.login(request, user)
				return redirect('home')
		else:
			return render(request, 'acc/sign.html', {'error':'Password must match'})		
	else:
		return render(request, 'acc/sign.html')

def login(request):
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request,user)
			return redirect('home')
		else:
			return render(request, 'acc/login.html', {'error':'username or password is not correct'})	

	else:
		return render(request, 'acc/login.html')

def logout(request):
	if request.method=='POST':
		auth.logout(request)
		return redirect('home')	
