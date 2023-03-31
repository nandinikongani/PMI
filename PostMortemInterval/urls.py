"""PostMortemInterval URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Doctor import views as Doctor
from admins import views as admins
from forensic import views as frnsc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', Doctor.index, name='index'),
    path('doctorlogin/',Doctor.doctorlogin,name='doctorlogin'),
    path('doctorregister/',Doctor.doctorregister,name='doctorregister'),
    path('doctorlogincheck/',Doctor.doctorlogincheck,name='doctorlogincheck'),
    path('bodydetails1/',Doctor.bodydetails1,name='bodydetails1'),
    path('doctorreport/',Doctor.doctorreport,name='doctorreport'),
    path('doctorreport1/',Doctor.doctorreport1,name='doctorreport1'),
    path('doctorfinalreport/',Doctor.doctorfinalreport,name='doctorfinalreport'),



    path('frnsclogin/', frnsc.frnsclogin, name='frnsclogin'),
    path('frnscloginentered/', frnsc.frnscloginentered, name='frnscloginentered'),
    path('bodydetails/', frnsc.bodydetails, name='bodydetails'),
    path('forensicreport/', frnsc.forensicreport, name='forensicreport'),
    path('frnscreport1/', frnsc.frnscreport1, name='frnscreport1'),



    path('admin1/', admins.adminlogin, name='admin1'),
    path('adminloginentered/', admins.adminloginentered, name='adminloginentered'),
    path('doctordetails/', admins.doctordetails, name='doctordetails'),
    path('activatedoctor/',admins.activatedoctor,name='activatedoctor'),
    path('finalreport/',admins.finalreport,name='finalreport'),
    path('adminbodydetails/',admins.adminbodydetails,name='adminbodydetails'),
    path('logout/',admins.logout,name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

