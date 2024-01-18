# YourApp/views.py
from django.shortcuts import render
from django.db.models import Avg
from task1.models import Student
from faker import Faker
import random
import time
import redis



def calculate_average_age(request):
    # Connect to the Redis server
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    # Check if the average_age is present in Redis
    average_age = redis_client.get('average_age')
    start_time = time.time()

    if average_age is not None:
        # If found in Redis, convert from bytes to float
        average_age = float(average_age.decode('utf-8'))
        from_redis = True
    else:
        # If not found in Redis, calculate using Django's aggregate function
        average_age = Student.objects.aggregate(Avg('age'))['age__avg']

        # Store the calculated average_age in Redis
        redis_client.set('average_age', str(average_age))
        from_redis = False
    end_time = time.time()
    execution_time = end_time - start_time



    # Get all students for display purposes (you might not need this in your actual application)
    all_students = Student.objects.all()

    return render(request, 'average_age.html', {'average_age': average_age, 'from_redis': from_redis,'execution':execution_time} )



def generate_average_age():
    fake = Faker()

    for _ in range (1,70):
        for _ in range(10000):
            # Generate a random name
            name = fake.name()

            # Generate a random age between 18 and 25
            age = random.randint(18, 25)

            # Create a Student object and save it to the database
            student = Student(name=name, age=age)
            student.save()

