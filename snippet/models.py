from django.db import models

## Data enable to apirest service

class Friends(models.Model):
	name 		= models.CharField(max_length = 10)
	last_name 	= models.CharField(max_length=10)

class Languages(models.Model):
	name 				= models.CharField(max_length=15)
	learning_time 		= models.FloatField()
	time_to_manage 		= models.FloatField()
	amount_ofcountries 	= models.IntegerField()

class CountriesSpeakers(models.Model):
	country 		= models.CharField(max_length=15)
	first_language 	= models.CharField(max_length=10)
	second_language = models.CharField(max_length=10) 

## Data for a database treat

class Pets(models.Model):
	name 		= models.CharField(max_length=10)
	years_old 	= models.IntegerField()
	hairColor 	= models.CharField(max_length=10)

class Customers(models.Model):
    name 			= models.CharField(max_length = 10)
    nation 			= models.CharField(max_length = 10)
    total_trans 	= models.IntegerField()
    partial_doubt 	= models.FloatField()
    average_revenue = models.FloatField()
