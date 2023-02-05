import string


def stringx(str, n):
  length = 2
  if length > len(str):
    length = len(str)
  substr = str[:length]
  
  result = ""
  for i in range(n):
    result = result + substr
  return result
print(stringx('nam', 2))
print(stringx('p', 6));