from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .models import Login,rtouser,Learners,licence,Vehi_Reg,NOC,Ownership_transfer,Payment,Test_date,Hazmate,PSV_Badge,International_dl,Adhaar
from Rtomanagement.serializers import UserRegisterSerializer,LoginUsersSerializer,LearnersSerializer,licenceSerializer,Vehi_RegSerializer,NOCSerializer,Ownership_transferSerializer,Test_dateSerializer,PaymentSerializer,HazmateSerializer,PSV_BadgeSerializer,International_dlSerializer,AdhaarSerializer


# Create your views here.
class UserRegisterAPIView(GenericAPIView): 
    serializer_class = UserRegisterSerializer 
    serializer_class_login = LoginUsersSerializer

    def post(self, request):

        login_id= ' ' 
        First_Name= request.data.get('First_Name')
        Last_Name= request.data.get('Last_Name')
        Gender = request.data.get('Gender')
        House_name = request.data.get("House_name")
        Post =request.data.get('Post')
        Pin= request.data.get("Pin")
        City = request.data.get('City') 
        Date_of_birth = request.data.get("Date_of_birth")
        Email_address = request.data.get("Email_address") 
        Phone_no = request.data.get("Phone_no")
        username= request.data.get("username")
        password = request.data.get("password")
        

        role ='rtouser'
        userstatus = '0'


        if (Login.objects.filter(username=username)):
            return Response({'message':'Duplicate Username Found!'},status= status.HTTP_400_BAD_REQUEST)
        else:
            serializer_login= self.serializer_class_login(data={'username':username,'password':password,'role':role})

        if serializer_login.is_valid():
            log=serializer_login.save()
            login_id=log.id
            print(login_id)
        serializer = self.serializer_class(data ={'First_Name': First_Name,'Last_Name': Last_Name,'Gender':Gender,'House_name':House_name,'Post':Post,'Pin':Pin,'City':City,'Date_of_birth':Date_of_birth,'Email_address':Email_address,'Phone_no':Phone_no,'login_id':login_id,'user_status':userstatus,'role':role})
        print(serializer)


        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({"data": serializer.data, 'message': 'user registered successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)





##################LOGIN

class LoginUsersAPIView(GenericAPIView):

    serializer_class = LoginUsersSerializer
    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')

        logreg = Login.objects.filter(username= username, password=password)


        if (logreg.count()>0):
            read_serializer = LoginUsersSerializer(logreg, many=True)
            for i in read_serializer.data:
                id = i['id']
                print(id)
                role = i['role']
                regdata=rtouser.objects.all().filter(login_id=id).values()
                print(regdata)
                for i in regdata:
                     u_id = i['id']
                     l_status = i['user_status']
                     print(l_status)
                     print(u_id)
            return Response({'data':{'login_id':id,'username':username,'password':password,'role':role,'user_id':u_id,'user_status':l_status}, 'success': True, 'message':'Logged in successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'data': 'username or password is invalid', 'success': False,} , status= status.HTTP_400_BAD_REQUEST)



class GetSingleUserDetails(GenericAPIView):
    serializer_class = UserRegisterSerializer
    def get(self,request,id):
        query = rtouser.objects.get(login_id=id)
        print(query)
        serializer =UserRegisterSerializer(query)
        return Response({'data': serializer.data, 'message':'user details fetched successfully', 'success':True}, status=status.HTTP_200_OK)


class UpdateUserDetails(GenericAPIView):
    serializer_class = UserRegisterSerializer
    def put(self, request, id):
        queryset = rtouser.objects.get(login_id=id)
        print(queryset)
        serializer = UserRegisterSerializer(instance=queryset, data=request.data, partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'user updated successfully', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':[],'message':'something went wrong', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
        
    
##################################
class LearnerslicenceAPIView(GenericAPIView): 
    serializer_class = LearnersSerializer 
    def post(self, request):
        user_id=request.data.get('user_id')
        First_Name= request.data.get('First_Name')
        Last_Name= request.data.get('Last_Name')
        House_name = request.data.get("House_name")
        Post =request.data.get('Post')
        Pin= request.data.get("Pin")
        City = request.data.get('City') 
        Date_of_birth = request.data.get("Date_of_birth")
        Email_address = request.data.get("Email_address") 
        Phone_no = request.data.get("Phone_no")
        Gender = request.data.get("Gender")
        Blood_group = request.data.get("Blood_group")
        photo = request.data.get("photo")
        Licence_type = request.data.get("Licence_type")
        



        role ='Learners'
        learners_status = '0'
        verified_with_adhar = '0'


        
        serializer = self.serializer_class(data ={'user_id':user_id,'First_Name': First_Name,'Last_Name': Last_Name,'House_name':House_name,'Post':Post,'Pin':Pin,'City':City,'Date_of_birth':Date_of_birth,'Email_address':Email_address,'Phone_no':Phone_no,'Gender':Gender,'Blood_group':Blood_group,'photo':photo,'Licence_type':Licence_type,'learners_status':learners_status,'verified_with_adhar':verified_with_adhar})
        print(serializer)


        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({"data": serializer.data, 'message': 'Learners applied successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
    

class getIndividualLearnersLicence(GenericAPIView):
    serializer_class = LearnersSerializer 
    def get(self,request,id):
        queryset = Learners.objects.all().filter(user_id=id).values()
        return Response({'data': queryset, 'message':' Learners data fetched', 'success':True}, status=status.HTTP_200_OK)
    


class LicenceoriginalAPIView(GenericAPIView): 
    serializer_class = licenceSerializer 

    def post(self, request):
        learners_id=request.data.get('learners_id')
        user_id=request.data.get('user_id')
        First_Name= request.data.get('First_Name')
        Last_Name= request.data.get('Last_Name')
        Gender= request.data.get('Gender')
        House_name = request.data.get("House_name")
        Post =request.data.get('Post')
        Pin= request.data.get("Pin")
        City = request.data.get('City') 
        Date_of_birth = request.data.get("Date_of_birth")
        Email_address = request.data.get("Email_address") 
        Phone_no = request.data.get("Phone_no")
        Blood_group = request.data.get("Blood_group")
        photo = request.data.get("photo")
        Date_of_issue = request.data.get("Date_of_issue")
        Reason_for_not_renew = request.data.get("Reason_for_not_renew")
        Reason_for_apply_duplicate = request.data.get("Reason_for_apply_duplicate")

    
        role ='licence'
        licence_status = '0'
        verified_with_adhar = '0'


        
        serializer = self.serializer_class(data ={'user_id':user_id,'learners_id':learners_id,'First_Name': First_Name,'Last_Name': Last_Name,'Gender':Gender,'House_name':House_name,'Post':Post,'Pin':Pin,'City':City,'Date_of_birth':Date_of_birth,'Email_address':Email_address,'Phone_no':Phone_no,'Gender':Gender,'Blood_group':Blood_group,'photo':photo,'Date_of_issue':Date_of_issue,'Reason_for_not_renew':Reason_for_not_renew,'Reason_for_apply_duplicate':Reason_for_apply_duplicate,'licence_status':licence_status,'verified_with_adhar':verified_with_adhar})
        print(serializer)


        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({"data": serializer.data, 'message': 'License Applied successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)



class getIndividualLicences(GenericAPIView):
    serializer_class = licenceSerializer 
    def get(self,request,id):
        queryset = licence.objects.all().filter(user_id=id).values()
        return Response({'data': queryset, 'message':' license data fetched', 'success':True}, status=status.HTTP_200_OK)
    


class updateIndividualLicences(GenericAPIView):
    serializer_class = licenceSerializer 
    def put(self,request,id):
        queryset = licence.objects.get(user_id=id)
        serializer = licenceSerializer(instance=queryset, data=request.data, partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data, 'message':'updated successfully', 'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'data':'Something Went Wrong', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


class Vehi_RegAPIView(GenericAPIView): 
    serializer_class = Vehi_RegSerializer 
    def post(self, request):
        Owner_Name= request.data.get('Owner_Name')
        user_id= request.data.get('user_id') 
        SDW= request.data.get('SDW')
        Gender = request.data.get("Gender")
        House_name = request.data.get("House_name")
        Post =request.data.get('Post')
        Pin= request.data.get("Pin")
        City = request.data.get('City') 
        Ownership_type =request.data.get('Ownership_type')
        Mobile= request.data.get("Mobile")
        Class_of_vehicle = request.data.get('Class_of_vehicle') 
        Motor_vehicle_type = request.data.get("Motor_vehicle_type")
        Type_of_body = request.data.get("Type_of_body") 
        Type_of_vehicle = request.data.get("Type_of_vehicle")
        Date_of_manufacture = request.data.get("Date_of_manufacture")
        Date_of_issue =request.data.get('Date_of_issue')
        Horse_power= request.data.get("Horse_power")
        Cubic_capacity = request.data.get('Cubic_capacity') 
        Seating_capacity = request.data.get("Seating_capacity")
        Fuel_used_in_engine = request.data.get("Fuel_used_in_engine") 
        Engine_no = request.data.get("Engine_no")
        Color = request.data.get("Color")
        Vehi_photo = request.data.get("Vehi_photo")
       
        role ='Vehi_Reg'
        vehi_reg_status = '0'

        serializer = self.serializer_class(data ={"user_id":user_id,'Owner_Name': Owner_Name,'SDW':SDW,'Gender':Gender,'House_name':House_name,'Post':Post,'Pin':Pin,'City':City,'Ownership_type':Ownership_type,'Mobile':Mobile,'Class_of_vehicle':Class_of_vehicle,'Motor_vehicle_type':Motor_vehicle_type,'Type_of_body':Type_of_body,'Type_of_vehicle':Type_of_vehicle,'Date_of_manufacture':Date_of_manufacture,'Date_of_issue':Date_of_issue,'Horse_power':Horse_power,'Cubic_capacity':Cubic_capacity,'Seating_capacity':Seating_capacity,'Fuel_used_in_engine':Fuel_used_in_engine,'Engine_no':Engine_no,'Color':Color,'Vehi_photo':Vehi_photo,'vehi_reg_status':vehi_reg_status})
        print(serializer)


        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({"data": serializer.data, 'message': 'Vehicle Registered successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
    


class getIndividualVehicleRegister(GenericAPIView):
    serializer_class = Vehi_RegSerializer 
    def get(self,request,id):
        queryset = Vehi_Reg.objects.all().filter(user_id=id).values()
        return Response({'data': queryset, 'message':' vehicle registration data fetched', 'success':True}, status=status.HTTP_200_OK)



class NocAPIView(GenericAPIView): 
    serializer_class = NOCSerializer 
   
    def post(self, request):
        Registration_id=request.data.get('Registration_id')
        user_id=request.data.get('user_id')
        First_Name= request.data.get('First_Name')
        Last_Name= request.data.get('Last_Name')
        SDW= request.data.get('SDW')
        Phone_no = request.data.get("Phone_no")
        Reg_of_vehicle =request.data.get('Reg_of_vehicle')
        Class_of_vehicle= request.data.get("Class_of_vehicle")
        Engine_no = request.data.get('Engine_no') 
        Period_of_stay_in_state = request.data.get("Period_of_stay_in_state")
        Tax_pending_details = request.data.get("Tax_pending_details") 
        Vehi_photo = request.data.get("Vehi_photo")
        sign = request.data.get("sign")
       
        role ='NOC'
        noc_status = '0'


        
        serializer = self.serializer_class(data ={"user_id":user_id,'Registration_id':Registration_id,'First_Name': First_Name,'Last_Name': Last_Name,'SDW':SDW,'Phone_no':Phone_no,'Reg_of_vehicle':Reg_of_vehicle,'Class_of_vehicle':Class_of_vehicle,'Engine_no':Engine_no,'Period_of_stay_in_state':Period_of_stay_in_state,'Tax_pending_details':Tax_pending_details,'Vehi_photo':Vehi_photo,'sign':sign,'noc_status':noc_status})
        print(serializer)


        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({"data": serializer.data, 'message': 'NOC Applied successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
    

class getIndividualNOC(GenericAPIView):
    serializer_class = NOCSerializer 
    def get(self,request,id):
        queryset = NOC.objects.all().filter(user_id=id).values()
        return Response({'data': queryset, 'message':' NOC data fetched', 'success':True}, status=status.HTTP_200_OK)
    



class Ownership_transferAPIView(GenericAPIView): 
    serializer_class = Ownership_transferSerializer 
   

    def post(self, request):
        Registration_id=request.data.get('Registration_id')
        user_id=request.data.get('user_id')
        Owner_Name= request.data.get('Owner_Name')
        SDW= request.data.get('SDW')
        Gender = request.data.get("Gender")
        House_name = request.data.get("House_name")
        Post =request.data.get('Post')
        Pin= request.data.get("Pin")
        City = request.data.get('City') 
        Ownership_type =request.data.get('Ownership_type')
        Mobile= request.data.get("Mobile")
        Class_of_vehicle = request.data.get('Class_of_vehicle') 
        Motor_vehicle_type = request.data.get("Motor_vehicle_type")
        Type_of_body = request.data.get("Type_of_body") 
        Type_of_vehicle = request.data.get("Type_of_vehicle")
        Date_of_manufacture = request.data.get("Date_of_manufacture")
        Colour = request.data.get("Colour")
        Engine_no = request.data.get("Engine_no")
        Transferror_name= request.data.get('Transferror_name')
        SDWnew= request.data.get('SDWnew')
        Gendernew = request.data.get("Gendernew")
        House_namenew = request.data.get("House_namenew")
        Postnew =request.data.get('Postnew')
        Pinnew= request.data.get("Pinnew")
        Citynew = request.data.get('Citynew') 
        Ownership_typenew =request.data.get('Ownership_typenew')
        Mobilenew= request.data.get("Mobilenew")
      
       
        role ='Ownership_transfer'
        vehi_newreg_status = '0'


        
        serializer = self.serializer_class(data ={"user_id":user_id,'Registration_id':Registration_id,'Owner_Name': Owner_Name,'SDW':SDW,'Gender':Gender,'House_name':House_name,'Post':Post,'Pin':Pin,'City':City,'Ownership_type':Ownership_type,'Mobile':Mobile,'Class_of_vehicle':Class_of_vehicle,'Motor_vehicle_type':Motor_vehicle_type,'Type_of_body':Type_of_body,'Type_of_vehicle':Type_of_vehicle,'Date_of_manufacture':Date_of_manufacture,'Colour':Colour,
        'Engine_no':Engine_no,'Transferror_name':Transferror_name,'SDWnew':SDWnew,'Gendernew':Gendernew,'House_namenew':House_namenew,'Postnew':Postnew,'Pinnew':Pinnew,'Citynew':Citynew,'Ownership_typenew':Ownership_typenew,'Mobilenew':Mobilenew,'vehi_newreg_status':vehi_newreg_status})
        print(serializer)


        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({"data": serializer.data, 'message': 'OwnerShip Transfer done successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
    


class getIndividualOwnership(GenericAPIView):
    serializer_class = Ownership_transferSerializer 
    def get(self,request,id):
        queryset = Ownership_transfer.objects.all().filter(user_id=id).values()
        return Response({'data': queryset, 'message':' OwnerShip Transfer data fetched', 'success':True}, status=status.HTTP_200_OK)


class Test_dateAPIView(GenericAPIView): 
    serializer_class = Test_dateSerializer 
   

    def post(self, request):
        userreg_id=request.data.get('userreg_id')
        licence_id=request.data.get('licence_id')
        Test_date= request.data.get('Test_date')
        Licence_type= request.data.get('Licence_type')
        
        role ='Test_date'
        test_status = '0'


        
        serializer = self.serializer_class(data ={'userreg_id':userreg_id,'licence_id':licence_id,'Test_date': Test_date,'Licence_type':Licence_type,'test_status':test_status})
        print(serializer)


        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({"data": serializer.data, 'message': 'Test date added successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
    

class getIndividualTestDates(GenericAPIView):
    serializer_class = Test_dateSerializer 
    def get(self,request,id):
        queryset = Test_date.objects.all().filter(user_id=id).values()
        return Response({'data': queryset, 'message':' Test dates are fetched', 'success':True}, status=status.HTTP_200_OK)


class PaymentAPIView(GenericAPIView): 
    serializer_class = PaymentSerializer 
   

    def post(self, request):
        userreg_id=request.data.get('userreg_id')
        name=request.data.get('name')
        Amount= request.data.get('Amount')
        Payment_mode= request.data.get('Payment_mode')
        Card_details = request.data.get("Card_details")
        Date = request.data.get("Date")
        Time =request.data.get('Time')
      
       
        role ='Payment'
        payment_status = '0'


        
        serializer = self.serializer_class(data ={'userreg_id':userreg_id,'name':name,'Amount': Amount,'Payment_mode':Payment_mode,'Card_details':Card_details,'Date':Date,'Time':Time,'payment_status':payment_status})
        print(serializer)


        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({"data": serializer.data, 'message': 'payment added successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
    

class getIndividualPayments(GenericAPIView):
    serializer_class = PaymentSerializer 
    def get(self,request,id):
        queryset = Payment.objects.all().filter(userreg_id=id).values()
        return Response({'data': queryset, 'message':' Payments data fetched', 'success':True}, status=status.HTTP_200_OK)


class HazmateAPIView(GenericAPIView): 
    serializer_class = HazmateSerializer 
   

    def post(self, request):
        First_Name= request.data.get('First_Name')
        user_id= request.data.get('user_id')
        Last_Name= request.data.get('Last_Name')
        Date_of_birth = request.data.get("Date_of_birth")
        Email_address = request.data.get("Email_address")
        Phone_no =request.data.get('Phone_no')
        Licence_photo =request.data.get('Licence_photo')

      
       
        role ='Hazmate'
        hazmate_status = '0'
        verified_with_adhar = '0'


        
        serializer = self.serializer_class(data ={"user_id":user_id,'First_Name': First_Name,'Last_Name':Last_Name,'Date_of_birth':Date_of_birth,'Email_address':Email_address,'Phone_no':Phone_no,'Licence_photo':Licence_photo,'hazmate_status':hazmate_status,'verified_with_adhar':verified_with_adhar})
        print(serializer)


        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({"data": serializer.data, 'message': 'Hazmate Applied successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


class getIndividualHazmate(GenericAPIView):
    serializer_class = HazmateSerializer 
    def get(self,request,id):
        queryset = Hazmate.objects.all().filter(user_id=id).values()
        return Response({'data': queryset, 'message':' hazmate data fetched', 'success':True}, status=status.HTTP_200_OK)


class PSV_BadgeAPIView(GenericAPIView): 
    serializer_class = PSV_BadgeSerializer 
   

    def post(self, request):
        First_Name= request.data.get('First_Name')
        user_id= request.data.get('user_id')
        Last_Name= request.data.get('Last_Name')
        SDW = request.data.get("SDW")
        House_name = request.data.get("House_name")
        Post =request.data.get('Post')
        Pin =request.data.get('Pin')
        City =request.data.get('City')
        Phone_no =request.data.get('Phone_no')
        Photo =request.data.get('Photo')
        sign =request.data.get('sign')

      
       
        role ='PSV_Badge'
        psv_status = '0'


        
        serializer = self.serializer_class(data ={"user_id":user_id,'First_Name': First_Name,'Last_Name':Last_Name,'SDW':SDW,'House_name':House_name,'Post':Post,'Pin':Pin,'City':City,'Phone_no':Phone_no,'Photo':Photo,'sign':sign,'psv_status':psv_status})
        print(serializer)


        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({"data": serializer.data, 'message': 'Badge Applied successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
    

class getIndividualBadge(GenericAPIView):
    serializer_class = PSV_BadgeSerializer 
    def get(self,request,id):
        queryset = PSV_Badge.objects.all().filter(user_id=id).values()
        return Response({'data': queryset, 'message':' PSV badge data fetched', 'success':True}, status=status.HTTP_200_OK)



class International_dlAPIView(GenericAPIView): 
    serializer_class = International_dlSerializer 
   

    def post(self, request):
        First_Name= request.data.get('First_Name')
        user_id= request.data.get('user_id')
        Last_Name= request.data.get('Last_Name')
        SDW = request.data.get("SDW")
        Place_of_birth_and_country =request.data.get('Place_of_birth_and_country')
        House_name = request.data.get("House_name")
        Post =request.data.get('Post')
        Pin =request.data.get('Pin')
        City =request.data.get('City')
        Mobile =request.data.get('Mobile')
        Date_of_birth =request.data.get('Date_of_birth')
        Identification_mark =request.data.get('Identification_mark')
        Blood_group =request.data.get('Blood_group')
        Details_if_already_held_international_dl =request.data.get('Details_if_already_held_international_dl')
        Licence_photo =request.data.get('Licence_photo')
        passport =request.data.get('passport')
        Photo =request.data.get('Photo')

      
       
        role ='International_dl'
        inter_dl_status = '0'


        
        serializer = self.serializer_class(data ={"user_id":user_id,'First_Name': First_Name,'Last_Name':Last_Name,'SDW':SDW,'Place_of_birth_and_country':Place_of_birth_and_country,'House_name':House_name,'Post':Post,'Pin':Pin,'City':City,'Mobile':Mobile,'Date_of_birth':Date_of_birth,'Identification_mark':Identification_mark,'Blood_group':Blood_group,'Details_if_already_held_international_dl':Details_if_already_held_international_dl,'Licence_photo':Licence_photo,'Photo':Photo,'inter_dl_status':inter_dl_status,'passport':passport})
        print(serializer)


        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({"data": serializer.data, 'message': 'Applied successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
    

class getIndividualInternationalLicence(GenericAPIView):
    serializer_class = International_dlSerializer 
    def get(self,request,id):
        queryset = International_dl.objects.all().filter(user_id=id).values()
        return Response({'data': queryset, 'message':' International licenses  fetched', 'success':True}, status=status.HTTP_200_OK)


class AdhaarAPIView(GenericAPIView): 
    serializer_class = AdhaarSerializer 
   

    def post(self, request):
        First_Name= request.data.get('First_Name')
        user_id= request.data.get('user_id')
        Last_Name= request.data.get('Last_Name')
        SDW = request.data.get("SDW")
        House_name = request.data.get("House_name")
        Post =request.data.get('Post')
        Pin =request.data.get('Pin')
        City =request.data.get('City')
        Mobile =request.data.get('Mobile')
        Date_of_birth =request.data.get('Date_of_birth')
        Identification_mark =request.data.get('Identification_mark')
        Blood_group =request.data.get('Blood_group')
        sign =request.data.get('sign')
        Licence_photo =request.data.get('Licence_photo')
        Photo =request.data.get('Photo')

      
       
        role ='Adhaar'
        adhaar_status = '0'


        
        serializer = self.serializer_class(data ={"user_id":user_id,'First_Name': First_Name,'Last_Name':Last_Name,'SDW':SDW,'House_name':House_name,'Post':Post,'Pin':Pin,'City':City,'Mobile':Mobile,'Date_of_birth':Date_of_birth,'Identification_mark':Identification_mark,'Blood_group':Blood_group,'sign':sign,'Photo':Photo,'adhaar_status':adhaar_status})
        print(serializer)


        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({"data": serializer.data, 'message': 'Adhar added successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)


class getIndividualAdhar(GenericAPIView):
    serializer_class = AdhaarSerializer 
    def get(self,request,id):
        queryset = Adhaar.objects.all().filter(user_id=id).values()
        return Response({'data': queryset, 'message':' Adhar data  fetched', 'success':True}, status=status.HTTP_200_OK)
    

class ApplyRenewLicence(GenericAPIView):
    serializer_class = licenceSerializer 

    def post(self, request):
        learners_id=request.data.get('learners_id')
        user_id=request.data.get('user_id')
        licence_number= request.data.get('licence_number')
        First_Name= request.data.get('First_Name')
        Last_Name= request.data.get('Last_Name')
        Gender= request.data.get('Gender')
        House_name = request.data.get("House_name")
        Post =request.data.get('Post')
        Pin= request.data.get("Pin")
        City = request.data.get('City') 
        Date_of_birth = request.data.get("Date_of_birth")
        Email_address = request.data.get("Email_address") 
        Phone_no = request.data.get("Phone_no")
        Blood_group = request.data.get("Blood_group")
        photo = request.data.get("photo")
        Date_of_issue = request.data.get("Date_of_issue")
        Reason_for_not_renew = request.data.get("Reason_for_not_renew")
        Reason_for_apply_duplicate = request.data.get("Reason_for_apply_duplicate")


        role ='licence'
        licence_status = '2'
        verified_with_adhar='0'


        
        serializer = self.serializer_class(data ={'user_id':user_id,'learners_id':learners_id,'licence_number':licence_number,'First_Name': First_Name,'Last_Name': Last_Name,'Gender':Gender,'House_name':House_name,'Post':Post,'Pin':Pin,'City':City,'Date_of_birth':Date_of_birth,'Email_address':Email_address,'Phone_no':Phone_no,'Gender':Gender,'Blood_group':Blood_group,'photo':photo,'Date_of_issue':Date_of_issue,'Reason_for_not_renew':Reason_for_not_renew,'Reason_for_apply_duplicate':Reason_for_apply_duplicate,'licence_status':licence_status,'verified_with_adhar':verified_with_adhar})
        print(serializer)


        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({"data": serializer.data, 'message': 'License Applied for renewal successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
    

class ApplyDuplicateLicence(GenericAPIView):
    serializer_class = licenceSerializer 

    def post(self, request):
        learners_id=request.data.get('learners_id')
        user_id=request.data.get('user_id')
        licence_number= request.data.get('licence_number')
        First_Name= request.data.get('First_Name')
        Last_Name= request.data.get('Last_Name')
        Gender= request.data.get('Gender')
        House_name = request.data.get("House_name")
        Post =request.data.get('Post')
        Pin= request.data.get("Pin")
        City = request.data.get('City') 
        Date_of_birth = request.data.get("Date_of_birth")
        Email_address = request.data.get("Email_address") 
        Phone_no = request.data.get("Phone_no")
        Blood_group = request.data.get("Blood_group")
        photo = request.data.get("photo")
        Date_of_issue = request.data.get("Date_of_issue")
        Reason_for_not_renew = request.data.get("Reason_for_not_renew")
        Reason_for_apply_duplicate = request.data.get("Reason_for_apply_duplicate")


        role ='licence'
        licence_status = '3'
        verified_with_adhar='0'


        
        serializer = self.serializer_class(data ={'user_id':user_id,'learners_id':learners_id,'licence_number':licence_number,'First_Name': First_Name,'Last_Name': Last_Name,'Gender':Gender,'House_name':House_name,'Post':Post,'Pin':Pin,'City':City,'Date_of_birth':Date_of_birth,'Email_address':Email_address,'Phone_no':Phone_no,'Gender':Gender,'Blood_group':Blood_group,'photo':photo,'Date_of_issue':Date_of_issue,'Reason_for_not_renew':Reason_for_not_renew,'Reason_for_apply_duplicate':Reason_for_apply_duplicate,'licence_status':licence_status,'verified_with_adhar':verified_with_adhar})
        print(serializer)


        if serializer.is_valid():
            print("hi")
            serializer.save()
            return Response({"data": serializer.data, 'message': 'Applied  duplicate license successfully', 'success': True}, status = status.HTTP_201_CREATED)

        return Response({'data':serializer.errors, 'message': 'Failed', 'success':False}, status=status.HTTP_400_BAD_REQUEST)
    

class getIndividualTestDate(GenericAPIView):
    serializer_class = Test_dateSerializer 
    def get(self,request):
        queryset = Test_date.objects.all().filter(user_id=id).values()
        return Response({'data': queryset, 'message':'Test Dates fetched Successfully', 'success':True}, status=status.HTTP_200_OK)
    
