from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User

class Client(models.Model):
	name 		= models.CharField(max_length=20)
	age			= models.IntegerField(	default=1,
										validators=[MaxValueValidator(50),MinValueValidator(18)])
	fond		= models.FloatField(default=0)
	register	= models.IntegerField(default=0)
	crypto		= models.BooleanField(default=False)
	coin 		= models.CharField(	null=True,
									blank=None,
									max_length=20, 
									default='Dollar')
	valoration	= models.IntegerField(default=2)
	email		= models.EmailField(unique=True)

	owner		= models.ForeignKey(User, on_delete=models.CASCADE)

	def allofthem(self):
		mylist = [	self.name,
					self.age,
					self.fond,
					self.register,
					self.crypto,
					self.coin,
					self.valoration,
					self.email]
		return mylist

class Transaction(models.Model):
	amount		= models.FloatField(	default=1,
										validators=[MinValueValidator(50)])
	date 		= models.DateTimeField(	auto_now_add=True)
	coin		= models.CharField(		max_length=20,
										default='Dollar')

	sender_id	= models.ForeignKey(	Client,
										on_delete=models.CASCADE,
										related_name='sent_transactions')

	dest_id		= models.ForeignKey(	Client, 
										on_delete=models.CASCADE,
										related_name='received_transactions')
