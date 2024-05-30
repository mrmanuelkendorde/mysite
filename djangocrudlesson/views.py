from django.shortcuts import render, redirect       
from .models import Gender
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
#from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def index_gender(request):
    genders = Gender.objects.all() # SELECT * FROM genders

    context = {
        'genders': genders 
    }

    return render(request, 'gender/index.html', context)
 
def create_gender(request):
    return render(request, 'gender/create.html')
    
def store_gender(request):
    gender = request.POST.get('gender')
    Gender.objects.create(gender=gender) # INSERT INTO genders(gender) VALUES(gender)
    messages.success(request, 'Gender successfully saved.')
    return redirect('/genders')

def show_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id) #SELECT * FROM gender WHERE gender_id = gender_id

    context = {
        'gender': gender,
    }

    return render(request, 'gender/show.html', context)

def edit_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id) #SELECT * FROM gender WHERE gender_id = gender_id

    context = {
        'gender': gender,
    }

    return render(request, 'gender/edit.html', context)

def update_gender(request, gender_id):
    gender = request.POST.get('gender') 

    Gender.objects.filter(pk=gender_id).update(gender=gender) # UPDATE genders SET gender = gender WHERE gender_id = gender_id
    messages.success(request, 'Gender Successfully updated')
    
    return redirect('/genders')

def delete_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id) #SELECT * FROM gender WHERE gender_id = gender_id

    context = {
        'gender': gender,
    }

    return render(request, 'gender/delete.html', context)

def destroy_gender(request, gender_id):
    Gender.objects.filter(pk=gender_id).delete() # DELETE FROM genders WHERE gender_id = gender_id
    messages.success(request, 'Gender successfully deleted.')

    return redirect('/genders')

def index_user(request):
    users = User.objects.select_related('gender') # SELECT * FROM users LEFT JOIN ON users.gender_id = genders.gender_id

    context = {
        'users': users,
    }

    return render(request, 'user/index.html', context)

def create_user(request):
    genders = Gender.objects.all()  # SELECT * FROM Genders

    context = {
        'genders': genders
    }

    return render(request, 'user/create.html', context)

def store_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        birth_date = request.POST.get('birth_date')  
        gender_id = request.POST.get('gender_id')
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            encrypted_password = make_password(password)

            User.objects.create(
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                age=age,
                birth_date=birth_date,  
                gender_id=gender_id,
                username=username,
                password=encrypted_password,
            )

            messages.success(request, 'User successfully saved.')

            return redirect('/users')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('/users/create')


def delete_user(request, user_id):
    user = User.objects.get(pk=user_id)  # SELECT * FROM user WHERE user_id = user_id

    context = {
        'user': user,
    }

    return render(request, 'user/delete.html', context)

def destroy_user(request, user_id):
    User.objects.filter(pk=user_id).delete()
    messages.success(request, 'User successfully deleted.')

    return redirect('/users')

def show_user(request, user_id):
    user = User.objects.get(pk=user_id) #SELECT * FROM gender WHERE gender_id = gender_id

    context = {
        'user': user,
    }

    return render(request, 'user/show.html', context)

def edit_user(request, user_id):
    user = User.objects.get(pk=user_id)
    genders = Gender.objects.all()
    
    context = {
        'user': user,
        'genders': genders
    }
    
    return render(request, 'user/edit.html', context)

def update_user(request, user_id):
    if request.method == 'POST':    
        firstName = request.POST.get('first_name')
        middleName = request.POST.get('middle_name')
        lastName = request.POST.get('last_name')
        age = request.POST.get('age')
        birthDate = request.POST.get('birth_date')
        genderId = request.POST.get('gender_id')
        username = request.POST.get('username')

        User.objects.filter(pk=user_id).update(first_name=firstName, middle_name=middleName, last_name=lastName, age=age, birth_date=birthDate, gender_id=genderId, username=username)
        
        messages.success(request, 'User successfully updated.')
        
    return redirect('/users')
