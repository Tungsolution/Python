import re
def FindTheSame(s):
    for i in range(len(s) -1):
        A = re.findall(s[i],s)
        print A
        if len(A) >1:
            return ''.join(A)
    return ""
print FindTheSame("AaabbcAdeefAA")