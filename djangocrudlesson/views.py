from django.shortcuts import render, redirect
from .models import Gender, User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

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
                password=encrypted_password
            )

            messages.success(request, 'User successfully saved.')

            return redirect('/users')
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('/users/create')
        