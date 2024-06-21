def decrypt():
    s = input().strip()
    letters="abcdefghijklmnopqrstuvwxyz"
    n = int(input())
    res = ""
    for i in s:
        if i in letters:
            position = letters.find(i)
            j = (position - n) % 26
            nc = letters[j]
            res += nc
        else:
            res += i
    print(res)
decrypt()

#for i in a:
#    if((ord(i)-c)>=97):
#        d=d+chr(ord(i)-c)
#   else:
#       d=d+chr(ord(i)-c+26) print(d)