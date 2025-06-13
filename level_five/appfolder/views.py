from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,logout,login # type: ignore
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse

def index(request):
    return render(request,'index.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_data = UserForm(data=request.POST)           # set the receievd data to the forms for validation
        user_pic = UserProfileInfoForm(data=request.POST)

        if user_data.is_valid() and user_pic.is_valid():
            validated_data = user_data.save()

            # Convert the password into hash for storage
            validated_data.set_password(validated_data.password)
            validated_data.save()

            validated_pic = user_pic.save(commit=False)  # Don't Save the pic in database
            validated_pic.user = validated_data          # Bridging them connects the extra data to the specific user

            if 'profile_pic' in request.FILES:           # see if the user provide pic and 'profile_pic' is field name given as a string   
                validated_pic.profile_pic = request.FILES['profile_pic'] # object.field = request.FILES['field name']

            validated_pic.save()
            registered = True
            
        else:
            print(user_data.errors,user_pic.errors)
    else:
        user_data = UserForm()
        user_pic = UserProfileInfoForm()

    return render(request,'register.html',{'user_data':user_data,
                                                 'user_pic':user_pic,
                                                 'register':registered}) 
 # {'register' : register} It doesn’t directly show True or False to the user;
 # it’s used in the template to control what’s displayed

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username') # username in get is a key matches with name html form input (name="username")
        pass_word = request.POST.get('password')  # the value for the key is whatever the user is inputted.

        print(f"Received: username='{user_name}', password='{pass_word}'")
        # authenticate if username & password with registered username & password

        user_auth = authenticate(username = user_name,password = pass_word) 

        if user_auth:
            if user_auth.is_active:
                login(request,user_auth)                      # Sets request.user to user_auth
                return HttpResponseRedirect(reverse('index')) # redirect the user to index with navbar stays as log out 
                # index refers to the name='index' defined in your project’s urls.py
            
            else:                            # if the user account is not active              
                print('ACCOUNT NOT ACTIVE')
                
        else:                                # if the user authentication is failed
            print('SOMEONE LOG-IN FAILED')
            print('USERNAME: {} AND PASSWORD: {}'.format(user_name,pass_word))
            return HttpResponse('Invalid details')     # To display the user
        
    else:
        return render(request,'login.html')
    
@login_required           # only the logged in user can log out
def user_logout(request):
    logout(request)       # it automatically logs out the user, no need details about the user
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse('YOU ARE LOGGED IN')




            


 