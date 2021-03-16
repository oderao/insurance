from django.db import models
from datetime import datetime
# Create your models here.


class RiskName(models.Model):

	#client creates the risk type they want
    name = models.CharField(max_length=100,)

    def __str__(self):
        return str(self.name)

class RiskDetails(models.Model):
 	"""Table containing details of risk"""
 	#contains details of Risktype

 	duration = [
 		("","Select Duration"),
        ('ONE MONTH', 'ONE MONTH'),
        ('THREE MONTHS', 'THREE MONTHS'),
        ('SIX MONTHS', 'SIX MONTHS'),
        ('A YEAR', 'A YEAR'),
    ]

 	risk_name = models.ForeignKey('RiskName',on_delete=models.CASCADE,)
 	risk_duration = models.CharField(choices=duration,max_length=100)
 	risk_id = models.AutoField(primary_key=True)
 	risk_amount = models.IntegerField()
 	risk_active_date = models.DateField() #date when insurance policy become active

 	def __str__(self):
 		return str(self.risk_name )+ "-" + str(self.risk_id)

class Declarations(models.Model):
	"""Table containing data for related party for the risk"""
	
	parties = [
			('Individual', 'Individual'),
			('Company','Company')
		]	

	party_type = models.CharField(choices=parties,max_length=60)
	party_name = models.CharField(max_length=70)
	party_address = models.TextField(blank=True,help_text='Enter Home/Office Address')
	party_agent = models.TextField(blank=True,help_text='Enter Name of Agent')

	def __str__(self):
		return self.party_name


class Coverage(models.Model):
	""" Enter Specific Coverage Information"""

	coverage_for = models.ForeignKey('RiskName',on_delete=models.CASCADE)
	coverage_description = models.TextField()
	coverage_limit = models.PositiveIntegerField()
	coverage_premium = models.PositiveIntegerField()




