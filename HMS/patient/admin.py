from django.contrib import admin
from . models import reception,doctors,diaglogin,pharmacy,patient,medicine,diagnosis,doctor,treatment
# Register your models here.
admin.site.register(reception)
admin.site.register(doctors)
admin.site.register(diaglogin)
admin.site.register(pharmacy)
admin.site.register(patient)
admin.site.register(medicine)
admin.site.register(diagnosis)
admin.site.register(doctor)
admin.site.register(treatment)
