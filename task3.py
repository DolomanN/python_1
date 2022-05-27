pi = 3.1415926
str_pi = str(pi)
str_pi = str_pi.replace('.', '')
lst_str = list(str_pi)
lst_num = map(int, lst_str)
s = sum(lst_num)
print (s)