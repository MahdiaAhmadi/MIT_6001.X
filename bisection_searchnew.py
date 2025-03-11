
x=25
epsilon=0.0001
high=x
low=1.0
numb_guessed=0

ans=(high+low)/2.0

while (ans**2 - x) >=epsilon:
    print('low: '+str(low)+'guess : '+str(numb_guessed)+'high : '+str(high))
    numb_guessed +=1
    if ans**2 < x:
        low=ans
    else: 
        high=ans
    ans=(high+low)/2.0

print('number guessed'+str(numb_guessed))
print('your square root is :'+ str(numb_guessed))



cube=27
guessed=0
high=cube
epsilon1=0.01
low=1.0
result=(high+low)/2.0

while (result **3 - cube)>=epsilon:
    if result**3 <cube:
        low=result
    else:
        high=result
    result=(high+low)/2.0
    guessed += 1
print('number guessed'+str(guessed))
print('your cube root is :'+ str(guessed))






