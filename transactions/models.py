from django.db import models

class Client(models.Model):
	name 		= models.CharField(max_length=20)
	age			= models.IntegerField()
	fond		= models.FloatField()
	register	= models.IntegerField()
	crypto		= models.BooleanField()
	coin 		= models.CharField(max_length=20)
	valoration	= models.IntegerField()
	email		= models.EmailField(unique=True)

	def __str__(self):
		return self.name + ":"

class Transactions(models.Model):
	amount		= models.FloatField()
	date 		= models.DateTimeField(auto_now_add=True)
	sender_id	= models.ForeignKey(Client,on_delete=models.CASCADE)
	dest_id		= models.IntegerField()
