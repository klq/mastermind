from django.db import models

# Create your models here.
class tblExperiment(models.Model):
  #ExpId = models.PositiveIntegerField()
  ExpName = models.CharField(max_length=50)
  ExpCatName = models.CharField(max_length=20)
  TR = models.FloatField()
  TP = models.IntegerField()

#
#class tblSubject(models.Model):
#  SubID = models.
#  SubName =
#  SubLongName =
#  SubRealName =
#  SubEmail = models.EmailField()
#
#  SubFirstScanDate = models.DateField()
#  SubEthnicity = models.Charfield(max_length=200)
#
#
#
#
#  GENDER_CHOICES = (
#    u'M',
#    u'F')
#  SubGender = models.CharField(max_length=1,
#                               choices=GENDER_CHOICES,
#                               default='F')
#  NativeEngSpkr= models.BooleanField()
#  Glasses = models.BooleanField()
#  Meditators = models.BooleanField()
#  Musicians = models.BooleanField()
#
