'''

list1 = [8, 2, 3, 0, 7]
def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)
 
total = sumOfList(list1, len(list1))
 
print("Sum of all elements in given list: ", total)

'''

def sum_of_list(l):
  total = 0
  for val in l:
    total = total + val
  return total

my_list = [8,2,3,0,7]
print ("The sum of my_list is", sum_of_list(my_list))