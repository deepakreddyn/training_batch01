# ip:khoor
plaintext=input()
n=int(input())
def encrypt_text(plaintext,n):
    ans = ""
    for i in range(len(plaintext)):
        ch = plaintext[i]
        if ch==" ":
            ans+=" "
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans
print(encrypt_text(plaintext,n))

