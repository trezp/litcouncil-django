from django.shortcuts import render, render_to_response

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Volunteer

def index(request):
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
	return render_to_response('index.html', context_dict, context)

def volunteer(request):
	context = RequestContext(request)
	# context_dict = {
	# 	'firstname': first_name.objects.all(),
	# 	'lastname': last_name.objects.all(),
	# 	'email': email.objects.all(),
	# 	'contactpref': contact_pref.objects.all(),
	# }
	context_dict = {}
	volunteer_list = Volunteer.objects.all()

	context_dict['volunteers'] = volunteer_list #creates a dict with a key of volunteers
	return render_to_response('index.html', context_dict, context)

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

def volunteer(request):
	return render_to_response("volunteer.html")

def calendars(request):
	return render_to_response("calendars.html")

def schedules(request):
	return render_to_response("schedules.html")

def links(request):
	return render_to_response("links.html")


