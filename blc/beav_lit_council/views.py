from django.shortcuts import render, render_to_response

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Volunteer, Comments
from json import dumps, loads
from forms import VolunteerForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

def register(request):
	if request.method == "POST":
		User.objects.create_user(request.POST["username"], None, request.POST["password"])
	return render(request, 'register.html')


def login(request):
	if request.method == "POST":
		user = auth.authenticate(username=request.POST["username"], password=request.POST["password"])

		if user is not None:
			if user.is_active:
				print("User is valid, active and authenticated")
				return redirect('index')
			else:
				print("The password is valid, but the account has been disabled")

	return render(request, "login.html")

def index(request):
	return render_to_response('index.html')

def dom(request):
	if request.method == "POST":
		print request.POST

	return render(request, 'dom.html')

def volunteer(request):
	# Request the context of the request
	# The context contains information such as the client's machine details, for example.
	context = RequestContext(request)

	#Construct a dictionary to pass to the template engine as its context.
	#Note the key boldmessage is the same as {{ boldmessage }} in the template!
	context_dict = {'boldmessage': "Teachin' fokes to read more gooder since 500 BC"}

	volunteer_list = Volunteer.objects.all()

	context_dict['volunteers'] = volunteer_list #creates a dict with a key of volunteers

	#Return a rendered response to send to the client.
	#We make use of the shortcut function to make our lives easier.
	#Note that the first parameter is the template we wish to use.
	return render_to_response('volunteer.html', context_dict, context)

@csrf_exempt
def ajax(request):
	if request.method == "POST":
		volunteer = Volunteer()
		volunteer.first_name = request.POST['first_name']
		volunteer.save()

	volunteer_list = list(Volunteer.objects.all())
	ajax_list = []
	for item in volunteer_list:
		ajax_list.append({
			"first_name": item.first_name,
			"last_name": item.last_name,
			"email": item.email,
			})

	return HttpResponse(dumps(ajax_list), content_type="application/json")

# def comments(request):
# 	context = RequestContext(request)
# 	comments = Comments.objects
# 	return render_to_response('index.html', context_dict, context)

def about(request):
	return render_to_response('about.html')

def board_info(request):
	return render_to_response("board_info.html")

def contact(request):
	return render_to_response("contact.html")

def locations(request):
	return render_to_response("locations.html")

def tutorinfo(request):
	return render_to_response("tutorinfo.html")

def calendars(request):
	return render_to_response("calendars.html")

def schedules(request):
	return render_to_response("schedules.html")

def links(request):
	return render_to_response("links.html")

def add_volunteer(request):
	#Get the context from the request
	context = RequestContext(request)

	# A HTTP
	if request.method == "POST":
		form = VolunteerForm(request.POST)
	# Have we been provided with a valid form?
		if form.is_valid():
		#Save the new volunteer to the database
			form.save()
		#now call the volunteer() view
		#the user will be shown the volunteer page
			return volunteer(request)
		else:
			print form.errors

	else:
		# The supplied form contained errors - just print them to the terminal
		form = VolunteerForm()

	# Bad form (or form details), no form supplied...
	# Render the form with error messages (if any)
	return render_to_response('add_volunteer.html', {'form': form}, context)

