"""
tb_example models.
"""
from django.db.models import fields
from opal.core.fields import ForeignKeyOrFreeText

from opal import models

class Demographics(models.Demographics): pass
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment): pass
class Investigation(models.Investigation): pass
class SymptomComplex(models.Investigation): pass
class PatientConsultation(models.Investigation): pass


class Contact(models.PatientSubrecord):
    surname = fields.CharField(max_length=255, blank=True)
    first_name = fields.CharField(max_length=255, blank=True)
    title = ForeignKeyOrFreeText(models.Title)
    telephone_number = fields.CharField(max_length=255)
    date_of_birth = fields.DateField(null=True, blank=True)
    address = fields.TextField(blank=True, null=True)
