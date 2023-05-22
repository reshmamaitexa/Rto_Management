from django.urls import path
from Rtomanagement import views

urlpatterns = [
   
   path('login_users', views.LoginUsersAPIView.as_view(), name='login_users'),
   path('user_register', views.UserRegisterAPIView.as_view(), name='user_register'),
   path('learners_apply', views.LearnerslicenceAPIView.as_view(), name='learners_apply'),
   path('get_user_details/<int:id>', views.GetSingleUserDetails.as_view(), name='get_user_details'),
   path('list_learners_licenses/<int:id>', views.getIndividualLearnersLicence.as_view(), name='list_learners_licenses'),
   path('list_licenses/<int:id>', views.getIndividualLicences.as_view(), name='list_licenses'),
   path('update_license/<int:id>', views.updateIndividualLicences.as_view(), name='update_license'),
   path('update_user/<int:id>', views.UpdateUserDetails.as_view(), name='update_user'),
   path('licence_apply', views.LicenceoriginalAPIView.as_view(), name='licence_apply'),
   path('vehi_reg_apply', views.Vehi_RegAPIView.as_view(), name='vehi_reg_apply'),
   path('list_vehicle_registers/<int:id>', views.getIndividualVehicleRegister.as_view(), name='list_vehicle_registers'),
   path('noc_apply', views.NocAPIView.as_view(), name='noc_apply'),
   path('list_noc/<int:id>', views.getIndividualNOC.as_view(), name='list_noc'),
   path('ownership_transfer_apply', views.Ownership_transferAPIView.as_view(), name='ownership_transfer_apply'), 
   path('list_ownership_transfers/<int:id>', views.getIndividualOwnership.as_view(), name='list_ownership_transfers'),
   path('test_date_apply', views.Test_dateAPIView.as_view(), name='test_date_apply'),
   path('list_testdates/<int:id>', views.getIndividualTestDates.as_view(), name='list_testdates'),
   path('payment_apply', views.PaymentAPIView.as_view(), name='payment_apply'),
   path('list_payments/<int:id>', views.getIndividualPayments.as_view(), name='list_payments'),
   path('hazmate_apply', views.HazmateAPIView.as_view(), name='hazmate_apply'),
   path('list_hazmates/<int:id>', views.getIndividualHazmate.as_view(), name='list_hazmates'),
   path('PSV_Badge_apply', views.PSV_BadgeAPIView.as_view(), name='PSV_Badge_apply'),
   path('list_badges/<int:id>', views.getIndividualBadge.as_view(), name='list_badges'),
   path('International_dl_apply', views.International_dlAPIView.as_view(), name='International_dl_apply'),
   path('list_international_licenses/<int:id>', views.getIndividualInternationalLicence.as_view(), name='list_international_licenses'),
   path('Aadhar_details', views.AdhaarAPIView.as_view(), name='Aadhar_details'),
   path('list_adhar/<int:id>', views.getIndividualAdhar.as_view(), name='list_adhar'),
   path('apply_renew_licence', views.ApplyRenewLicence.as_view(), name='apply_renew_licence'),
   path('apply_duplicate_licence', views.ApplyDuplicateLicence.as_view(), name='apply_duplicate_licence'),
   path('list_test_dates', views.getIndividualTestDate.as_view(), name='list_test_dates'),




]