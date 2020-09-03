from django .urls import path
from . import views

urlpatterns = [

    #path for validating page

     path('',views.home,name='home'),
     path('CheckReception',views.CheckReception, name='CheckReception'),
     path('registration',views.Reg,name="patientreg"),
     path('getdetailstoupdate',views.getdetailstoupdate,name="taking no to update"),
     path('Storevalues',views.Storevalues,name="Regstration"),
     path('update_patient',views.update_patient,name="update_patient"),
     path('delete_patient',views.delete_patient,name=" delete_patient"),
     path('delete_form',views.delete_form,name="delete_form"),
     path('updating',views.updating,name="updating"),
     path('viewallpatients',views.viewallpatients,name="viewallpatients"),
     path('deleting',views.deleting,name="deleting"),
     path('viewPatientForm',views.viewPatientForm,name="viewPatientForm"),
     path('view_patient',views.view_patient,name="view_patient"),
     path('CheckDoctor',views.Checkdoctors, name='Checkd'),
     path('CheckDiagnostics',views.Checkdiaglogin, name='Checkdiagl'),
     path('CheckPharmacy',views.Checkpharmalogin, name='Checkpl'),
     path('Storevalues',views.Storevalues,name="storingintobatabase"),
     path('billing_form',views.billing_form,name="billing_form"),
     path('patient_billing',views.patient_billing,name="patient_billing"),
     path('doctorspatient',views.doctorspatient,name="doctorspatient"), 
     path('treatedpatient',views.treatedpatient,name="treatedpatient"),
    path('doccheckstatus',views.doccheckstatus,name="doccheckstatus"),
     path('Add_New_Medicines',views.Add_New_Medicines,name="Add_New_Medicines"),
     path('store_New_Medicines',views.store_New_Medicines,name="store_New_Medicines"),
      path('view_medicines',views.view_medicines,name="view_medicines"),
       path('updatemed',views.updatemed,name="updatemed"),
       path('update_Medicines',views.update_Medicines,name="update_Medicines"),
      path('getdetailsforpharmacy',views.getdetailsforpharmacy,name="taking no to update Pharmacy"),
      path('pharmacy_patient',views.pharmacy_patient,name="pharmacy_patient"),
      path('issue_medicine_form',views.issue_medicine_form,name="issue_medicine_form"),
       path('IssueMedicines',views.IssueMedicines,name="IssueMedicines"),
      





]