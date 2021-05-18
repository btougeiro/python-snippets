import random

names = [ "Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie" ]

students_scores = { student:random.randint(1, 100) for student in names }

passed_students = { student:score for (student, score) in students_scores.items() if score >= 60 }

## little exercise 1

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = { word:len(word) for word in sentence.split() }
print(result)

## little exercise 2

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

weather_f = { day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items() }
print(weather_f)
