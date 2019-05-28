"""bookproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,re_path
from bookproject.bookmodule import views 
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('home/', views.layout,name="home"),
	path('reg/', views.register,name="libraryRegistration"),
	path('sellerreg/', views.registerAsseller,name="sellerRegistration"),
    path('userreg/', views.registerAsuser,name="userRegistration"),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name= 'login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('libraryaddbook',views.LibraryAddBook,name="libraryaddbook"),
    # path('myprofile/<str:username>',views.get_user_profile,name="myprofile"),
    path('librarybook',views.librarybook,name="librarybook"),
    path('libraryTable',views.libraryTable,name="libraryTable"),
    path('singlebook/<int:id>',views.singlelibrarybook,name="singlelibrarybook"),
    path("DeleteBook/<int:id>",views.libraryDeleteBook,name="libraryDeleteBook"),
    path("libraryTableUpdate/<int:id>",views.libraryTableUpdate,name="libraryTableUpdate"),
    path("search/",views.search,name="search"),
    re_path(r'^profile/(?P<pk>\d+)/$', views.get_user_profile, name='view_profile_with_pk'),
    path('selleraddbook',views.sellerAddBook,name="selleraddbook"),
    path('sellerbook',views.sellerbook,name="sellerbook"),
    path('singlesellerbook/<int:id>',views.singlesellerbook,name="singlesellerbook"),
    path('sellerTable',views.sellerTable,name="sellerTable"),
    path("DeleteBook/<int:id>",views.sellerDeleteBook,name="sellerDeleteBook"),
    path("sellerTableUpdate/<int:id>",views.sellerTableUpdate,name="sellerTableUpdate"),
    path('useraddbook',views.UseraddBook,name="useraddbook"),
    path('userbook',views.userbook,name="userbook"),
    path('singleuserbook/<int:id>',views.singleuserbook,name="singleuserbook"),
    path('userTable',views.userTable,name="userTable"),
    path("DeleteBook/<int:id>",views.userDeleteBook,name="userDeleteBook"),
    path("userTableUpdate/<int:id>",views.userTableUpdate,name="userTableUpdate"),
    path('maps',views.maps,name="maps"),
    path('locations',views.locations,name="locations"),
    # path('',views.homePage,name="homeByPage"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
        name='password_reset'),
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    path('change_password',auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='change_password'),

    path('HomepageBook/<int:id>',views.singleuserbookHomepage,name="singleuserbookHomepage"),
    path('registratioBLock',views.registratioBLock,name="registrationBlocks"),


    path('policy',views.policy,name="policy"),
    path('tandc',views.tandc,name="terms"),
    path('checkout',views.checkout,name="checkout"),
    path('payment',views.payment,name="payment"),


    re_path(r'^profile/(?P<pk>\d+)/$', views.get_seller_profile, name='view_profile_with_seller'),
    re_path(r'^profile/(?P<pk>\d+)/$', views.get_user_profile, name='view_profile_with_user'),
    re_path(r'^profile/(?P<pk>\d+)/$', views.get_bookuser_profile, name='view_bookprofile_with_user'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_URL)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


