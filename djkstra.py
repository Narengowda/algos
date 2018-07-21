paths = {
    'a':{
        'b':5,
        'c':10
    },
    'b':{
        'e':3,
        'd':6,
    },
    'e':{
        'c':2,
        'd':2,
        'g':2
    },
    'd':{
        'f':6,
    },
    'g': {
        'f':2
    }
}


visited = []
stack = ['a']
values = {'a': 0,
          'b':99999,
          'c':99999,
          'd':99999,
          'e':99999,
          'f':99999,
          'g':9999
          }

while len(stack):
    curr = stack[0]
    curr_value = values[curr]
    stack = stack[1:]
    visited.append(curr)
    for c in paths.get(curr, []):
        if c not in visited:
            stack.append(c)
        if values[c] > (curr_value + paths.get(curr)[c]):
            values[c] = curr_value + paths.get(curr)[c]


print values


