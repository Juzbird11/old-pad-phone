
def old_phone_pad(stri):
    mapNumToChar = {
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ',
    }

    result = []

    i = 0
    while i < len(stri):
        inc = 1
        consec = 0

        if stri[i] == '#':
            break

        if stri[i] == '*' and len(result):
            result.pop()
            i += inc
            continue

        if stri[i] == ' ':
            i += inc
            continue

        if stri[i] == stri[i+1]:
            consec += 1
            inc += 1

            if stri[i+1] == stri[i+2]:
                consec += 1
                inc += 1

                if stri[i] == '7' or stri[i] == '9':

                    if stri[i+2] == stri[i+3]:
                        consec += 1
                        inc += 1

        result.append(mapNumToChar[stri[i]][consec])

        i += inc

    return ''.join(result)

print(old_phone_pad('33#'))
print(old_phone_pad('227*#'))
print(old_phone_pad('4433555 555666#'))
print(old_phone_pad('8 88777444666*664#'))