from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#utility functions
'''
def hours_vs_date_every_employee():
	qs = Attendance.objects.all()
	diff=[]
	
	for obj in qs:
		ti=obj.time_in
		to=obj.time_out
		hours=((to-ti).total_seconds())/3600
		diff.append(hours)
		
	df = read_frame(qs)
	df['hours']=diff
	figure=plt.figure()
	sns.barplot(data=df,x='date',y='')
	html_graph=mpld3.fig_to_html(fig)


'''

from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

@login_required
def register(request):
    if request.user.username != 'admin':
        return redirect('not-authorised')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, f'Employee registered successfully!')
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def register2(request):
    if request.user.username != 'admin':
        return redirect('not-authorised')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, f'Employee registered successfully!')
            return redirect('dashboard2')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register2.html', {'form': form})




