a='abcdefghijklmnopqrstuvwxyz'
b = 'aman'
c= " "
i=0
c = c +(a[((a.index(b[i]))+1)%26] )
c = c +(a[((a.index(b[i+1]))+1)%26] )
c= c +(a[((a.index(b[i+2]))+1)%26] )
c= c +(a[((a.index(b[i+3]))+1)%26] )
print(c)  