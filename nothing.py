d = {}
d2 = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)
        d2[chr((i+13) % 26 + c)] = chr(i+c)

scramble = lambda x: ''.join([d2.get(c, c) for c in x])
unscramble = lambda x: ''.join([d.get(c, c) for c in x])
