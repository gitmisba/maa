p=93
g=9
print('the value of p is:%d'%(p))
print('the value of g is:%d'%(g))
a=4
print('the private key a for alici is:%d'%(a))
x=int(pow(g,a,p))
b=3
print('the private key b for bob is:%d'%(b))
y=int(pow(g,b,p))
ka=int(pow(y,a,p))
kb=int(pow(x,b,p))
print('the secetr key for alici is:%d'%(ka))
print('the secetr key for bob is:"%d'%(kb))
