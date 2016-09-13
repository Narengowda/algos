

signature = {}

def gen_signature(num):
    signature = [num]
    count = 2
    while True:
        newnum = (num ** count) % 10
        if signature[0] == newnum:
            return signature
        else:
            signature.append(newnum)
            count += 1

def main():
    num = int(raw_input('Enter base: '))
    powr = int(raw_input('Enter power: '))

    last_dig = num % 10

    if not signature.get(last_dig):
        signature[last_dig] = gen_signature(last_dig)

    num_sig = signature[last_dig]
    num_sig_len = len(num_sig)

    print 'Last digit: ', num_sig[(powr-1) % num_sig_len]


while True:
    main()

