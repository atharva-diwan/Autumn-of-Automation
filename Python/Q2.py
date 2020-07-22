def is_palin(n):            #to check wether no. is a palindrome
  st=str(n)
  inv_st=[]
  for i in range(len(st)):
    inv_st.append(st[len(st)-i-1])
  
  if inv_st==list(st):
    return True
  else:
    return False
num=int(input())
if is_palin(num)==False:
  raise Exception("enter a palindrome")
while(True):               #finding next palindrome
  num=num+1
  if is_palin(num)==True:
    print(num)
    break
