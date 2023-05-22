from django.db import models

# Create your models here.
class Login(models.Model):

    username= models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=10)

    def __str__(self):
       return self.username

class rtouser(models.Model):

    First_Name = models.CharField(max_length= 20)
    Last_Name= models.CharField(max_length= 20)
    Gender= models.CharField(max_length=20)
    House_name =models.CharField(max_length=30) 
    Post = models.CharField(max_length=20)
    Pin = models.CharField(max_length=10)
    City = models.CharField(max_length=20)
    Date_of_birth= models.CharField(max_length=20) 
    Email_address = models.CharField(max_length=20)
    Phone_no = models.CharField(max_length=10)
    login_id= models.OneToOneField(Login, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)
    user_status = models.CharField(max_length=20)
    rejected_reason = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.First_Name
    



class Learners(models.Model):

    First_Name = models.CharField(max_length= 20)
    user_id= models.ForeignKey(rtouser, on_delete=models.CASCADE)
    Last_Name= models.CharField(max_length= 20)
    House_name =models.CharField(max_length=30) 
    Post = models.CharField(max_length=20)
    Pin = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    Date_of_birth= models.CharField(max_length=20) 
    Email_address = models.CharField(max_length=20)
    Phone_no = models.CharField(max_length=10)
    Gender= models.CharField(max_length=30)
    Blood_group= models.CharField(max_length=10)
    photo = models.ImageField(upload_to='learnersimages/', blank=True, null=True)
    Licence_type= models.CharField(max_length=50)
    test_date = models.CharField(max_length=20,blank=True, null=True)
    test_location = models.CharField(max_length=50,blank=True, null=True)
    learners_status = models.CharField(max_length=20)
    verified_with_adhar = models.CharField(max_length=20)
    rejected_reason = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.First_Name

class licence(models.Model):
    learners_id= models.ForeignKey(Learners, on_delete=models.CASCADE)
    user_id= models.ForeignKey(rtouser, on_delete=models.CASCADE)
    licence_number = models.CharField(max_length= 20,blank=True, null=True)
    First_Name = models.CharField(max_length= 30)
    Last_Name= models.CharField(max_length= 20)
    Gender= models.CharField(max_length=30)
    House_name =models.CharField(max_length=30) 
    Post = models.CharField(max_length=20)
    Pin = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    Date_of_birth= models.CharField(max_length=20) 
    Email_address = models.CharField(max_length=20)
    Phone_no = models.CharField(max_length=10)
    Blood_group= models.CharField(max_length=10)
    photo = models.ImageField(upload_to='licenseimages/', blank=True, null=True)
    Date_of_issue= models.CharField(max_length=20)
    Reason_for_not_renew= models.CharField(max_length=50)
    Reason_for_apply_duplicate= models.CharField(max_length=50)
    new_date = models.CharField(max_length=20,blank=True, null=True)
    test_date = models.CharField(max_length=20,blank=True, null=True)
    test_location = models.CharField(max_length=50,blank=True, null=True)
    licence_status = models.CharField(max_length=20)
    verified_with_adhar = models.CharField(max_length=20)
    rejected_reason = models.CharField(max_length=50,blank=True,null=True)
    renew_rejected_reason = models.CharField(max_length=50,blank=True,null=True)
    duplicated_rejected_reason = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.First_Name


class Vehi_Reg(models.Model):

    Owner_Name= models.CharField(max_length= 20)
    user_id= models.ForeignKey(rtouser, on_delete=models.CASCADE)
    SDW= models.CharField(max_length=20)
    Gender= models.CharField(max_length=30)
    House_name =models.CharField(max_length=30) 
    Post = models.CharField(max_length=20)
    Pin = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    Ownership_type =models.CharField(max_length=30) 
    Mobile = models.CharField(max_length=10)
    Class_of_vehicle = models.CharField(max_length=20)
    Motor_vehicle_type = models.CharField(max_length=20)
    Type_of_body = models.CharField(max_length=20)
    Type_of_vehicle = models.CharField(max_length=20)
    Date_of_manufacture = models.CharField(max_length=20)
    Date_of_issue = models.CharField(max_length=20)
    Horse_power = models.CharField(max_length=20)
    Cubic_capacity = models.CharField(max_length=20)
    Seating_capacity = models.CharField(max_length=20)
    Fuel_used_in_engine = models.CharField(max_length=20)
    Engine_no = models.CharField(max_length=20)
    Color = models.CharField(max_length=20)
    Vehi_photo = models.ImageField(upload_to='vehicleimages/', blank=True, null=True)
    vehi_reg_status = models.CharField(max_length=20)
    rejected_reason = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.First_Name



class NOC(models.Model):

    Registration_id= models.ForeignKey(Vehi_Reg, on_delete=models.CASCADE)
    user_id= models.ForeignKey(rtouser, on_delete=models.CASCADE)
    First_Name = models.CharField(max_length= 20)
    Last_Name= models.CharField(max_length= 20)
    SDW= models.CharField(max_length=20)
    Phone_no = models.CharField(max_length=10)
    Reg_of_vehicle =models.CharField(max_length=30) 
    Class_of_vehicle = models.CharField(max_length=20)
    Engine_no = models.CharField(max_length=20)
    Period_of_stay_in_state = models.CharField(max_length=20)
    Tax_pending_details= models.CharField(max_length=20) 
    Vehi_photo = models.ImageField(upload_to='vehicleimages/', blank=True, null=True)
    sign = models.ImageField(upload_to='signature/', blank=True, null=True)
    noc_status = models.CharField(max_length=20)
    rejected_reason = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.First_Name
class Ownership_transfer(models.Model):
    Registration_id= models.ForeignKey(Vehi_Reg, on_delete=models.CASCADE)
    Owner_Name= models.CharField(max_length= 20)
    user_id= models.ForeignKey(rtouser, on_delete=models.CASCADE)
    SDW= models.CharField(max_length=20)
    Gender= models.CharField(max_length=10)
    House_name =models.CharField(max_length=30) 
    Post = models.CharField(max_length=20)
    Pin = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    Ownership_type =models.CharField(max_length=30) 
    Mobile = models.CharField(max_length=10)
    Class_of_vehicle = models.CharField(max_length=20)
    Motor_vehicle_type = models.CharField(max_length=20)
    Type_of_body = models.CharField(max_length=20)
    Type_of_vehicle = models.CharField(max_length=20)
    Date_of_manufacture = models.CharField(max_length=20)
    Colour = models.CharField(max_length=20)
    Engine_no = models.CharField(max_length=20)
    Transferror_name= models.CharField(max_length= 20)
    SDWnew= models.CharField(max_length=20)
    Gendernew= models.CharField(max_length=10)
    House_namenew =models.CharField(max_length=30) 
    Postnew = models.CharField(max_length=20)
    Pinnew = models.CharField(max_length=20)
    Citynew = models.CharField(max_length=20)
    Ownership_typenew =models.CharField(max_length=30) 
    Mobilenew = models.CharField(max_length=10)
    vehi_newreg_status = models.CharField(max_length=20)
    rejected_reason = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.First_Name
class Test_date(models.Model):
    Test_date= models.CharField(max_length=20) 
    user_id = models.ForeignKey(rtouser,on_delete=models.CASCADE)
    name= models.CharField(max_length=50) 
    Licence_type = models.CharField(max_length=50)
    test_status = models.CharField(max_length=20)

    def __str__(self):
        return self.name
class Payment(models.Model):

    userreg_id= models.ForeignKey(rtouser, on_delete=models.CASCADE)
    name = models.CharField(max_length= 50)
    Amount = models.CharField(max_length= 20)
    Payment_mode= models.CharField(max_length= 20)
    Card_details= models.CharField(max_length=15)
    Date = models.CharField(max_length=10)
    Time =models.CharField(max_length=30) 
    payment_status = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Hazmate(models.Model):

    First_Name = models.CharField(max_length= 20)
    user_id= models.ForeignKey(rtouser, on_delete=models.CASCADE)
    Last_Name= models.CharField(max_length= 20)
    Date_of_birth= models.CharField(max_length=20)
    Email_address = models.CharField(max_length=20)
    Phone_no =models.CharField(max_length=30) 
    test_date = models.CharField(max_length=20,blank=True, null=True)
    test_location = models.CharField(max_length=50,blank=True, null=True)
    Licence_photo = models.ImageField(upload_to='licenseimages/', blank=True, null=True)
    hazmate_status = models.CharField(max_length=20)
    verified_with_adhar = models.CharField(max_length=20)
    rejected_reason = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.First_Name

class PSV_Badge(models.Model):

    First_Name = models.CharField(max_length= 20)
    Last_Name= models.CharField(max_length= 20)
    SDW= models.CharField(max_length=20)
    House_name =models.CharField(max_length=30) 
    Post = models.CharField(max_length=20)
    user_id= models.ForeignKey(rtouser, on_delete=models.CASCADE)
    Pin = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    Phone_no = models.CharField(max_length=10)
    Photo= models.ImageField(upload_to='licenseimages/', blank=True, null=True) 
    sign = models.ImageField(upload_to='signature/', blank=True, null=True)
    psv_status = models.CharField(max_length=20)
    rejected_reason = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.First_Name

class International_dl(models.Model):

    First_Name = models.CharField(max_length= 20)
    Last_Name= models.CharField(max_length= 20)
    user_id= models.ForeignKey(rtouser, on_delete=models.CASCADE)
    SDW= models.CharField(max_length=20)
    Place_of_birth_and_country= models.CharField(max_length=20)
    House_name =models.CharField(max_length=30) 
    Post = models.CharField(max_length=20)
    Pin = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    Mobile = models.CharField(max_length=10)
    Date_of_birth = models.CharField(max_length=20)
    Identification_mark = models.CharField(max_length=20)
    Blood_group = models.CharField(max_length=20)
    Details_if_already_held_international_dl = models.CharField(max_length=20)
    Licence_photo = models.ImageField(upload_to='licenseimages/', blank=True, null=True)
    Photo = models.ImageField(upload_to='internationalimages/', blank=True, null=True)
    passport = models.ImageField(upload_to='internationalimages/', blank=True, null=True)
    inter_dl_status = models.CharField(max_length=20)
    rejected_reason = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.First_Name

class Adhaar(models.Model):

    First_Name = models.CharField(max_length= 20)
    Last_Name= models.CharField(max_length= 20)
    SDW= models.CharField(max_length=20)
    House_name =models.CharField(max_length=30) 
    Post = models.CharField(max_length=20)
    Pin = models.CharField(max_length=20)
    City = models.CharField(max_length=20)
    Mobile = models.CharField(max_length=10)
    Date_of_birth = models.CharField(max_length=20)
    Photo = models.ImageField(upload_to='adharimages/', blank=True, null=True)
    adhaar_status = models.CharField(max_length=20)

    def __str__(self):
        return self.First_Name