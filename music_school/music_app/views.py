"""
Renders the html page using the html files and database models from models.py. Each link is clicked on a website, will 
call the url specified in urls.py then calls a function here in views.py. Each function on this page will get the html file
inside the templates folder. It will also retrieve the database tables if needed for the page. once all information is gathere
Django, pages are rendered and displayed for the user.
"""

from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.forms import UserCreationForm, authenticate, UserChangeForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.db.models import F


from music_app.forms import SignUpForm
from music_app.models import schedule, Bookings, UserProfile, teacher, instrument
import time
from datetime import date, datetime, timedelta

#Specify the teacher id in array
teacherslist = [1, 2, 3, 4, 5, 6]

#Specify names of each teacher in an array
teacherNames = ['Mika Williams', 'Andy Garrett', 'Milly Buxton', 'David Bernal', 'Luke Holmes', 'Caleb Dixon']

#Specify the available languages
languageslist = ['English', 'German', 'Spanish', 'Italian', 'French']

#Specify the available instruments
instrumentlist = ['Violin', 'Flute', 'Piano', 'Saxophone', 'Drums', 'Guitar']

#Specify the school's open times
timelist = ['10:00', '10:30', '11:00','11:30',
        '12:00','12:30','13:00','13:30',
        '14:00','14:30','15:00','15:30',
        '16:00','16:30','17:00', '18:00']

#Rename instruments imported from music_app.models as it will conflict with function definition names and variables
theinstruments = instrument

#Return the login html page
def loginPage(request):
    return render(request, 'registration/login.html')

#Return the home html page
def indexPage(request):
    return render(request, 'music_app/index.html')

#Return the instrument html page
def instrumentPage(request):
    if (request.method == 'GET'):
        #Specifies the amount of instruments made to be available
        amount = 100
        for x in range(0, 6):
            #Check if instrument exists in datable table 'instruments'
            if theinstruments.objects.filter(instrument_name=instrumentlist[x]).exists():
                continue
            #If instrument doesn't exist, add instrument to the database and add starting quantity
            else:
                created = theinstruments.objects.get_or_create(instrument_name=instrumentlist[x], quantity=amount)
        return render(request, 'music_app/instrument.html')

@csrf_exempt #exempts csrf token needed to display page
def paymentPage(request):
    if (request.method == 'GET'):
        data_list = theinstruments.objects.filter(quantity__gt=0) #gets all instruments that have a quantity greater than 0
        context = {'data_list':data_list } 
        return render(request, 'music_app/payment.html', context) #renders instruments data and html page
    else:
        try:
            #get the selected instrument
            instrumentHiring = str(request.POST.get('id'))

            #Deduct the instrument quantity in the database 'instruments'
            theinstruments.objects.filter(instrument_name=instrumentHiring).update(quantity=F('quantity') - 1)

            #Return ok response, no errors in the process
            return JsonResponse({'status': 'ok'})
        except theinstruments.DoesNotExist:
            #display message that the instrument is incorrect, doesn't match the database
            return JsonResponse({'status':'error', 'message': 'Instrument does not exists'}) 
        except ValueError:
            import traceback
            #display message that the instrument is incorrect
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid Instrument'})

#Return the about html page
def aboutPage(request):
    return render(request, 'music_app/about.html')

#Return the services html page
def servicesPage(request):
    return render(request, 'music_app/services.html')

#Return the contact html page
def contactPage(request):
    return render(request, 'music_app/contact.html')

#Return the pricing html page
def pricingPage(request):
    return render(request, 'music_app/pricing.html')

#Return the registration html page
def reg_formPage(request):
    return render(request, 'music_app/reg_form.html')


@csrf_exempt #exempts csrf token needed to display page
def bookingsPage(request):
    if (request.method == 'GET'):
        #Makes sure teachers are on the database, if not create the teachers
        for b in range(0, 6):
            addTeacher = teacherNames[b]
            roomNO = teacherslist[b]
            #add selected teacher and the room number and add/update to teachers database table
            created = teacher.objects.get_or_create(name=addTeacher, room=roomNO)

        #create array to store the dates
        dates = []

        #Gets current date
        today = date.today()

        #Gets the date after 14 days of variable 'today'
        end_date = today + timedelta(7)
        bookedString = 'NO'

        #Delete all lessons in schedule table that haven't been booked
        #Gets rid of old dates
        schedule.objects.filter(Booked="NO").delete()

        #puts dates in 'date' array
        for y in range(0, 7):
            dates.append(today + timedelta(y))

        #add lessons
        for i in range(0, 7): #next 7 days, 1 to 7
            dateChosen = dates[i]

            #creates lessons and stores in schedule database table
            for x in range(0, 16): #lesson times, 10am to 6pm, 1 to 16 lessons
                timeChosen = timelist[x]
                for x in range (0, 6):
                    instrumentChosen = instrumentlist[x]
                    teacherChosen = teacherslist[x]
                    languageChosen = 'English'

                    #Add all retrieve values and store in the schedule database table
                    created = schedule.objects.get_or_create(Instrument=instrumentChosen,
                                Date=dateChosen,
                                Time=timeChosen,
                                Lesson_id=instrumentChosen + timeChosen + '-' + str(dateChosen),
                                Booked=bookedString,
                                teacher_id=teacherChosen,
                                Language=languageChosen)

        #Get all lessons that haven't been booked and display on the page
        data_list = schedule.objects.filter(Booked="NO")
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)

    else:

        try:
            schedule_id = int(request.POST.get('id')) #Gets the chosen lesson, gets button's id
            sched = schedule.objects.get(id = schedule_id) #Gets the schedule id from the schedule database
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user) #adds lesson information to the 'bookings' table
            schedule.objects.filter(id=schedule_id).update(Booked='YES') #update lesson in the schedule table's booked status from 'NO' to 'YES'
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'}) #display error is obtained id is wrong
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'}) #display error is obtained id is wrong

@csrf_exempt #exempts csrf token needed to display page
def bookings_Piano(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Instrument="Piano", Booked="NO") #get lessons from the schedule database with that is Piano and has not been booked
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context) #render html page & retrieved data and display for user

    else:

        try:
            schedule_id = int(request.POST.get('id')) #Gets the chosen lesson, gets button's id
            sched = schedule.objects.get(id = schedule_id) #Gets the schedule id from the schedule database
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user) #adds lesson information to the 'bookings' table
            schedule.objects.filter(id=schedule_id).update(Booked='YES') #update lesson in the schedule table's booked status from 'NO' to 'YES'
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'}) #display error is obtained id is wrong
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'}) #display error is obtained id is wrong

@csrf_exempt #exempts csrf token needed to display page
def bookings_Saxophone(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Instrument="Saxophone", Booked="NO")#get lessons from the schedule database with that is saxophone and has not been booked
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context) #render html page & retrieved data and display for user

    else:

        try:
            schedule_id = int(request.POST.get('id')) #Gets the chosen lesson, gets button's id
            sched = schedule.objects.get(id = schedule_id) #Gets the schedule id from the schedule database
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user) #adds lesson information to the 'bookings' table
            schedule.objects.filter(id=schedule_id).update(Booked='YES') #update lesson in the schedule table's booked status from 'NO' to 'YES'
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'}) #display error is obtained id is wrong
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'}) #display error is obtained id is wrong

@csrf_exempt #exempts csrf token needed to display page
def bookings_Flute(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Instrument="Flute", Booked="NO")#get lessons from the schedule database with that is flute and has not been booked
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context) #render html page & retrieved data and display for user

    else:

        try:
            schedule_id = int(request.POST.get('id')) #Gets the chosen lesson, gets button's id
            sched = schedule.objects.get(id = schedule_id) #Gets the schedule id from the schedule database
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user) #adds lesson information to the 'bookings' table
            schedule.objects.filter(id=schedule_id).update(Booked='YES') #update lesson in the schedule table's booked status from 'NO' to 'YES'
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'}) #display error is obtained id is wrong
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'}) #display error is obtained id is wrong

@csrf_exempt #exempts csrf token needed to display page
def bookings_Violin(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Instrument="Violin", Booked="NO") #get lessons from the schedule database with that is violin and has not been booked
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context) #render html page & retrieved data and display for user

    else:

        try:
            schedule_id = int(request.POST.get('id')) #Gets the chosen lesson, gets button's id
            sched = schedule.objects.get(id = schedule_id) #Gets the schedule id from the schedule database
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user) #adds lesson information to the 'bookings' table
            schedule.objects.filter(id=schedule_id).update(Booked='YES') #update lesson in the schedule table's booked status from 'NO' to 'YES'
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'}) #display error is obtained id is wrong
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'}) #display error is obtained id is wrong

@csrf_exempt #exempts csrf token needed to display page
def bookings_Guitar(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Instrument="Guitar", Booked="NO") #get lessons from the schedule database with that is guitar and has not been booked
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context) #render html page & retrieved data and display for user

    else:

        try:
            schedule_id = int(request.POST.get('id')) #Gets the chosen lesson, gets button's id
            sched = schedule.objects.get(id = schedule_id) #Gets the schedule id from the schedule database
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user) #adds lesson information to the 'bookings' table
            schedule.objects.filter(id=schedule_id).update(Booked='YES') #update lesson in the schedule table's booked status from 'NO' to 'YES'
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'}) #display error is obtained id is wrong
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'}) #display error is obtained id is wrong

@csrf_exempt #exempts csrf token needed to display page
def bookings_Drums(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Instrument="Drums", Booked="NO") #get lessons from the schedule database with that is drums and has not been booked
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context) #render html page & retrieved data and display for user

    else:

        try:
            schedule_id = int(request.POST.get('id')) #Gets the chosen lesson, gets button's id
            sched = schedule.objects.get(id = schedule_id) #Gets the schedule id from the schedule database
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user) #adds lesson information to the 'bookings' table
            schedule.objects.filter(id=schedule_id).update(Booked='YES') #update lesson in the schedule table's booked status from 'NO' to 'YES'
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'}) #display error is obtained id is wrong
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'}) #display error is obtained id is wrong

@csrf_exempt #exempts csrf token needed to display page
def bookings_English(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Language="English", Booked="NO") #get lessons from the schedule database with that is english and has not been booked
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context) #render html page & retrieved data and display for user

    else:

        try:
            schedule_id = int(request.POST.get('id')) #Gets the chosen lesson, gets button's id
            sched = schedule.objects.get(id = schedule_id) #Gets the schedule id from the schedule database
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user) #adds lesson information to the 'bookings' table
            schedule.objects.filter(id=schedule_id).update(Booked='YES') #update lesson in the schedule table's booked status from 'NO' to 'YES'
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'}) #display error is obtained id is wrong
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'}) #display error is obtained id is wrong

@csrf_exempt #exempts csrf token needed to display page
def bookings_Italian(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Booked="NO", Language="Italian") #get lessons from the schedule database with that is italian and has not been booked
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context) #render html page & retrieved data and display for user

    else:

        try:
            schedule_id = int(request.POST.get('id')) #Gets the chosen lesson, gets button's id
            sched = schedule.objects.get(id = schedule_id) #Gets the schedule id from the schedule database
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user) #adds lesson information to the 'bookings' table
            schedule.objects.filter(id=schedule_id).update(Booked='YES') #update lesson in the schedule table's booked status from 'NO' to 'YES'
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'}) #display error is obtained id is wrong
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'}) #display error is obtained id is wrong

@csrf_exempt #exempts csrf token needed to display page
def bookings_German(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Booked="NO", Language="German") #get lessons from the schedule database with that is german and has not been booked
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)#render html page & retrieved data and display for user

    else:

        try:
            schedule_id = int(request.POST.get('id')) #Gets the chosen lesson, gets button's id
            sched = schedule.objects.get(id = schedule_id) #Gets the schedule id from the schedule database
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user) #adds lesson information to the 'bookings' table
            schedule.objects.filter(id=schedule_id).update(Booked='YES') #update lesson in the schedule table's booked status from 'NO' to 'YES'
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'}) #display error is obtained id is wrong
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'}) #display error is obtained id is wrong

@csrf_exempt #exempts csrf token needed to display page
def bookings_Spanish(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Booked="NO", Language="Spanish") #get lessons from the schedule database with that is spanish and has not been booked
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)#render html page & retrieved data and display for user
    else:
        try:
            schedule_id = int(request.POST.get('id')) #Gets the chosen lesson, gets button's id
            sched = schedule.objects.get(id = schedule_id) #Gets the schedule id from the schedule database
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user) #adds lesson information to the 'bookings' table
            schedule.objects.filter(id=schedule_id).update(Booked='YES') #update lesson in the schedule table's booked status from 'NO' to 'YES'
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'}) #display error is obtained id is wrong
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'}) #display error is obtained id is wrong

@csrf_exempt #exempts csrf token needed to display page
def bookings_Chinese(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Booked="NO", Language="Chinese") #get lessons from the schedule database with that is chinese and has not been booked
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)#render html page & retrieved data and display for user

    else:

        try:
            schedule_id = int(request.POST.get('id')) #Gets the chosen lesson, gets button's id
            sched = schedule.objects.get(id = schedule_id) #Gets the schedule id from the schedule database
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user) #adds lesson information to the 'bookings' table
            schedule.objects.filter(id=schedule_id).update(Booked='YES') #update lesson in the schedule table's booked status from 'NO' to 'YES'
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'}) #display error is obtained id is wrong
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'}) #display error is obtained id is wrong

@csrf_exempt #exempts csrf token needed to display page
def bookings_French(request):
    if (request.method == 'GET'):
        data_list = schedule.objects.filter(Booked="NO", Language="French") #get lessons from the schedule database with that is french and has not been booked
        context = {'data_list':data_list }
        return render(request, 'music_app/bookings.html', context)#render html page & retrieved data and display for user

    else:

        try:
            schedule_id = int(request.POST.get('id')) #Gets the chosen lesson, gets button's id
            sched = schedule.objects.get(id = schedule_id) #Gets the schedule id from the schedule database
            booking, created = Bookings.objects.get_or_create(schedule=sched, student=request.user) #adds lesson information to the 'bookings' table
            schedule.objects.filter(id=schedule_id).update(Booked='YES') #update lesson in the schedule table's booked status from 'NO' to 'YES'
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'}) #display error is obtained id is wrong
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'}) #display error is obtained id is wrong

#display's dashboard page
def dashboardPage(request):
    user_bookings = Bookings.objects.filter(student__id=request.user.id).select_related('schedule'); #Get user's bookings using the current user's id
    context = {'user_bookings':user_bookings}
    return render(request, 'music_app/dashboard.html', context)#render html page & retrieved data and display for user

#displays user's booked lessons
@csrf_exempt #exempts csrf token needed to display page
def lessonsPage(request):
    if (request.method == 'GET'):
        user_bookings = Bookings.objects.filter(student__id=request.user.id).select_related('schedule'); #Get user's bookings using the current user's id
        return render(request, 'music_app/lessons.html', {'user_bookings':user_bookings}) #render html page & retrieved data and display for user
    else:
        try:
            schedule_id = int(request.POST.get('id')) #get selected lesson for cancellation
            instance = Bookings.objects.filter(schedule_id=schedule_id) #finds lesson booked
            instance.delete() #removes booked lesson from the bookings table
            schedule.objects.filter(id=schedule_id).update(Booked='NO') #finds lesson in the schedule table and updates it from 'YES' to 'NO'
            return JsonResponse({'status': 'ok'})
        except schedule.DoesNotExist:
            return JsonResponse({'status':'error', 'message': 'Schedule does not exists'}) #display error is obtained id is wrong
        except ValueError:
            import traceback
            traceback.print_exc()
            return JsonResponse({'status':'error', 'message': 'Invalid shcedule id'}) #display error is obtained id is wrong

def accountPage(request):
    if (request.method == 'GET'):
        data_list = UserProfile.objects.filter(user=request.user) #gets user's profile information from the UserProfile table
        context = {'data_list':data_list }
        return render(request, 'music_app/account.html', context) #render html page & retrieved data and display for user

def SignUpPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) #gets the default sign up form 
        if form.is_valid():
            user = form.save() #saves form input to the database table called users_auth 
            username = form.cleaned_data.get('username') #retrieves username and saves it
            raw_password = form.cleaned_data.get('password') #retrieves password, hashed and stored in the database
            auth_login(request, user) #logs in user automatically after signing up
            return redirect('edit_account') #redirect user to add more information to othe profile
    else:
        form = UserCreationForm() #gets the default sign up form 
    return render(request, 'signup.html', {'form': form})#render html page & retrieved data and display for user

@login_required #exempts csrf token needed to display page
def edit_accountPage(request):
    form = SignUpForm(request.POST, instance=request.user) #gets the form from the forms.py file and displays it
    user_id = request.user #gets the user id of the current user
    if form.is_valid():
        existing_instance=UserProfile.objects.filter(user=request.user) #Checks if user is new

        #if user is new
        if (len(existing_instance) == 0):

            #allow customers to add age, email, skill level, address and gender
            new_instance=UserProfile(age=request.POST.get("age"),
            user=request.user, email=request.POST.get("email"),
            skill_level=request.POST.get("skill_level"),
            address=request.POST.get("address"),
            gender=request.POST.get("gender"))
            new_instance.save() #save input to database
        else:
            #allow customers to only change their age, email, skill level, address and gender
            current_instance=existing_instance[0]
            current_instance.skill_level=request.POST.get("skill_level")
            current_instance.email=request.POST.get("email")
            current_instance.gender=request.POST.get("gender")
            current_instance.address=request.POST.get("address")
            current_instance.age=request.POST.get("age")
            current_instance.save()#save input to database
        form.save() #saves form
        return redirect('/music_app/account/') #redirect user back to the account page displaying the information provided
    return render(request, 'music_app/edit_account.html', {'form' : form}) #render html page & retrieved data and display for user
