from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.contrib import messages
from . models import reception,doctors,diaglogin,pharmacy,patient,doctor,medicine
# from . import models
from django.core.mail import send_mail
from django.db.models import Max,Min,Avg,Sum


# Create your views here.

# def home(request):
#     return HttpResponse("<h1>hai</h1>")

def home(request):
    return render(request,'index.html')

def CheckReception(request):
    if request.method=='POST':
        user=request.POST['txt']
        pwd=request.POST['pwd']

        #admin=Admin(username=username,password=password)
        cust=reception.objects.filter(username=user, password=pwd)

     
        if cust.exists():
            recp=reception.objects.get(username=user)
            request.session['rid']=recp.id
            request.session['rname']=recp.username
            print(recp)
            return render(request,'reception-home.html',{'rname':recp})
           
        else:
            messages.info(request,'invalid credentials')
            return redirect('home')
    
def Checkdoctors(request):
    if request.method=='POST':
        user=request.POST['txt']
        pwd=request.POST['pwd']

        #admin=Admin(username=username,password=password)
        cust=doctor.objects.filter(username=user, password=pwd)

     
        if cust.exists():
            doc=doctor.objects.get(username=user)
            request.session['did']=doc.id
            request.session['dname']=doc.username
            request.session['kind']=doc.specialization
            return render(request,'doctors-home.html',{'dname':doc})
           
        else:
            messages.info(request,'invalid credentials')
            return redirect('home')
    
def Checkdiaglogin(request):
    if request.method=='POST':
        user=request.POST['txt']
        pwd=request.POST['pwd']

        #admin=Admin(username=username,password=password)
        cust=diaglogin.objects.filter(username=user, password=pwd)

     
        if cust.exists():
            recp=diaglogin.objects.get(username=user)
            print(recp)
            return render(request,'diaglogin-home.html',{'recption':recp})
           
        else:
            messages.info(request,'invalid credentials')
            return redirect('home')
    
def Checkpharmalogin(request):
    user=request.POST['txt']
    pwd=request.POST['pwd']

                #admin=Admin(username=username,password=password)
    cust=pharmacy.objects.filter(username=user, password=pwd)

            
    if cust.exists():
        recp=pharmacy.objects.get(username=user)
        return render(request,'pharmacylogin-home.html',{'recption':recp})
    else:
        messages.info(request,'invalid credentials')
        return redirect('home')
    



def Reg(request):
    return render(request,'registratation.html')
    


def Storevalues(request):
    rname=request.session['rname']
    pname=request.POST['Name']
    age=request.POST['Age']
    doa=request.POST['doa']
    diag=request.POST['diag']
    tob=request.POST['typ']
    address=request.POST['add']
    state1=request.POST['state']
    dist=request.POST['District']
    pObj=patient(patient_name=pname,age=age,doa=doa, dod='Null', diagnosis=diag,type_of_bed=tob, address=address, state1=state1,city=dist,status="Active",doccheck="UNchecked")
    pObj.save();
    return render(request,'reception-home.html',{'rname':rname})

# ===================================================================

def getdetailstoupdate(request):
    return render(request,'getdetailstoupdate.html')

def update_patient(request):
    id=request.GET.get('pt_id')
    pobj=patient.objects.filter(id=id)
    if(pobj.exists()):
        return render(request,'update_patient.html',{'p':pobj} ) 


def updating(request):
    rname=request.session['rname']
    id=request.POST['id']
    pname=request.POST['Name']
    age=request.POST['Age']
    doa=request.POST['doa']
    tob=request.POST['typ']
    address=request.POST['add']
    state1=request.POST['state']
    dist=request.POST['District']
    pobj=patient.objects.get(id=id)
    pobj.patient_name=pname
    pobj.age=age
    pobj.doa=doa
    pobj.address=address
    pobj.state1=state1
    pobj.city=dist
    pobj.save()
    messages.info(request,'Updated Successfully ')
    return render(request,'reception-home.html',{'rname':rname})

def viewallpatients(request):
    patients=patient.objects.all().order_by('id')
    if patients is not None:
        return render(request,'viewallpatients.html',{'p':patients})


def delete_form(request):
    return render(request,'getdetailstodelete.html')

def delete_patient(request):
    id=request.GET.get('pt_id')
    pobj=patient.objects.filter(id=id)
    if(pobj.exists()):
        return render(request,'delete_patient.html',{'p':pobj} ) 

def deleting(request):
    rname=request.session['rname']
    pid=request.GET.get('pt_id')
    poobj=patient.objects.filter(id=pid).delete()
    messages.info(request,'deleted Successfully ')
    return render(request,'reception-home.html',{'rname':rname})


def viewPatientForm(request):
    return render(request,'getdetailstoiew.html')

def view_patient(request):
    rname=request.session['rname']
    id=request.GET.get('pt_id')
    pobj=patient.objects.filter(id=id)
    if(pobj.exists()):
        return render(request,'view_patient.html',{'p':pobj} ) 
    else:
        messages.info(request,'No Records Found ')
        return render(request,'reception-home.html',{'rname':rname})


def billing_form(request):
    return render(request,'billingform.html')

def patient_billing(request):
    id=request.GET.get('pt_id')
    pobj=patient.objects.filter(id=id)
    if(pobj.exists()):
        return render(request,'patient_billing.html',{'p':pobj}) 

def doctorspatient(request):
    kind=request.session['kind']
    dobj=patient.objects.filter(diagnosis=kind ,doccheck ='UNchecked',status='Active')
    if dobj is not None:
        return render(request,'viewadoctorpatients.html',{'p':dobj})
    
def treatedpatient(request):
    kind=request.session['kind']
    dobj=patient.objects.filter(diagnosis=kind ,doccheck ='checked')
    if dobj is not None:
        return render(request,'treatedpatients.html',{'p':dobj})

def doccheckstatus(request):
    patientid=request.GET.get('id')
    pobj=patient.objects.get(id=patientid)
    pobj.doccheck='checked'
    pobj.save()
    return redirect('doctorspatient')


def Add_New_Medicines(request):
    return render(request,'Add_New_Medicines.html')

def store_New_Medicines(request):
    dname=request.POST['drugname']
    quantity=request.POST['quantity']
    rate=request.POST['rate']
    mfgdate=request.POST['mfgdate']
    expdate=request.POST['expdate']
    mObj=medicine(medicine_name=dname,quantity=quantity,rate=rate, mfgdate=mfgdate, expdate=expdate)
    mObj.save();
    m=medicine.objects.all().order_by('id')
    if m is not None:
        return render(request,'view_medicines.html',{'m':m})

def view_medicines(request):
    m=medicine.objects.all().order_by('id')
    return render(request,'view_medicines.html',{'m':m})

def updatemed(request):
    drugid=request.GET.get('id')
    m=medicine.objects.filter(id=drugid)
    return render(request,'update_medicines.html',{'m':m})

def update_Medicines(request):
    drugid=request.POST['id']
    dname=request.POST['drugname']
    quantity=request.POST['quantity']
    rate=request.POST['rate']
    mfgdate=request.POST['mfgdate']
    expdate=request.POST['expdate']
    mobj=medicine.objects.get(id=drugid)
    mobj.medicine_name=dname;
    mobj.quantity=quantity
    mobj.rate=rate
    mobj.mfgdate=mfgdate
    mobj.expdate=expdate
    mobj.save()
    return redirect('view_medicines')


   
def getdetailsforpharmacy(request):
    return render(request,'getdetailsforpharmacy.html')



def pharmacy_patient(request):
    id=request.GET.get('pt_id')
    pobj=patient.objects.filter(id=id,status ='Active')
    if(pobj.exists()):
        return render(request,'pharmacypatientdetails.html',{'p':pobj} ) 



def issue_medicine_form(request):
    id=0
    id=request.GET['pt_id']
    mobj=medicine.objects.all()
    return render(request,'medicine_form1.html',{'id':id,'m':mobj})

def IssueMedicines(request):
    pass



