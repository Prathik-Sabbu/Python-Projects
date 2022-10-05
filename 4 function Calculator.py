First = input("first value:")
Second= input("second value:")
operator=input('Operator:')
if operator == "+":
    sum=float(First)+float(Second)
    print(sum)
elif operator == "/" and Second == "0":
    print("und")
elif operator == "-":
    sum=float(First) - float(Second)
    print(sum)
elif operator == "/":
    sum=float(First) / float(Second)
    print(sum)
elif operator == "*":
    sum=float(First) * float(Second)
    print(sum)
elif operator == "^":
    sum=float(First)**float(Second)
    print(sum)
Continue = input("continue (yes) or (no):")
while Continue == "yes":
    First = sum
    Second = input("second value:")
    operator = input('Operator:')
    if operator == "+":
        sum = float(First) + float(Second)
        print(sum)
    elif operator == "/" and Second == "0":
        print("und")
    elif operator == "-":
        sum = float(First) - float(Second)
        print(sum)
    elif operator == "/":
        sum = float(First) / float(Second)
        print(sum)
    elif operator == "*":
        sum = float(First) * float(Second)
        print(sum)
    elif operator == "^":
        sum = float(First) ** float(Second)
        print(sum)
    Continue = input("continue (yes) or (no):")
if Continue == "no":
    print(sum)