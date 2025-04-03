#Creating my list
my_list = []

#Appending my list with values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


print("1)", my_list)

#my_list[10,20,30,40]
#Inserting the value 15 into the second position on the list 
my_list.insert(1,15)
print("2)",my_list)

#Extending my list with another list called list2 50,60,70
list2 = [50,60,70]
my_list.extend(list2)

print("3)",my_list)

#Removing the last element from the list which is 70
my_list.remove(70)
print("4)",my_list)

#Sorting the list in ascending order
my_list.sort()
print("5)",my_list)

#finding and printing the index of the value 30 in a list
#Using for with an if statement to find and print the index
for num in my_list:
    if num == 30:
        print("6)", "Value:",num, "Index is:", my_list.index(num))