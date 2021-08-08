# put your python code here
students_number_of_first_group = abs(int(input()))
students_number_of_second_group = abs(int(input()))
students_number_of_third_group = abs(int(input()))
number_of_desk_for_first_class = students_number_of_first_group // 2 + students_number_of_first_group % 2
number_of_desk_for_second_class = students_number_of_second_group // 2 + students_number_of_second_group % 2
number_of_desk_for_third_class = students_number_of_third_group // 2 + students_number_of_third_group % 2
print(number_of_desk_for_first_class + number_of_desk_for_second_class + number_of_desk_for_third_class)
