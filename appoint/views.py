from django.shortcuts import render, redirect
from .models import Time_Slot, Appointment, Hour
from .forms import Appointment_Form
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'appoint/register.html', {'form': form})


@login_required
def Form(request):
	slots = Time_Slot.objects.all()
	appointment = Appointment.objects.all()
	hour = Hour.objects.all()
	
	if request.method == "POST":
		form = Appointment_Form(request.POST)
		if form.is_valid():
			entered_from_time = form.cleaned_data['afrom_time']
			entered_to_time = form.cleaned_data['ato_time']
			entered_date = form.cleaned_data['adate']
			client = request.user
			
			li = []

			for slot in slots:
				from_time = slot.from_time
				to_time = slot.to_time
				date = slot.date
				if entered_from_time >= from_time and entered_to_time <= to_time and entered_date == date:
					if appointment:
						for app in appointment:
							if entered_date == app.adate:
								if entered_from_time != app.afrom_time and entered_to_time != app.ato_time:
									if entered_from_time < app.afrom_time and entered_to_time < app.afrom_time:
										# form.save()
										li.append(True)

									elif entered_from_time > app.afrom_time and entered_from_time > app.ato_time:
										# form.save()
										li.append(True)
									else:
										li.append(False)
								else:
									# print('appointment not available')
									li.append(False)
							else:
								# form.save()
								li.append(True)
					else:
						# form.save()
						li.append(True)



				else:
					print('appointment not available')
					# li.append(False)
			
			f = li.count(False)
			t = li.count(True)
			print(li)
			if f == 0 and t > 0 :
				app = Appointment(afrom_time=entered_from_time,ato_time=entered_to_time,adate=entered_date,client=request.user)
				app.save()			
				messages.success(request, f'Your Slot has been Booked')
				print('slot Booked')
				return redirect('home')
			else:
				messages.info(request, f'Sorry No Slots Available for this time !!')
				print('slot not available')

	else:
		form = Appointment_Form()

	context = {'slots':slots,'form':form,'appointment':appointment}
	# context = {'slots':slots,'appoint':appoint,'hour':hour}

	return render(request,'appoint/form.html',context = context)

def Home(request):
	slots = Time_Slot.objects.all()
	appointment = Appointment.objects.all()
	
	context = {'slots':slots,'appointment':appointment}


	return render(request,'appoint/home.html', context)


