from django.contrib import admin
from .models import LibraryProfile,sellerProfile,userProfile,libraryAddBook,SellerAddBook,UserAddBook
# Register your models here.
admin.site.register(LibraryProfile)
admin.site.register(sellerProfile)
admin.site.register(userProfile)
admin.site.register(libraryAddBook)
admin.site.register(SellerAddBook)
admin.site.register(UserAddBook)

