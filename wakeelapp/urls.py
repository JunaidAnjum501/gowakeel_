from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .sitemaps import StaticViewSitemap, BlogSitemap
from django.contrib import admin
from django.urls import path
from . import views

app_name = "wakeelapp"

urlpatterns =[
    path('', views.index, name="index"),
    path('cal/', views.calculator, name="calculator"),
    path('atl/', views.atl, name="atl"),
    path('ntn/', views.ntn, name="ntn"),
    path('faq/', views.faq, name="faq"),
    path('contact/', views.contact, name="contact"),
    path('service_card/', views.service_card, name="service_card"),
    path("service/<str:service_name>/", views.service_detail, name="service_detail"),
    path('blogs/', views.blogs, name="blogs"),
    path('video/', views.video, name="video"),
    path('about/', views.about, name="about"),
    path('usaservice/', views.usaservice, name="usaservice"),
    path('login/', views.login, name="login"),
    path('blogdetail/<slug:blogs_slug>/', views.blogdetail, name='blogdetail'),
    path('zakatcalculator/', views.zakatcalculator, name="zakatcalculator"),
    path('currencyconvert/', views.currencyconvert, name="currencyconvert"),
    path('services/', views.services, name="services"),
    path('taxreturn/', views.taxreturn, name="taxreturn"),
    path('compnayregistration/', views.companyregistration, name="companyregistration"),
    path('karachichamber/', views.karachichamber, name="karachichamber"),
    path('pswregistration/', views.pswregistration, name="pswregistration"),
    path('pseb/', views.pseb, name="pseb"),
    path('trademark/', views.trademark, name="trademark"),
    path('schoolngo', views.schoolngo, name="schoolngo"),
    path('propertytransfer/', views.propertytransfer, name="propertytransfer"),
    path('auditservice/', views.auditservice, name="auditservice"),
]


sitemaps = {
    'static': StaticViewSitemap(),
    'blogs': BlogSitemap(),
}

urlpatterns += [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
