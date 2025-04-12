#Problem: First Unique Character in a String
#Given a string s, return the index of the first non-repeating character.
# If there is no such character, return -1.

#Input: "leetcode"
#Output: 0  # 'l' is the first unique

#Input: "loveleetcode"
#Output: 2  # 'v' is the first unique

#Input: "aabb"
#Output: -1  # no unique character

#Approach:
#Use a hashmap to count how many times each character appears.
#Then go through the string again to find the first character with count 1.

def unique_char(Input):
 dict1 = dict.fromkeys(Input,0)   # {'l': 0, 'e': 0, 't': 0, 'c': 0, 'o': 0, 'd': 0}
 for i in Input:
    dict1[i] +=1

 for idx,char in enumerate(Input):
     if dict1[char] ==1:
        return idx 
 return -1

Input= "leetcode"
resp = unique_char(Input)
print(resp)
