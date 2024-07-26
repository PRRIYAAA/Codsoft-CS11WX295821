a=int(input("Enter number 1"))
b=int(input("Enter  number 2"))
operator=input("Enter the operator: ").strip()
if operator=='+':
    print('Add =',a+b)
elif operator=='-':
    print('Subtract =',a-b)
elif operator=='*':
    print('Multiply =',a*b)
elif operator=='%':
    if b!=0:
        print('Modulus =',a%b)
    else:
        print('division is not allowed')
elif operator=='/':
    if b!=0:
        print('Divide =',a/b)
    else:
        print('division is not allowed')
elif operator=='**':
    print('Exponent =',a**b)

print('Thank you')
    