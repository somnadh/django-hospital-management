from django.db import models

# Create your models here.
class reception(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username


class doctors(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.username

class diaglogin(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.username

class pharmacy(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.username



class patient(models.Model):
    patient_name=models.CharField(max_length=50)
    age=models.IntegerField()
    doa=models.CharField(max_length=50)
    dod=models.CharField(max_length=20)
    diagnosis=models.CharField(max_length=10)
    type_of_bed=models.CharField(max_length=50)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=150)
    state1=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    doccheck=models.CharField(max_length=150)


    def __str__(self):
        return self.patient_name

class medicine(models.Model):
    medicine_name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    rate=models.IntegerField()
    mfgdate=models.CharField(max_length=50)
    expdate=models.CharField(max_length=50)
    def __str__(self):
        return self.medicine_name

class diagnosis(models.Model):
    diag_name=models.CharField(max_length=50)
    rate=models.IntegerField()
    def __str__(self):
        return self.diag_name

class tracking_diagnostics(models.Model):
    patient_id=models.ForeignKey(patient, on_delete=models.CASCADE)
    diag_id=models.ForeignKey(diagnosis, on_delete=models.CASCADE)

class tracking_medicines(models.Model):
    patient_id=models.ForeignKey(patient, on_delete=models.CASCADE)
    medi_id=models.ForeignKey(medicine, on_delete=models.CASCADE)

class cart(models.Model):
    patient_id=models.ForeignKey(patient, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    rate= models.IntegerField()


class doctor(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    def __str__(self):
        return self.username


class treatment(models.Model):
    patient_id=models.ForeignKey(patient, on_delete=models.CASCADE)
    doc_id=models.ForeignKey(doctor, on_delete=models.CASCADE)
    prescription=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default='unchecked')


