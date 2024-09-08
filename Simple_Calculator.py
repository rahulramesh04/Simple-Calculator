print("      \n\n       SIMPLE  CALCULATOR      \n\n    ")

num1=int(input("Enter your First Number: "))
num2=int(input("Enter your Second Number: "))
print("\n\nPress 1 to Add both numbers.\n\t  2 to Subtract both numbers.\n\t  3 to Multiply both numbers.\n\t  4 to Divide both numbers.\n\t  5 to find the reminder of both numbers.\n\t  6 to Find the Exponential(power) of both numbers.");
op=input("\nEnter your choice: ")

if(op=='1'):
   res=num1+num2
   print("\nYou chose Addition:")
   print("%d + %d = %d"%(num1,num2,res))


elif(op=='2'):
    res=num1-num2
    print("\nYou chose Subtraction:")
    print("%d - %d = %d3f" % (num1, num2, res))


elif(op=='3'):
    res=num1*num2
    print("\nYou chose Multiplication:")
    print("%d x %d = %d" % (num1, num2, res))


elif(op=='4'):
    if(num2!=0):
       res=num1/num2
       print("\nYou chose Divition:")
       print("%d / %d = " % (num1, num2),float(res))
    else:
        print("Division not possible when the denominator(second number) is zero \n\tPlease try again!")


elif(op=='5'):
    res=num1%num2
    print("\nYou chose Modular:")
    print("%d (mod%d) = %d" % (num1, num2, res))


elif(op=='6'):
    m=int(input("Enter the power of the First number: "))
    n=int(input("Enter the power of the Second number: "))

    a =num1 ** m
    b =num2 ** n
    print("The %dth power of %d is : %d" %(m,num1,a))
    print("The %dth power of %d is : %d" %(n,num2,b))






