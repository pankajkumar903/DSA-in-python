def binary_search(array,left,right,x):
    if right >=left:
        mid = left + (right-left) // 2

        if array[mid] == x:
            return mid

        elif array[mid] >x:
            return binary_search(array,left,mid-1,x)

        else:
            return binary_search(array,mid+1,right,x)
    else:
        return 0

array=[10,20,30,40,50,60,70,80]
x=15

result = binary_search(array, 0, len(array) -1, x)

if result == 0:
    print("not able to find {} value in the array".format(x))
else:
    print("we found the item {} at {} position".format(x,result))
