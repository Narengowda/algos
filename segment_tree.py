odata = range(16)


out = []

def construct(data):
    if len(data) >= 2:
        fh = data[:len(data)/2]
        sh = data[len(data)/2:]
        fho = construct(fh)
        sho = construct(sh)
        return fho + sho
    else:
        return [{"data": data[0]}]


print construct(odata)
