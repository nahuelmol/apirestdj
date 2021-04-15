from django.db import models

class whoever(models.Model):
	name = models.CharField(max_length = 10)
	last_name = models.CharField(max_length=10)
<<<<<<< HEAD

class Pets(models.Model):
	name = models.CharField(max_length=10)
	years_old = models.IntegerField()
	hairColor = models.CharField(max_length=10)

class Cosanew(models.Model):
	name = models.CharField(max_length=10)
	years_old = models.IntegerField()
	hairColor = models.CharField(max_length=10)
=======
       
class Customer(models.Model):
        name = models.CharField(max_length = 10)
        nation = models.CharField(max_length = 10)
        total_trans = models.IntegerField()
        partial_doubt = models.FloatField()
        average_revenue = models.FloatField()
>>>>>>> 09c12cbeb971595e7cb09aa40020a3eae11dd084
