# def fact(exp):
#     assert exp>0 ,"this is less number for factorial"
#     if exp in [0,1]:
#         return 1
#     else:
#         return exp*fact(exp-1)
# exp=int(input())
# print(fact(exp))


# def sum(exp):
#     assert exp>=0 and int(exp)==exp ,"this is small number for fabonacci"
#     if exp ==0:
#         return 0
#     else:
#         return int(exp%10) + sum(exp//10)
# print(sum(-541))


# def power(base, exp):
#     assert exp>=0 and int(exp)==exp ,"this is small number for fabonacci"
#     if exp==0:
#         return 1
#     if exp==1:
#         return 0
#     return (base + power(base, exp-1))
# print(power(3,))

def gcd(a,b):
    assert int(a)==a and int(b)==b, "the number should be integer only"
    if a<0:
        a= -1*a
    if b<0:
        b= -1*b
    if b==0:
        return a
    return gcd(b, a%b)
print(gcd(48,18))