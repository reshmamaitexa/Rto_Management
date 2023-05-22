from django.shortcuts import render,redirect
from Rtomanagement.models import rtouser,Learners,licence,Vehi_Reg,NOC,Hazmate,Ownership_transfer,Payment,International_dl,Test_date,PSV_Badge,Adhaar
from django.contrib import messages

# Create your views here.


def get_users(request):
    data=rtouser.objects.all()
    return render(request,'table-data-users.html',{'data':data})

def Viewadhardetails(request):
     data=Adhaar.objects.all()
     return render(request,'table-view-adhar.html',{'data':data})

def Addadhardetails(request):
     return render(request,'table-add-adhar.html')

def approveuser(request, cr_id):     
        cr = rtouser.objects.get(id=cr_id)
        cr.user_status =  1  
        cr.save()
        return redirect('getusers')

def rejectuser(request,cr_id):
     item =rtouser.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('getusers')   

def rejectUserWithReson(request,cr_id):
     rejected_reason= request.POST.get('rejected_reason') 
     item =rtouser.objects.get(id=cr_id) 
     item.user_status = 2
     item.rejected_reason = rejected_reason
     item.save()
     return redirect('getusers')   

def admin_dashboard(request):
    return render(request,'dashboard.html')


def manage_learners_license(request):
    data=Learners.objects.all().values()
    print("data==========>",data)
    return render (request,'table-data-learners.html',{'data':data})


def approvelearners(request, cr_id):     
        cr = Learners.objects.filter(user_id=cr_id).values()
        print("crrrrrrrrrrrrrrr===========>",cr)
        for i in cr:
             id=i['id']
             First_Name=i['First_Name']
             user_id = i['user_id_id']
             Licence_type=i['Licence_type']

             context = {
                  'id':id,
                  'First_Name':First_Name,
                  'user_id':user_id,
                  'Licence_type':Licence_type
             }

        # cr.learners_status =  1  
        # cr.save()
        # return redirect('managelearnerslicense')
        return render (request,'add-test-date.html',context)

def submitLearnersTestDateAndLocation(request,cr_id):
     test_date= request.POST.get('test_date') 
     test_location= request.POST.get('test_location') 
     First_Name= request.POST.get('First_Name') 
     Last_Name= request.POST.get('Last_Name') 
     Phone_no= request.POST.get('Phone_no') 

     adhar_data = Adhaar.objects.filter(First_Name=First_Name).filter(Last_Name=Last_Name).filter(Mobile=Phone_no).values()

     print("adhar_data=========>",adhar_data)
     if(adhar_data):
          print("ddd")
          cr = Learners.objects.get(id=cr_id) 
          cr.learners_status =  1  
          cr.test_date = test_date
          cr.test_location = test_location
          cr.verified_with_adhar = 1
          cr.save()
          return redirect('managelearnerslicense')
     else:
          return redirect('managelearnerslicense')

        

def rejectlearners(request,cr_id):
     item =Learners.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('managelearnerslicense')
   
def rejectlearnersWithReason(request,cr_id):
     rejected_reason= request.POST.get('rejected_reason') 
     item =Learners.objects.get(id=cr_id) 
     item.learners_status = 2
     item.rejected_reason = rejected_reason
     item.save()
    #  item.delete()
    #  messages.info(request,'Rejected')
     return redirect('managelearnerslicense')   

def manage_license(request):
    data=licence.objects.all()
    return render (request,'table-data-licence.html',{'data':data})


def approvelicense(request, cr_id):     
        cr = licence.objects.get(user_id=cr_id)
        cr.licence_status =  1  
        cr.save()
        return redirect('managelicense')


def submitLicenceTestDateAndLocation(request,cr_id):
     test_date= request.POST.get('test_date') 
     test_location= request.POST.get('test_location') 
     First_Name= request.POST.get('First_Name') 
     Last_Name= request.POST.get('Last_Name') 
     Phone_no= request.POST.get('Phone_no')

     adhar_data = Adhaar.objects.filter(First_Name=First_Name).filter(Last_Name=Last_Name).filter(Mobile=Phone_no).values()

     print("adhar_data=========>",adhar_data)
     if(adhar_data):
        cr = licence.objects.get(id=cr_id)
        print("cr=============>",cr)
        cr.licence_status =  1  
        cr.test_date = test_date
        cr.test_location = test_location
        cr.verified_with_adhar = 1
        cr.save()
        return redirect('managelicense')
     else:
          return redirect('managelicense')

def rejectlicence(request,cr_id):
     item =licence.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('managelicense')   

def rejectlicenseWithReason(request,cr_id):
     rejected_reason= request.POST.get('rejected_reason') 
     item =licence.objects.get(id=cr_id) 
     item.licence_status = 4
     item.rejected_reason = rejected_reason
     item.save()
    #  item.delete()
    #  messages.info(request,'Rejected')
     return redirect('managelicense')   


def manage_renew_license(request):
    data=licence.objects.all()
    return render (request,'table-data-renewlicence.html',{'data':data})

def approverenewlicense(request, cr_id): 
            
        # cr = licence.objects.get(user_id=cr_id)
        # cr.licence_status =  1  
        # cr.save()
        new_date= request.POST.get('new_date') 
        print("datas===>",new_date,cr_id)
        return redirect('managerenewlicense')

def submitNewDate(request,cr_id):
     new_date= request.POST.get('new_date') 
     print("datas===>",new_date,cr_id)
     cr = licence.objects.get(id=cr_id)
     cr.licence_status =  1 
     cr.new_date = new_date 
     cr.save()
     return redirect('managerenewlicense')

def rejectrenewlicence(request,cr_id):
     item =licence.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('managerenewlicense')  


def rejectrenewlicenseWithReason(request,cr_id):
     rejected_reason= request.POST.get('rejected_reason') 
     item =licence.objects.get(id=cr_id) 
     item.licence_status = 5
     item.renew_rejected_reason = rejected_reason
     item.save()
    #  item.delete()
    #  messages.info(request,'Rejected')
     return redirect('managerenewlicense')   


def manage_duplicate_license(request):
    data=licence.objects.all()
    return render (request,'table-data-duplicate.html',{'data':data})


def approveduplicatelicense(request, cr_id):     
        cr = licence.objects.get(id=cr_id)
        cr.licence_status =  1  
        cr.save()
        return redirect('manageduplicatelicense')

def rejectduplicatelicence(request,cr_id):
     item =licence.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('manageduplicatelicense')   


def rejectduplicatelicenseWithReason(request,cr_id):
     rejected_reason= request.POST.get('rejected_reason') 
     item =licence.objects.get(id=cr_id) 
     item.licence_status = 6
     item.duplicated_rejected_reason = rejected_reason
     item.save()
    #  item.delete()
    #  messages.info(request,'Rejected')
     return redirect('manageduplicatelicense')   



def manage_hazmate(request):
    data=Hazmate.objects.all()
    return render (request,'table-data-hazmate.html',{'data':data})


def approvehazmate(request, cr_id):     
        cr = Hazmate.objects.get(id=cr_id)
        cr.hazmate_status =  1  
        cr.save()
        return redirect('managehazmate')

def submitHazmateTestDateAndLocation(request,cr_id):
     test_date= request.POST.get('test_date') 
     test_location= request.POST.get('test_location') 
     First_Name= request.POST.get('First_Name') 
     Last_Name= request.POST.get('Last_Name') 
     Phone_no= request.POST.get('Phone_no')

     adhar_data = Adhaar.objects.filter(First_Name=First_Name).filter(Last_Name=Last_Name).filter(Mobile=Phone_no).values()

     print("adhar_data=========>",adhar_data)
     if(adhar_data):
        cr = Hazmate.objects.get(id=cr_id)
        print("cr=============>",cr)
        cr.hazmate_status =  1  
        cr.test_date = test_date
        cr.test_location = test_location
        cr.verified_with_adhar = 1
        cr.save()
        return redirect('managehazmate')
     else:
          return redirect('managehazmate')

def rejecthazmate(request,cr_id):
     item =Hazmate.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('managehazmate') 


def rejecthazmateWithReason(request,cr_id):
     rejected_reason= request.POST.get('rejected_reason') 
     item =Hazmate.objects.get(id=cr_id) 
     item.hazmate_status = 2
     item.rejected_reason = rejected_reason
     item.save()
    #  item.delete()
    #  messages.info(request,'Rejected')
     return redirect('managehazmate') 


def manage_international_license(request):
    data=International_dl.objects.all()
    return render (request,'table-data-international_licence.html',{'data':data})


def approveinternationalLicence(request, cr_id):     
        cr = International_dl.objects.get(id=cr_id)
        cr.inter_dl_status =  1  
        cr.save()
        return redirect('manageinternationallicense')

def rejectinternationalLicence(request,cr_id):
     item =International_dl.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('manageinternationallicense')


def rejectinternationalLicenceWithReason(request,cr_id):
     rejected_reason= request.POST.get('rejected_reason')
     item =International_dl.objects.get(id=cr_id) 
     item.inter_dl_status = 2
     item.rejected_reason = rejected_reason
     item.save()
    #  item.delete()
    #  messages.info(request,'Rejected')
     return redirect('manageinternationallicense') 

def manage_psvBadge(request):
    data=PSV_Badge.objects.all()
    return render (request,'table-data-psv.html',{'data':data})

def approvepsv(request, cr_id):     
        cr = PSV_Badge.objects.get(id=cr_id)
        cr.psv_status =  1  
        cr.save()
        return redirect('managepsvBadge')

def rejectpsv(request,cr_id):
     item =PSV_Badge.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('managepsvBadge') 


def rejectPsvWithReason(request,cr_id):
     rejected_reason= request.POST.get('rejected_reason') 
     item =PSV_Badge.objects.get(id=cr_id) 
     item.psv_status = 2
     item.rejected_reason = rejected_reason
     item.save()
    #  item.delete()
    #  messages.info(request,'Rejected')
     return redirect('managepsvBadge') 


def manage_noc(request):
    data=NOC.objects.all()
    return render (request,'table-data-noc.html',{'data':data})

def approvenoc(request, cr_id):     
        cr = NOC.objects.get(id=cr_id)
        cr.noc_status =  1  
        cr.save()
        return redirect('managenoc')

def rejectnoc(request,cr_id):
     rejected_reason= request.POST.get('rejected_reason') 
     item =NOC.objects.get(id=cr_id) 
     item.noc_status =  2  
     item.rejected_reason = rejected_reason
     item.save()
     messages.info(request,'Rejected')
     return redirect('managenoc')   


def manage_noc_cancellation(request):
    data=NOC.objects.all()
    return render (request,'table-data-cancelnoc.html',{'data':data})

def new_vehicle_register(request):
    data=Vehi_Reg.objects.all()
    return render (request,'table-data-vehicle_reg.html',{'data':data})

def vehicle_ownership_status(request):
    data=Ownership_transfer.objects.all()
    return render (request,'table-data-ownership_transfer.html',{'data':data})


def approvevehicleregister(request, cr_id):     
        cr = Vehi_Reg.objects.get(id=cr_id)
        cr.vehi_reg_status =  1  
        cr.save()
        return redirect('newvehicleregister')


def rejectvehicleRegWithReason(request, cr_id):  
        rejected_reason= request.POST.get('rejected_reason')    
        cr = Vehi_Reg.objects.get(id=cr_id)
        cr.vehi_reg_status =  2  
        cr.rejected_reason = rejected_reason
        cr.save()
        return redirect('newvehicleregister')

def approveownership(request, cr_id):     
        cr = Ownership_transfer.objects.get(id=cr_id)
        cr.vehi_newreg_status =  1  
        cr.save()
        return redirect('vehicleownershipstatus')


def rejectOwnershipWithReason(request, cr_id):
        rejected_reason= request.POST.get('rejected_reason')       
        cr = Ownership_transfer.objects.get(id=cr_id)
        cr.vehi_newreg_status =  2  
        cr.rejected_reason = rejected_reason
        cr.save()
        return redirect('vehicleownershipstatus')

def rejectownership(request,cr_id):
     item =Ownership_transfer.objects.get(id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('vehicleownershipstatus')  
 

def update_license_data(request):
    return render (request,'table-data-update_dl.html')


def test_date(request):
    return render (request,'table-data-add_testdate.html')


def view_payment(request):
    data = Payment.objects.all()
    return render (request,'table-data-payment.html',{'data':data})


def approvepayment(request, cr_id):     
        cr = Payment.objects.get(userreg_id=cr_id)
        cr.payment_status =  1  
        cr.save()
        return redirect('viewpayment')


def rejectpayment(request,cr_id):
     item =Payment.objects.get(userreg_id=cr_id) 
     item.delete()
     messages.info(request,'Rejected')
     return redirect('viewpayment')


def view_report(request):
    return render (request,'table-data-report.html')


def view_test_date(request):
     data=Test_date.objects.all()
     return render (request,'table-data-view-testdate.html',{'data':data})


def create_test_date(request):
     if request.method == 'POST':
        fullname= request.POST.get('fullname') 
        Licence_type= request.POST.get('Licence_type') 
        date= request.POST.get('date')
        user_id= request.POST.get('user_id')
        id= request.POST.get('id')



        data = Test_date(Test_date=date,user_id=user_id,name=fullname,Licence_type=Licence_type,test_status=0)
        data.save()
        cr = Learners.objects.get(user_id=id)

        cr.learners_status =  '1'  
        cr.save()
        return redirect('viewtestdate')
     
def AddFormAdharDetails(request):
     if request.method == 'POST':
          First_Name= request.POST.get('First_Name') 
          Last_Name= request.POST.get('Last_Name') 
          SDW= request.POST.get('SDW') 
          House_name= request.POST.get('House_name') 
          Post= request.POST.get('Post') 
          Pin= request.POST.get('Pin') 
          City= request.POST.get('City') 
          Mobile= request.POST.get('Mobile') 
          Date_of_birth= request.POST.get('Date_of_birth') 
          Photo= request.POST.get('Photo') 
          data = Adhaar(First_Name=First_Name,Last_Name=Last_Name,SDW=SDW,House_name=House_name,Post=Post,Pin=Pin,City=City,Mobile=Mobile,Date_of_birth=Date_of_birth,Photo=Photo,adhaar_status=0)
          data.save()
          return redirect(Viewadhardetails)