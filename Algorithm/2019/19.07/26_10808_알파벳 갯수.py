words = list(map(str,input()))
alphabet = [0*i for i in range(26)]

for i in words:
    if i == 'a':
        alphabet[0] += 1
    elif i == 'b':
        alphabet[1] += 1
    elif i == 'c':
        alphabet[2] += 1
    elif i == 'd':
        alphabet[3] += 1
    elif i == 'e':
        alphabet[4] += 1
    elif i == 'f':
        alphabet[5] += 1
    elif i == 'g':
        alphabet[6] += 1
    elif i == 'h':
        alphabet[7] += 1
    elif i == 'i':
        alphabet[8] += 1
    elif i == 'j':
        alphabet[9] += 1
    elif i == 'k':
        alphabet[10] += 1
    elif i == 'l':
        alphabet[11] += 1
    elif i == 'm':
        alphabet[12] += 1
    elif i == 'n':
        alphabet[13] += 1
    elif i == 'o':
        alphabet[14] += 1
    elif i == 'p':
        alphabet[15] += 1
    elif i == 'q':
        alphabet[16] += 1
    elif i == 'r':
        alphabet[17] += 1
    elif i == 's':
        alphabet[18] += 1
    elif i == 't':
        alphabet[19] += 1
    elif i == 'u':
        alphabet[20] += 1
    elif i == 'v':
        alphabet[21] += 1
    elif i == 'w':
        alphabet[22] += 1
    elif i == 'x':
        alphabet[23] += 1
    elif i == 'y':
        alphabet[24] += 1
    else:
        alphabet[25] += 1


for k in alphabet:
    print(k, end=' ')