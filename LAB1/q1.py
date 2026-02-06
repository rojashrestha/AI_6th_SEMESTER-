#Qn1
#variable and input/output operation 

name = input("What is your name ?")
age = input("What is your age?")
city = input("Where do you live?")

print("hello", name , 'your age is', age, 'and you are from', city)


#Q2
#arthimetic and data types

total_gb =float(input("total data used in this month ? (in GB):"))
price_gb = float(input(" The total price per GB?"))
total_bill = total_gb * price_gb 
avg_cost_per_mb = price_gb / 1024
projected_cost = total_bill*1.20

print(f"total bill: $ {total_bill}")
print("Total cost per mb: $" ,avg_cost_per_mb)
print("projected bill" ,projected_cost) 



#Q3
#Control Flow ( Condition and loops )
""" Write a validation scrtip to access 
the strenth of the user-provided password based on specific security criteria"""

password = input("Enter your password:")
if len(password) > 8  and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char in '!@#$%^&*()_+' for char in password):
    print("Strong Password")
else:
    print("Weak Password") 
    print("Password must be 8 Character long")




