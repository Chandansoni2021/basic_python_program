from datetime import date
today = date.today()
print("Today date is: ", today)
s=str(today)
f=""
for i in range(0,4):
    f=f+s[i]
print("please enter year to know your age: ")
n=int(input())
g=n-int(f)
print(g)
