
def replaceChar(s, a, b):
    l = len(s)
    if l == 0:
        return s
    smalleroutput = replaceChar(s[1:], a, b)
    if s[0] == a:
        return b + smalleroutput
    else:
        return s[0] + smalleroutput


print(replaceChar("dacdxcd", 'c', 'x'))
