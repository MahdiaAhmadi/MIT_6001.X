

def genPrime():
     x=2 # first prime number
     prime =[] # to store the found prime num

     while True:
          is_prime= True
          for p in prime:
               if x %p==0:
                    is_prime = False
                    break
               
          if is_prime:
              prime.append(x)
              yield x
          x +=1

prime_gen = genPrime()  # Create generator instance

for p in range(5):  # Print first 5 prime numbers
    print(next(prime_gen))



     
    
    


