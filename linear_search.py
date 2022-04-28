def linear_search(arr, length, item):

    for i in range(0, length):
        if arr[i] == item:
            return i

    return 0


arr = ['a','b','c','d']
item = input("enter then value that you'd want to search: ")

length = len(arr)

result = linear_search(arr, length, item)

if result == 0:
    print("The item {} was not found".format(item))
else:
    print("The Value {} was found {} index".format(item, result))
