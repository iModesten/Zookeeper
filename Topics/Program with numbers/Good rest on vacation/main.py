# put your python code here
duration_in_days = int(input())
total_food_cost = int(input())
flight_cost = int(input())
one_night_flight_cost = int(input())
print(duration_in_days * total_food_cost + 2 * flight_cost + one_night_flight_cost * (duration_in_days - 1))
