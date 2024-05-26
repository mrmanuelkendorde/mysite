from django.db import models

class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True)  # BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    gender = models.CharField(max_length=55)  # VARCHAR(55) NOT NULL
    date_created = models.DateTimeField(auto_now_add=True)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    date_updated = models.DateTimeField(auto_now=True)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

    class Meta:
        db_table = 'genders'

    def __str__(self):
        return self.gender

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)  # BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    first_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55, blank=True)
    last_name = models.CharField(max_length=55)
    age = models.IntegerField()
    birth_date = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=55)
    date_created = models.DateTimeField(auto_now_add=True)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    date_updated = models.DateTimeField(auto_now=True)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

    class Meta:
        db_table = 'users'
