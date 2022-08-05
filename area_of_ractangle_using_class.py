class area:
    def __init__(self,length,bidth):
        self.length=length
        self.bidth=bidth
print("the previous length of ractangle is:-")
a=area(0,0)
print(a.length)
print("the previous length of ractangle is:-")
print(a.bidth)
a.length=int(input("please enter the value of length-  "))
a.bidth=int(input("please enter the value of bidth-  "))
print("updated length or bidth")
print(a.length,"cm")
print(a.bidth,"cm")
print("the area of ractangle is: ",a.length*a.bidth,"cm^2")