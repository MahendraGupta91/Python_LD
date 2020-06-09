s='fgfg mahendra shivam anu mahi'
print(s+s)
print(s.strip()+s.strip())
s2=s.split(' ')
#for a in s2:
print(s2[0])
print(s2[1])
print(s2[2])
print(s2[3])
print(s2[4])
print("..................................................")
import re
s = "                    many      fancy                          word \nhello    \thi       "
s2=re.split('\s+', s.strip())
print(s2[0]+"   ")
print(len(s2[0]))
print(s2[1])
print(len(s2[1]))
print(s2[2])
print(len(s2[2]))
print(s2[3])
print(len(s2[3]))
print(s2[4])
print(len(s2[4]))

ss="pleased with your situation and not hoping for change or improvement:"
print(ss.strip(' :'))