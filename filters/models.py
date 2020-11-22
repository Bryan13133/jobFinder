from django.db import models
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError 

jobChoices = (('FT','Fulltime'),('PT','Part Time'),('C','Contract'),('I','Internship'),('T','Temporary'),)
dayChoices = (('1','1'),('3','3'),('5','5'),('7','7'),('14','14'))
techChoices = (('J','Java'),('C','C'),('P','Python'),('C++','C++'),('VB','Visual Basic'),('JS','Javascript'),('C#','C#'),('PH','PHP'),('SQ','SQL'),('OC','Objective-c'),('G','Go'),('SF','Swift'),('R','Ruby'))


class Filters(models.Model):
    jobDescription = models.CharField(max_length=120)
    country        = CountryField(blank=False)   
    jobType        = models.CharField(max_length=120,choices=jobChoices,blank=False) 
    category       = models.CharField(max_length=120,blank=False)
    skills         = models.CharField(max_length=120,blank=False)
    budget         = models.CharField(max_length=120,blank=False)
    daysPosted     = models.CharField(max_length=120,choices=dayChoices,blank=False)
    technology     = models.CharField(max_length=120,choices=techChoices,blank=False)

   
  