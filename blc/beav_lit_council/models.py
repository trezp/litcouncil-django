from django.db import models

class ContactPref(models.Model):
	short_name = models.CharField(max_length=2, blank=True, null=True)
	display_name = models.CharField(max_length=200, blank=True, null=True)
	# PHONE = "PH"
	# EMAIL = "EM"
	# POSTAL_MAIL = "PM"
	# CONTACT_PREFERENCE_CHOICES = (
	# 	(PHONE, 'PHONE'),
	# 	(EMAIL, 'EMAIL'),
	# 	(POSTAL_MAIL, 'POSTAL MAIL'),
	# )
	# contact_preferences = models.Charfield(max_length=2,
	# 									   choices=CONTACT_PREFERENCE_CHOICES,
	# 									   default=PHONE)
	def __unicode__(self):
		return self.display_name

class Volunteer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	#phone = #install django-phonenumber-field
	contact_pref = models.ForeignKey(ContactPref, blank=True, null=True)

	def __unicode__(self):
		return self.first_name + " " + self.last_name

class Comments(models.Model):
	title = models.CharField(max_length=100, default="")
	announcement = models.TextField(default="")