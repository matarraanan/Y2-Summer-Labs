  import random

<<<<<<< HEAD:2.1 python review #1/python.py
=======

>>>>>>> 69259a4b8a9595f9ce93ab8c36c8484b5aa9726b:0.2 Python Review/python.py
def generate_temperatures():
    temperatures = []
    for _ in range(7):
        temperatures.append(random.randint(26, 40))
    print(temperatures)
    


def get_day(i):
    daysk = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return daysk[i]


def count_even_temperatures(temperatures):
    even_count = 0
    even_days = []
    for i in range(7):
        if temperatures[i] % 2 == 0:
            even_count += 1
            even_days.append(get_day(i))
            print("even" + even_count + "even days" )
    return even_count, even_days


def find_temperatures(temperatures):
    highest= max(temperatures)
    lowest= min(temperatures)
    highest_day = get_day(temperatures.index(highest))
    lowest_day = get_day(temperatures.index(lowest))
    return highest, highest_day, lowest, lowest_day


def average(temperatures):
    return sum(temperatures) / len(temperatures)


def above_average(temperatures, average_temp):
    above_avg = []
    for temp in temperatures:
        if temp > average_temp:
            above_avg.append(temp)
    return above_avg


