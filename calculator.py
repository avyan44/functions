def add (p,q):
    return p+q
def substract(p,q):
    return p-q
def multiply (p,q):
   return p*q
def divide (p,q):
    return p/q
print("please select the operation")
print("a.add")
print("b.substract")
print("c. multiply")
print("d.divide")
choice = input("please enter choice(a/b/c/d/):")
num_1= int (input("please enter the first number"))
num_2= int (input("please enter the second number"))
if choice == "a":
    print(add (num_1,num_2))
elif choice =="b" :
    print(substract (num_1,num_2))
elif choice =="c":
    print(multiply (num_1,num_2))
elif choice =="d":
    print(divide (num_1,num_2))
else:                      
    print("this is an invalid input")
