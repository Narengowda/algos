
import simplejson

context = {
    "event": {
        'category': 'child'
    },
    "user":
        {
            "check": True,
            "age": 19,
            "address":
                {
                    "address_line":"XYZ Street",
                    "city":"San Francisco",
                    "state":"CA",
                    "zipcode": "94150",
                    "check": False
                }}}

inp = ["OR", ["IN", "event.category", ["infant", "child", "teen"]], ["LT", "user.age", 18] ]
inp =  ["AND", ["IN", "user.address.city", ["infant", "child", "teen"]],["LT", "user.age", 18]]
inp =  ["OR", ["EQ", "user.address.check", ["EQ", "user.address.city", "Los Angeles"]],["LT", "user.age", 18]]

def exp_or(a, b):
    return a or b

def exp_and(a, b):
    return a and b

def exp_gt(a, b):
    return a > b

def exp_lt(a, b):
    return a < b

def exp_eq(a, b):
    return a == b

def exp_in(a, b):
    return a in b

def get_val(var_str):
    if isinstance(var_str, int) or var_str.isalpha():
        return int(var_str)

    try:
        data = context
        for var in var_str.split('.'):
            data = data[var]
        return data
    except (KeyError, AttributeError) as e:
        print "just note: ", e
        return var_str

exp_map = {
    'OR': exp_or,
    'AND': exp_and,
    'GT': exp_gt,
    'LT': exp_lt,
    'EQ': exp_eq,
    'IN': exp_in
}

def process(expression):
    op, vo, vt = expression


    if op != 'IN':
        if isinstance(vo, list):
            vo = process(vo)
        else:
            vo = get_val(vo)

        if isinstance(vt, list):
            vt = process(vt)
        else:
            vt = get_val(vt)

        out = exp_map[op](vo, vt)
        print '> Evaluating ', vo, op, vt, '=', out
        return out


    else:
        vo = get_val(vo)
        out = exp_map[op](vo, vt)
        print '> Evaluating ', vo, op, vt, '=', out
        return out


output = process(inp)
print '--' * 20
print "Evaluated expression {} ----> {}".format(inp, output)
