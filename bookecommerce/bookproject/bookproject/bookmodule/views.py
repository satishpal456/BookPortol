from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import LibraryProfile,sellerProfile,userProfile,libraryAddBook,SellerAddBook,UserAddBook
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .forms import ExtendedUserCreationForm,libraryProfileForm,sellerProfileForm,userProfileForm,LibraryForm,sellerForm,userForm
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def layout(request):
	return render(request,'layout.html')
def register(request):
	if request.method=='POST':
		form=ExtendedUserCreationForm(request.POST)
		profile_form=libraryProfileForm(request.POST)
		if form.is_valid() and profile_form.is_valid():
			user=form.save()
			profile=profile_form.save(commit=False)
			profile.user=user
			profile.save()
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password1')
			user=authenticate(username=username,password=password)
			login(request,user)
			return HttpResponse("submitted")
	else:
		form=ExtendedUserCreationForm()
		profile_form=libraryProfileForm()
	context={'form':form,'profile_form':profile_form}
	return render(request,'registration.html',context)
def registerAsseller(request):
	if request.method=='POST':
		form=ExtendedUserCreationForm(request.POST)
		profile_form=sellerProfileForm(request.POST)
		if form.is_valid() and profile_form.is_valid():
			user=form.save()
			profile=profile_form.save(commit=False)
			profile.user=user
			profile.save()
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password1')
			user=authenticate(username=username,password=password)
			login(request,user)
			return HttpResponse("submitted")
	else:
		form=ExtendedUserCreationForm()
		profile_form=sellerProfileForm()
	context={'form':form,'profile_form':profile_form}
	return render(request,'sellerregistration.html',context)

def registerAsuser(request):
	if request.method=='POST':
		form=ExtendedUserCreationForm(request.POST)
		profile_form=userProfileForm(request.POST)
		if form.is_valid() and profile_form.is_valid():
			user=form.save()
			profile=profile_form.save(commit=False)
			profile.user=user
			profile.save()
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password1')
			user=authenticate(username=username,password=password)
			login(request,user)
			return HttpResponse("submitted")
	else:
		form=ExtendedUserCreationForm()
		profile_form=userProfileForm()
	context={'form':form,'profile_form':profile_form}
	return render(request,'userregistration.html',context)

def LibraryAddBook(request):
	# sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
	if request.method == 'POST':
		form = LibraryForm(request.POST,request.FILES)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.author=request.user
			instance.save()
			return redirect('home')		
	else:
		form = LibraryForm()
	return render(request, 'libraryaddbook.html', {'form': form})

def librarybook(request):
	librarybookData=libraryAddBook.objects.all()
	return render(request,'librarybook.html',{"librarybookData":librarybookData})
def singlelibrarybook(request,id):
	singlebook=libraryAddBook.objects.get(id=id)
	return render(request,'singlebook.html',{'singlebook':singlebook})

def libraryTable(request):
	librarybookDisp=libraryAddBook.objects.filter(author=request.user)
	return render(request,'librarytable.html',{'librarybookDisp':librarybookDisp})
# def librarybookmanage(request,id=None):
# 	librarybookEdit=libraryAddBook.objects.get(id=id)
# 	if request.method=="POST":
# 		form = LibraryForm(request.POST,request.FILES,instance=librarybookEdit)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('librarybook')
# 	else:
# 		librarybook = LibraryForm(instance=librarybookEdit)
# 	return render(request, 'libraryEditBookPage.html', {'librarybook': librarybook})

def libraryDeleteBook(request,id):
	deleteBook=libraryAddBook.objects.get(id=id)
	deleteBook.delete()
	return redirect('libraryTable')
def libraryTableUpdate(request,id=None):
	librarybookEdit=libraryAddBook.objects.get(id=id)
	if request.method=="POST":
		form = LibraryForm(request.POST,request.FILES,instance=librarybookEdit)
		if form.is_valid():
			form.save()
			return redirect('libraryTable')
	else:
		librarybookupdate = LibraryForm(instance=librarybookEdit)
	return render(request, 'libraryEditBookPage.html', {'librarybookupdate': librarybookupdate})

# def get_user_profile(request,username):
#     user = User.objects.get(username=username)
#     return render(request, 'libraryprofile.html', {"user":user})

def get_user_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'libraryprofile.html', args)


# search book in models

def search(request):
	if request.method=="POST":
		srch=request.POST['booksearch']
		if srch:
			match=libraryAddBook.objects.filter(Q(bookName__icontains=srch))
			if match:
				return render(request,'search.html',{'sr':match})
			else:
				messages.error(request,'Oops,no result found')
		else:
			return HttpResponseRedirect('/search/')
	return render(request,'search.html')	

# seller modules	

def sellerAddBook(request):
	# sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
	if request.method == 'POST':
		form = sellerForm(request.POST,request.FILES)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.author=request.user
			instance.save()
			return redirect('home')		
	else:
		form = sellerForm()
	return render(request, 'selleraddbook.html', {'form': form})
def sellerbook(request):
	sellerbookData=SellerAddBook.objects.all()
	return render(request,'sellerbook.html',{"sellerbookData":sellerbookData})

def singlesellerbook(request,id):
	singlesellerbook=SellerAddBook.objects.get(id=id)
	return render(request,'singlesellerbook.html',{'singlesellerbook':singlesellerbook})

def sellerTable(request):
	sellerbookDisp=SellerAddBook.objects.filter(author=request.user)
	return render(request,'sellertable.html',{'sellerbookDisp':sellerbookDisp})

def sellerDeleteBook(request,id):
	sellerdeleteBook=SellerAddBook.objects.get(id=id)
	sellerdeleteBook.delete()
	return redirect('sellerTable')

def sellerTableUpdate(request,id=None):
	sellerbookEdit=SellerAddBook.objects.get(id=id)
	if request.method=="POST":
		form = sellerForm(request.POST,request.FILES,instance=sellerbookEdit)
		if form.is_valid():
			form.save()
			return redirect('sellerTable')
	else:
		sellerbookupdate = sellerForm(instance=sellerbookEdit)
	return render(request, 'sellerEditBookPage.html', {'sellerbookupdate': sellerbookupdate})

def get_seller_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'sellerprofile.html', args)


# user view

def UseraddBook(request):
	# sweetify.success(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
	if request.method == 'POST':
		form = userForm(request.POST,request.FILES)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.author=request.user
			instance.save()
			return redirect('home')		
	else:
		form = userForm()
	return render(request, 'useraddbook.html', {'form': form})

def userbook(request):
	userbookData=UserAddBook.objects.all()
	return render(request,'userbook.html',{"userbookData":userbookData})

def singleuserbook(request,id):
	singleuserbook=UserAddBook.objects.get(id=id)
	return render(request,'singleuserbook.html',{'singleuserbook':singleuserbook})

def userTable(request):
	userbookDisp=UserAddBook.objects.filter(author=request.user)
	return render(request,'usertable.html',{'userbookDisp':userbookDisp})

def userDeleteBook(request,id):
	userdeleteBook=UserAddBook.objects.get(id=id)
	userdeleteBook.delete()
	return redirect('userTable')

def userTableUpdate(request,id=None):
	userbookEdit=UserAddBook.objects.get(id=id)
	if request.method=="POST":
		form = userForm(request.POST,request.FILES,instance=userbookEdit)
		if form.is_valid():
			form.save()
			return redirect('userTable')
	else:
		userbookupdate = userForm(instance=userbookEdit)
	return render(request, 'userEditBookPage.html', {'userbookupdate': userbookupdate})

def get_bookuser_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'userprofile.html', args)

def maps(request):
	return render(request,'map.html')

def locations(request):
	return render(request,'locations.html')

def registratioBLock(request):
	return render(request,'registrationBlock.html')
# def homePage(request):
# 	bookdisp=UserAddBook.objects.all()
# 	return render(request,"homepage.html",{"bookdisp":bookdisp})
def singleuserbookHomepage(request,id):
	bookSeperate=UserAddBook.objects.get(id=id)
	return render(request,'singleUserBookOutside.html',{'bookSeperate':bookSeperate})

def policy(request):
	return render(request,'policy.html')


def tandc(request):
	return render(request, 'tandc.html')

def checkout(request):
	return render(request, 'checkout.html')

def payment(request):
	return render(request, 'payment.html')