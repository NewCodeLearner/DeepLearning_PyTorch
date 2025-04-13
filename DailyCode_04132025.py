#Find the maximum sum for a window size 3 in an given array
#sliding window technique

def find_max_sum(arr,window):

    curr_sum =sum(arr[:window])
    max_sum =curr_sum
    n=len(arr)
    for i in range(window,n):
        print(f' {i} curr_sum', curr_sum)
        print(f' {i} max_sum', max_sum)
        curr_sum = curr_sum + arr[i] - arr[i-window]
        if curr_sum > max_sum:
           max_sum = curr_sum
          
    return max_sum

arr =[1,3,6,8,11,1,4,6]
window=3
resp = find_max_sum(arr,window)
print(resp)
