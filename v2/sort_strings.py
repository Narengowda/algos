x  = ['naren', 'nami', 'apple', 'ball', 'zeta']

out = []

def chars_to_num(string):
    return ''.join(map(str, [ord(a) for a in string]))

print([chars_to_num(a) for a in x])

