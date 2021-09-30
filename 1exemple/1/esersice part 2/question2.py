d=int(input("pick a date: "))
m=int(input("pick a month: "))
y=int(input("pick a year: "))
a=y%10
b=y//10%10
print(f"{d}/{m}/{a}{b}")