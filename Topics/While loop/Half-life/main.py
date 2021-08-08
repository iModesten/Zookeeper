initial_quantity = int(input())
final_quantity = int(input())
count_of_periods = 0
while initial_quantity > final_quantity:
    initial_quantity = initial_quantity // 2
    count_of_periods += 1
print(count_of_periods * 12)
