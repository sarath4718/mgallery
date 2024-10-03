from django.db import models

#Create your models here.

class GenreChoices(models.TextChoices):

    ACTION='Action','Action'

    THRILLER='Thriller','Thriller'

    ROMANCE='Romance','Romance'

# GENRE_CHOICES = [('Action','Action'),('Fiction','Fiction')]

class Movies(models.Model):

    title=models.CharField(max_length=200)

    genre=models.CharField(max_length=200,choices=GenreChoices.choices)

    language=models.CharField(max_length=200)

    year=models.CharField(max_length=200)

    run_time=models.PositiveIntegerField()

    director=models.CharField(max_length=200)

# class Employee(models.Model):

#     name=models.CharField(max_length=30)

#     designation=models.CharField(max_length=200)

#     department=models.CharField(max_length=200)

#     contact=models.CharField(max_length=200)

#     salary=models.IntegerField()

#     address=models.CharField(max_length=200)

# class ClassesChoice(models.IntegerChoices):
#     c1=1,1
#     c2=2,2
#     c3=3,3
#     c4=4,4
#     c5=5,5
#     c6=6,6
#     c7=7,7
#     c8=8,8
#     c9=9,9
#     c10=10,10

# class DivisionChoice(models.TextChoices):
#     div1='A','A'
#     div2='B','B'
#     div3='C','C'
#     div4='D','D'

# class Student(models.Model):

#     name=models.CharField(max_length=200)
#     class1=models.CharField(max_length=200,choices=ClassesChoice.choices)
#     division=models.CharField(max_length=50,choices=DivisionChoice.choices)
#     rollno=models.CharField(max_length=50)
#     about_me=models.TextField()
#     image=models.ImageField()
#     url=models.URLField()

# class FuelChoice(models.TextChoices):
#     PETROL='Petrol','Petrol'
#     DIESEL='Diesel','Diesal'
#     Electric='Electric','Electric'

# class SeatChoice(models.IntegerChoices):
#     s1=2,2
#     s2=4,4
#     s3=6,6
    
# class Car(models.Model):
#     name=models.CharField(max_length=200)
#     model=models.CharField(max_length=200)
#     fuel_type=models.CharField(max_length=50,choices=FuelChoice.choices)
#     Date=models.DateField()
#     no_of_seat=models.PositiveIntegerField(choices=SeatChoice.choices)
#     image=models.ImageField()
#     url=models.URLField()
#     stock=models.BooleanField()

