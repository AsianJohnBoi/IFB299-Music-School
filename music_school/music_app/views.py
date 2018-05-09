from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.forms import UserCreationForm, authenticate, UserChangeForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from music_app.forms import SignUpForm
from music_app.models import schedule, Bookings, UserProfile

def login(request):
        return render(request, 'registration/login.html')

def index(request):
    return render(request, 'music_app/index.html')

def about(request):
    return render(request, 'music_app/about.html')

def services(request):
    return render(request, 'music_app/services.html')

def contact(request):
    return render(request, 'music_app/contact.html')

def pricing(request):
    return render(request, 'music_app/pricing.html')

def reg_form(request):
    return render(request, 'music_app/reg_form.html')

@csrf_exempt
def bookings(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Booked="NO")
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)

    else:

        try:
            schedule_id = int(request.POST.get('id'))
            sched = schedule.objects.get(id = schedule_id)
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user)
            schedule.objects.filter(id=schedule_id).update(Booked='YES')
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'})
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'})

def bookings_Piano(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Instrument="Piano", Booked="NO")
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)

    else:

        try:
            schedule_id = int(request.POST.get('id'))
            sched = schedule.objects.get(id = schedule_id)
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user)
            schedule.objects.filter(id=schedule_id).update(Booked='YES')
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'})
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'})


def bookings_Claranet(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Instrument="Claranet", Booked="NO")
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)

    else:

        try:
            schedule_id = int(request.POST.get('id'))
            sched = schedule.objects.get(id = schedule_id)
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user)
            schedule.objects.filter(id=schedule_id).update(Booked='YES')
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'})
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'})

def bookings_Flute(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Instrument="Flute", Booked="NO")
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)

    else:

        try:
            schedule_id = int(request.POST.get('id'))
            sched = schedule.objects.get(id = schedule_id)
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user)
            schedule.objects.filter(id=schedule_id).update(Booked='YES')
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'})
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'})

def bookings_Violin(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Instrument="Violin", Booked="NO")
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)

    else:

        try:
            schedule_id = int(request.POST.get('id'))
            sched = schedule.objects.get(id = schedule_id)
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user)
            schedule.objects.filter(id=schedule_id).update(Booked='YES')
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'})
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'})

def bookings_Guitar(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Instrument="Guitar", Booked="NO")
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)

    else:

        try:
            schedule_id = int(request.POST.get('id'))
            sched = schedule.objects.get(id = schedule_id)
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user)
            schedule.objects.filter(id=schedule_id).update(Booked='YES')
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'})
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'})

def bookings_Trumpet(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Instrument="Trumpet", Booked="NO")
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)

    else:
        
        try:
            schedule_id = int(request.POST.get('id'))
            sched = schedule.objects.get(id = schedule_id)
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user)
            schedule.objects.filter(id=schedule_id).update(Booked='YES')
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'})
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'})

def bookings_English(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Language="English", Booked="NO")
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)

    else:

        try:
            schedule_id = int(request.POST.get('id'))
            sched = schedule.objects.get(id = schedule_id)
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user)
            schedule.objects.filter(id=schedule_id).update(Booked='YES')
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'})
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'})

def bookings_Italian(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Booked="NO", Language="Italian")
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)

    else:
        
        try:
            schedule_id = int(request.POST.get('id'))
            sched = schedule.objects.get(id = schedule_id)
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user)
            schedule.objects.filter(id=schedule_id).update(Booked='YES')
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'})
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'})

def bookings_German(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Booked="NO", Language="German")
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)

    else:
        
        try:
            schedule_id = int(request.POST.get('id'))
            sched = schedule.objects.get(id = schedule_id)
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user)
            schedule.objects.filter(id=schedule_id).update(Booked='YES')
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'})
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'})

def bookings_Spanish(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Booked="NO", Language="Spanish")
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)

    else:
        
        try:
            schedule_id = int(request.POST.get('id'))
            sched = schedule.objects.get(id = schedule_id)
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user)
            schedule.objects.filter(id=schedule_id).update(Booked='YES')
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'})
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'})

def bookings_Chinese(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Booked="NO", Language="Chinese")
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)

    else:
        
        try:
            schedule_id = int(request.POST.get('id'))
            sched = schedule.objects.get(id = schedule_id)
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user)
            schedule.objects.filter(id=schedule_id).update(Booked='YES')
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'})
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'})

def bookings_French(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Booked="NO", Language="French")
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)

    else:
        
        try:
            schedule_id = int(request.POST.get('id'))
            sched = schedule.objects.get(id = schedule_id)
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user)
            schedule.objects.filter(id=schedule_id).update(Booked='YES')
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'})
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'})

def dashboard(request):
    user_bookings = Bookings.objects.filter(student__id=request.user.id).select_related('schedule');
    context = {'user_bookings':user_bookings}
    return render(request, 'music_app/dashboard.html', context)

def lessons(request):
    user_bookings = Bookings.objects.filter(student__id=request.user.id).select_related('schedule');
    context = {'user_bookings':user_bookings}
    return render(request, 'music_app/lessons.html', context)

def account(request):
    if (request.method == 'GET'):
        data_list = UserProfile.objects.filter(user=request.user)
        context = {'data_list':data_list }
        return render(request, 'music_app/account.html', context)

# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

     # def post(self, request):
     #    form = SignUpForm(request.POST)
     #    if form.is_valid():
     #        text = form.cleaned_data['']


# def Profile(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST, user=request.user)

#         if form.is_valid():
#             form.save()
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             gender = form.cleaned_data['gender']
#             age = form.cleaned_data['age']
#             email = form.cleaned_data['email']
#             address = form.cleaned_data['address']
#             skill_level = form.cleaned_data['skill_level']
#             return redirect('dashboard')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

# username = form.cleaned_data.get('username')
# password = form.cleaned_data.get('password')
def SignUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('edit_account')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def edit_account(request):
    form = SignUpForm(request.POST, instance=request.user)
    print(request.POST.get("first_name"))
    user_id = request.user
    if form.is_valid():
        existing_instance=UserProfile.objects.filter(user=request.user)
        if (len(existing_instance) == 0):
            new_instance=UserProfile(age=request.POST.get("age"), 
            user=request.user, email=request.POST.get("email"), 
            skill_level=request.POST.get("skill_level"), 
            address=request.POST.get("address"), 
            gender=request.POST.get("gender"))
            new_instance.save()
        else:
            current_instance=existing_instance[0]
            current_instance.skill_level=request.POST.get("skill_level")
            current_instance.email=request.POST.get("email")
            current_instance.gender=request.POST.get("gender")
            current_instance.address=request.POST.get("address")
            current_instance.age=request.POST.get("age")
            current_instance.save()
        
        # new_instance.save()
        form.save()
        return redirect('/music_app/account/')
    return render(request, 'music_app/edit_account.html', {'form' : form})
