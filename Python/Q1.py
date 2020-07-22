n_digit=int(input())
def is_prime(N):            #function to check whether no. is prime
  if N==1:
    return False
  for i in range(2,N):
    if N%i==0:
      return False
    
    else:   
      continue
  return True
f = open("myFirstFile.txt", "w")
for i in range(10**(n_digit-1),10**(n_digit)-1):
  if is_prime(i)==True and is_prime(i+2)==True:

    print(str(str(i)+' '+str(i+2))+'\n',file=f)       #writing to text file
f.close()
