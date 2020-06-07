import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

with open("CartpoleDQN.txt", "r") as f:
    lines=f.readlines()
    result=[]
    for x in lines:
        result.append(x.split(' ')[4])
    f.close()
    
result = [float(i) for i in result]
av_result=[]
n=1
for i in range(0, len(result), n):
    if i==len(result)-n:
        break
    av=sum(result[i:i+n])//n
    av_result.append(av)

with open("Cartpole_regression_ridge.txt", "r") as f:
    lines=f.readlines()
    result1=[]
    for x in lines:
        result1.append(x.split(' ')[4])
    f.close()
    
result1 = [float(i) for i in result1]
av_result1=[]
for i in range(0, len(result1), n):
    if i==len(result1)-n:
        break
    av=sum(result1[i:i+n])//n
    av_result1.append(av)

with open("Cartpole_regression_KNN_10_2.txt", "r") as f:
    lines=f.readlines()
    result1=[]
    for x in lines:
        result1.append(x.split(' ')[4])
    f.close()
    
result1 = [float(i) for i in result1]
av_result2=[]
for i in range(0, len(result1), n):
    if i==len(result1)-n:
        break
    av=sum(result1[i:i+n])//n
    av_result2.append(av)


y = np.arange(len(av_result))
plt.plot(y, av_result, 'r--', label='DQN')
plt.plot(y, av_result1, 'p-', label='Ridge')
plt.plot(y, av_result2, 'y-', label='KNN')
plt.xlabel('episode')
plt.ylabel('Score')
#plt.title('Linear approximators')
plt.legend()
plt.show()
plt.savefig('NN_KNN_Ridge.png', bbox_inches='tight')