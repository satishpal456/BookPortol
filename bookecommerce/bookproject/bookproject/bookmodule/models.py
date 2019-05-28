from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
# Create your models here.
bookStock = (
    ('In Stock', 'In Stock'),
    ('Out of Stock', 'Out of Stock'),
    )
class LibraryProfile(models.Model):
	
	user=models.OneToOneField(User,on_delete="models.CASCADE")
	nameOfLibrary=models.CharField("Library Name",max_length=30,blank=False,null=True)
	libraryAddress=models.CharField("Library Address",max_length=30,blank=False,null=True)
	Phone=models.IntegerField("contact Us",null=True)
	dateOfEstablishment=models.CharField("Establishment",max_length=30,blank=False,null=True)
	time=models.CharField("Library Time",max_length=30,blank=False,null=True)
	email = models.EmailField("E-mail",max_length=70,blank=False, null= True, unique= True)
	librarywebsite= models.URLField("website",max_length=250, null= True)
	libraryPolicy=models.CharField("Library Policy",max_length=30,blank=False,null=True)
	libraryMembership=models.CharField("Membership",max_length=30,blank=False,null=True)
	librarySymbol = models.FileField(upload_to='LibraryProfile/', blank=True,null=True)

	def __str__(self):
		return self.user.username
def create_profile(sender,**kwargs):
	if kwargs['created']:
		user_profile=LibraryProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)
class sellerProfile(models.Model):
	user=models.OneToOneField(User,on_delete="models.CASCADE")

	nameOfSeller=models.CharField("Name",max_length=30,blank=False,null=True)
	sellerAddress=models.CharField("Address",max_length=30,blank=False,null=True)
	sellerContactNumber=models.CharField("Mobile No",max_length=30,blank=False,null=True)
	selleremail = models.EmailField("E-mail",max_length=70,blank=False, null= True,unique= True)
	sellerProfile= models.FileField(upload_to='sellerProfile/', blank=True,null=True)

	def __str__(self):
		return self.user.username
class userProfile(models.Model):
	user=models.OneToOneField(User,on_delete="models.CASCADE")

	nameOfUser=models.CharField("Name",max_length=30,blank=False,null=True)
	userAddress=models.CharField("Address",max_length=30,blank=False,null=True)
	usermobile=models.CharField("Mobile No",max_length=30,blank=False,null=True)
	email = models.EmailField("E-mail",max_length=70,blank=False, null= True, unique= True)
	userProfile1= models.FileField("userProfile",upload_to='userProfile/', blank=True,null=True)

	def __str__(self):
		return self.user.username

bookStock = (
    ('In Stock', 'In Stock'),
    ('Out of Stock', 'Out of Stock'),
    )
class libraryAddBook(models.Model):
	bookName=models.CharField("Book Name",max_length=30,blank=False,null=True)
	# bookPrice=models.CharField("Book Price",max_length=30,blank=False,null=True)
	bookLanguage=models.CharField("Language",max_length=30,blank=False)
	bookBinding=models.CharField("Binding",max_length=30,error_messages={'required': 'Please enter your name'})
	bookISBN=models.CharField("ISBN",max_length=30,blank=False,)
	bookGener=models.CharField("Genre",max_length=30,blank=False,)
	bookEdition=models.IntegerField("Edition")
	bookPages=models.IntegerField("Pages")
	bookStock=models.CharField("InStock",max_length=30, blank=False,choices=bookStock)
	bookSummary=RichTextField("Summary Of The Book",null= True)
	aboutAuthor=RichTextField("About the Author",null= True)
	bookImage = models.FileField(upload_to='documents/%Y/', blank=True)
	author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	# location = models.PointField(srid=4326,null=True)

class SellerAddBook(models.Model):
	bookName=models.CharField("Book Name",max_length=30,blank=False,null=True)
	bookPrice=models.CharField("Book Price",max_length=30,blank=False,null=True)
	bookLanguage=models.CharField("Language",max_length=30,blank=False,null=True)
	bookBinding=models.CharField("Binding",max_length=30,error_messages={'required': 'Please enter your name'},null=True)
	bookISBN=models.CharField("ISBN",max_length=30,blank=False,null=True)
	bookGener=models.CharField("Genre",max_length=30,blank=False,null=True)
	bookEdition=models.IntegerField("Edition",null=True)
	bookPages=models.IntegerField("Pages",null=True)
	bookStock=models.CharField("InStock",max_length=30, blank=False,choices=bookStock,null=True)
	bookSummary=RichTextField("Summary Of The Book",null=True)
	aboutAuthor=RichTextField("About the Author",null=True)
	bookImage = models.FileField(upload_to='documents/%Y/', blank=True,null=True)
	author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class UserAddBook(models.Model):
	bookName=models.CharField("Book Name",max_length=30,blank=False,null=True)
	bookPrice=models.CharField("Book Price",max_length=30,blank=False,null=True)
	bookLanguage=models.CharField("Language",max_length=30,blank=False,null=True)
	bookBinding=models.CharField("Binding",max_length=30,error_messages={'required': 'Please enter your name'},null=True)
	bookISBN=models.CharField("ISBN",max_length=30,blank=False,null=True)
	bookGener=models.CharField("Genre",max_length=30,blank=False,null=True)
	bookEdition=models.IntegerField("Edition",null=True)
	bookPages=models.IntegerField("Pages",null=True)
	bookStock=models.CharField("InStock",max_length=30, blank=False,choices=bookStock,null=True)
	bookSummary=RichTextField("Summary Of The Book",null=True)
	aboutAuthor=RichTextField("About the Author",null=True)
	bookImage = models.FileField(upload_to='documents/%Y/', blank=True,null=True)
	author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)