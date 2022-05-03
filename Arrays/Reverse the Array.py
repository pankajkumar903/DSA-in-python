# Iterative python program to reverse an array

# Function to reverse A[] from start to end
def reverseList(A, start, end):
	while start < end:
		A[start], A[end] = A[end], A[start]
		start += 1
		end -= 1

# Driver function to test above function

A = eval(input("Enter the value of x:"))  # [1, 2, 3, 4, 5]
print("list is")
reverseLists = A[::-1]
print("Reversed list is")
print(reverseLists)
