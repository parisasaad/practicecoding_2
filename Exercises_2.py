#Ask a user for two inputs
#Implement  (- , + , *, **, / , operations on them) and print the results.
#ubmit your code to GitHub Provide access to your peer to modify your code
#Ask your peer add the third input and apply its value to the output of previous operations, and print it. E.g., (2+2=4  new input Is 2  4*2, 4+2…)

############PARISA############3
Task_1 = int(input("Enter your first variable: "))
Task_2 = int(input("Enter your second variable: "))
addition = Task_1 + Task_2
Distributive_property = 2*Task_1 *(Task_1 - Task_2)
Division = Task_1 / Task_2

print ("addition: " , addition)
print ("Distributive_property: " , Distributive_property)
print ("Division: " , Division)
############Kamyar############3
Task_3 = int(input("Enter your Third variable: "))
addition = addition + Task_3
Distributive_property = 2*Distributive_property *(Distributive_property - Task_3)
Division = Distributive_property / Task_3

print ("addition made by peer: " , addition)
print ("Distributive_property  made by peer: " , Distributive_property)
print ("Division  made by peer: " , Division)
