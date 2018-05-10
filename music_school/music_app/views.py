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
import time
from datetime import date, datetime, timedelta

teacherslist = [1, 2, 3, 4, 5, 6]
# ['Andy Garrett', 'Mika Williams', 'Milly Buxton', 'David Bernal', 'Luke Holmes', 'Caleb Dixon']
languageslist = ['English', 'German', 'Spanish', 'Italian', 'French']
instrumentlist = ['Violin', 'Flute', 'Piano', 'Claranet', 'Trumpet', 'Guitar']
timelist = ['10:00', '10:30', '11:00','11:30', 
        '12:00','12:30','13:00','13:30',
        '14:00','14:30','15:00','15:30',
        '16:00','16:30','17:00', '18:00']

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

def teacher_details(request):
    return render(request, 'music_app/teacher_details.html')

@csrf_exempt
def bookings(request):
    if (request.method == 'GET'):
        dates = []
        #Gets current days
        today = date.today()
        #Gets the date after 14 days of variable 'today'
        end_date = today + timedelta(7)
        bookedString = 'NO'

        #puts dates in array
        for y in range(0, 7):
            dates.append(today + timedelta(y))

        for i in range(0, 7): #next 7 days, 1 to 7
            dateChosen = dates[i]


            for x in range(0, 16): #lesson times, 10am to 6pm, 1 to 16 lessons
                timeChosen = timelist[x]
                for x in range (1, 6):
                    instrumentChosen = instrumentlist[x]
                    teacherChosen = teacherslist[x]
                    languageChosen = 'English'
                    created = schedule.objects.get_or_create(Instrument=instrumentChosen, 
                                Date=dateChosen,
                                Time=timeChosen,
                                Lesson_id=instrumentChosen + timeChosen + '-' + str(dateChosen),
                                Booked=bookedString,
                                teacher_id=teacherChosen,
                                Language=languageChosen)
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
def lessons(request):
    if (request.method == 'GET'):
        user_bookings = Bookings.objects.filter(student__id=request.user.id).select_related('schedule');
        return render(request, 'music_app/lessons.html', {'user_bookings':user_bookings})
    else:
        try:
            schedule_id = int(request.POST.get('id'))
            # bookings.objects.filter(schedule_id=schedule_id).delete()
            instance = Bookings.objects.filter(schedule_id=schedule_id)
            instance.delete()
            schedule.objects.filter(id=schedule_id).update(Booked='NO')
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'})
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'})

def account(request):
    if (request.method == 'GET'):
        data_list = UserProfile.objects.filter(user=request.user)
        context = {'data_list':data_list }
        return render(request, 'music_app/account.html', context)

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
