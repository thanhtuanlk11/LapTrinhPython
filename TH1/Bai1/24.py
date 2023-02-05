from ctypes.wintypes import WORD


def check(char):
    work = 'aeiou'
    return char in work
print(check('y'))
print(check('e'))