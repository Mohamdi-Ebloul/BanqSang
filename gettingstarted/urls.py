from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
from django.contrib.auth.views import LogoutView,LoginView
from bqsang import views
# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    
    path('donor/', include('donor.urls')),
    path('patient/', include('patient.urls')),

    path('', views.home_view, name='home'),
    path('logout', LogoutView.as_view(template_name='blood/logout.html'), name='logout'),

    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('adminlogin', LoginView.as_view(template_name='blood/adminlogin.html'), name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),
    path('admin-blood', views.admin_blood_view, name='admin-blood'),
    path('admin-donor', views.admin_donor_view, name='admin-donor'),
    path('admin-patient', views.admin_patient_view, name='admin-patient'),
    path('update-donor/<int:pk>', views.update_donor_view, name='update-donor'),
    path('delete-donor/<int:pk>', views.delete_donor_view, name='delete-donor'),
    path('admin-request', views.admin_request_view, name='admin-request'),
    path('update-patient/<int:pk>', views.update_patient_view, name='update-patient'),
    path('delete-patient/<int:pk>', views.delete_patient_view, name='delete-patient'),
    path('admin-donation', views.admin_donation_view, name='admin-donation'),
    path('approve-donation/<int:pk>', views.approve_donation_view, name='approve-donation'),
    path('reject-donation/<int:pk>', views.reject_donation_view, name='reject-donation'),
    path('admin-request-history', views.admin_request_history_view, name='admin-request-history'),
    path('update-approve-status/<int:pk>', views.update_approve_status_view, name='update-approve-status'),
    path('update-reject-status/<int:pk>', views.update_reject_status_view, name='update-reject-status'),
]
