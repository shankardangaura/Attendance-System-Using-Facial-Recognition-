from django.db import models
from django.contrib.auth.models import User

import datetime
# Create your models here.
	

class Present(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date = models.DateField(default=datetime.date.today)
	present=models.BooleanField(default=False)

	def __str__(self) -> str:
		status = "Absent"
		if self.present:
			status = "Present"
		return f"{self.user} => {status} on {self.date}"
	
	
class Time(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date = models.DateField(default=datetime.date.today)
	time=models.DateTimeField(null=True,blank=True)
	out=models.BooleanField(default=False)

	def __str__(self) -> str:
		status = "Not Out"
		if self.out:
			status = "Out"
		return f"{self.user} => {status} on {self.date} and {self.time}"
	

