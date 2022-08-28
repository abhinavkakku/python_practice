from cgitb import small


def replace_pi(s):
    l = len(s)
    if l == 0 or l == 1:
        return s
    if s[0] == 'p' and s[1] == 'i':
        smallOutput = replace_pi(s[2:])
        return '3.14' + smallOutput
    else:
        smallOutput = replace_pi(s[1:])
        return s[0] + smallOutput


print(replace_pi('apippibcd'))
