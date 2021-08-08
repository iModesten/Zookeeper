sum_of_deposit = int(input())
years = 0
while 50000 < sum_of_deposit < 700000:
    sum_of_deposit += sum_of_deposit * 7.1 / 100
    years += 1
print(years)
