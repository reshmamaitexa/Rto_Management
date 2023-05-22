from rest_framework import serializers
from .models import Login,rtouser,Learners,licence,Vehi_Reg,NOC,Ownership_transfer,Test_date,Payment,Hazmate,PSV_Badge,International_dl,Adhaar

class LoginUsersSerializer(serializers.ModelSerializer):
    class  Meta:
        model= Login
        fields='__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=rtouser
        fields='__all__'

    def Create(self,validated_data):
        return rtouser.objects.Create(**validated_data)

class LearnersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Learners
        fields='__all__'

    def Create(self,validated_data):
        return Learners.objects.Create(**validated_data)

class licenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=licence
        fields='__all__'

    def Create(self,validated_data):
        return licence.objects.Create(**validated_data)



class Vehi_RegSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehi_Reg
        fields='__all__'

    def Create(self,validated_data):
        return Vehi_Reg.objects.Create(**validated_data)

class NOCSerializer(serializers.ModelSerializer):
    class Meta:
        model=NOC
        fields='__all__'

    def Create(self,validated_data):
        return NOC.objects.Create(**validated_data)
class Ownership_transferSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ownership_transfer
        fields='__all__'

    def Create(self,validated_data):
        return Ownership_transfer.objects.Create(**validated_data)

class Test_dateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Test_date
        fields='__all__'

    def Create(self,validated_data):
        return Test_date.objects.Create(**validated_data)

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'

    def Create(self,validated_data):
        return Payment.objects.Create(**validated_data)


class HazmateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hazmate
        fields='__all__'

    def Create(self,validated_data):
        return Hazmate.objects.Create(**validated_data)


class PSV_BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model=PSV_Badge
        fields='__all__'

    def Create(self,validated_data):
        return PSV_Badge.objects.Create(**validated_data)


class International_dlSerializer(serializers.ModelSerializer):
    class Meta:
        model=International_dl
        fields='__all__'

    def Create(self,validated_data):
        return International_dl.objects.Create(**validated_data)

class AdhaarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Adhaar
        fields='__all__'

    def Create(self,validated_data):
        return Adhaar.objects.Create(**validated_data)

