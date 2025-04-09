
#find the common and non-coomon elements from the given lists.

list1=[1,2,3,4]
list2=[2,3,4,6]


output1=[]
output2=[]

for i in list1:
  flag = False
  for j in list2:
    if i ==j:
      flag =True
      break
  if flag:
    output2.append(i)
  else:
    output1.append(i)

for j in list2:
    if j not in list1:
     output1.append(j)
        
    
print("Output1 : ",output1)
print("Output2 : ",output2)
