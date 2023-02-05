from gettext import find


def finddata(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
print(finddata([1, 5, 8, 3], 3))
print(finddata([5, 8, 3], -1))