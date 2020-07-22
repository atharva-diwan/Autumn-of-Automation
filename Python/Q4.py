import numpy as np

def normal_eq(x,y):
  assert(x.shape[0] == y.shape[0])
  temp1=np.linalg.inv(np.dot(x.T,x))
  temp2=np.dot(temp1,x.T)
  theta=np.dot(temp2,y)
  return theta
x=np.random.normal(size=(20,20))
y=np.random.rand(20,1)
print(normal_eq(x,y))
