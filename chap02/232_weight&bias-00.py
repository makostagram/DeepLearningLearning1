import numpy as np


'''
x = np.array([1, 1]) # input values
w = np.array([0.5, 0.5]) # weight values
b = -0.75

# calculation
print(x * w)
print(np.sum(x * w))
print(np.sum(x * w) + b)
if np.sum(x * w) + b <= 0:
    print('silent...')
elif np.sum(x * w) + b:
    print('explosion!')
'''

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.75
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

for i in range(2):
    for j in range(2):
        print(i, 'and', j, '->', AND(i, j))
        message = 'silence...' if AND(i, j) == 0 else 'explosion!'
        print(message)
        print()

'''
print(AND(0, 0))
print('silence...' if AND(0, 0) == 0 else 'explosion!')
print(AND(1, 0))
print('silence...' if AND(1, 0) == 0 else 'explosion!')
print(AND(0, 1))
print('silence...' if AND(0, 1) == 0 else 'explosion!')
print(AND(1, 1))
print('silence...' if AND(1, 1) == 0 else 'explosion!')
'''