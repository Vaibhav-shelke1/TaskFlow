arr=[1,1,0,-1,-1]
count1=0
count0=0
count2=0
for i in arr:
    if i>0:
        count1+=1
    elif i==0:
        count0+=1
    else:
        count2+=1   
print("{:6f}".format(count1/len(arr)))       
print("{:6f}".format(count0/len(arr)))      
print("{:6f}".format(count2/len(arr)))     
  
           