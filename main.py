# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)

#get total number of items in list
len_of_names = len(names)
#print(len_of_names)

rand_name = random.randint(0, len_of_names-1)
# print(rand_name)
who_pay = names[rand_name]
print(f'{who_pay} is going to buy the meal today')