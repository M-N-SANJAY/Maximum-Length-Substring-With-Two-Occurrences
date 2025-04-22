'''
It uses a sliding window approach with two pointers: left and right, and a dictionary d to keep track of the frequency of characters within the current window. 
As it iterates over each character ch in the string, it increments the right pointer and updates the count of ch in the dictionary. 
If the count of any character exceeds 2, the window is shrunk from the left until the condition is satisfied. 
At each step, it updates Max to store the length of the longest valid window seen so far. Finally, it returns Max.
'''
def maximumLengthSubstring(s):
        d = {}
        Max = left = right = 0
    
        for ch in s:
            right += 1
            d[ch] += 1
          
            while d[ch] > 2:
                d[s[left]] -= 1
                left += 1
            
            Max = max(Max, right - left)    
        
        return Max  
'''
Time Complexity : O(n)
Space Complexity : O(k) where k is the number of unique characters present in the given string s.
'''
