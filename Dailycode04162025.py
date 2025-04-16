 # "Find Peak Element" using binary search

#input = [1,2,3,1]
#output = 2
# element 3 at index 2 is peak element

#input = [1,2,1,3,5,6,4]
#output = 2
# element 3 at index 2 is peak element

def Peak_element(nums):
  l=0
  h= len(nums)-1
  
  while l<=h:
    m= l + (h-l) //2
    if (m==0 or nums[m-1]< nums[m]) and (m == (len(nums)-1) or nums[m+1] < nums[m]):
      return m
    elif m>0 and nums[m-1] > nums[m]:
      h = m-1
    else:
      l = m+1
  
  return -1

nums =[1,2,3,1]
resp = print(Peak_element(nums))
