# Task: To Implement a logical expression evaluator
# Expression is stored in the form of a JSON array and uses standard logical
# operators [AND, OR, NOT] and the following arithmetic
# operators: EQUALS (EQ), GREATER THAN (GT), LESS THAN (LT), CONTAINS (IN)
# An expression always follows the
# format: [OPERATOR, OPERAND, COMPARISON_VALUE(S)]
# Few example expressions follow: rAND", ["EQ", "user.address.city", "Los Angeles"], rGT", "user.age", 35]]
#  ["OR'; [IN", "event.category", [``infant", "child", "teen"]],["LT", "user.age", 18] ]
# The input will be a JSON object such as
# {"user":{"address":{"address_line":"XYZ Street", "city":"San Francisco", "state":"CA", "zipcode": "94150"}}} and the expression should evaluate to TRUE or FALSE
# The OPERAND & COMPARISION_VALUE(S) could refer to a value in the input object or be an absolute value.


# Using eval it will be simple.
# This implementation is without eval

import simplejson

context = {
    "event": {
        'category': 'child'
    },
    "user":
        {
            "age": 19,
            "address":
                {
                    "address_line":"XYZ Street",
                    "city":"San Francisco",
                    "state":"CA",
                    "zipcode": "94150"}}}

inp = ["OR", ["IN", "event.category", ["infant", "child", "teen"]], ["LT", "user.age", 18] ]

#inp = ["AND", ["EQ", "user.address.city", "Los Angeles"], ["GT", "user.age", 35]]


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
