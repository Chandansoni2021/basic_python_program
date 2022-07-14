def biggest(array,n):
    if n==1:
        return array[0]
    else:
        return max(array[n-1],biggest(array,n-1))
    
array=[2,3,4,3,55,644,44,3]
n=len(array)
print(biggest(array,n))
