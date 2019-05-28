from django import forms
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm
from .models import LibraryProfile,sellerProfile,userProfile,libraryAddBook,SellerAddBook,UserAddBook

class ExtendedUserCreationForm(UserCreationForm):
	# role=forms.ModelChoiceField(queryset=Group.objects.all())
	class Meta:
		model=User
		fields = ('username', 'email', 'password1', 'password2', )
	# def __init__(self,*args,**kwargs):
	# 	if kwargs.get('instance'):
	# 		initial=kwargs.setdefault('initial',{})
	# 		if kwargs['instance'].groups.all():
	# 			initial['role']=kwargs['instance'].groups.all()[0]
	# 		else:
	# 			initial['role']=None
	# 	forms.ModelForm.__init__(self,*args,**kwargs)
	def save(self,commit=True):
		# role=self.cleaned_data.pop('role')
		user=super().save(commit=False)
		# user.groups.set([role])
		if commit:
			user.save()
		return user
class libraryProfileForm(forms.ModelForm):
	class Meta:
		model=LibraryProfile
		fields=("nameOfLibrary","libraryAddress","Phone","dateOfEstablishment","time","email","librarywebsite","libraryPolicy","libraryMembership","librarySymbol")

class sellerProfileForm(forms.ModelForm):
	class Meta:
		model=sellerProfile
		fields=("nameOfSeller","sellerAddress","sellerContactNumber","selleremail","sellerProfile")

class userProfileForm(forms.ModelForm):
	class Meta:
		model=userProfile
		fields=("nameOfUser","usermobile","userAddress","userProfile1")
class LibraryForm(forms.ModelForm):
	class Meta:
		model=libraryAddBook
		exclude=['author',]

class sellerForm(forms.ModelForm):
	class Meta:
		model=SellerAddBook
		exclude=['author',]

class userForm(forms.ModelForm):
	class Meta:
		model=UserAddBook
		exclude=['author',]