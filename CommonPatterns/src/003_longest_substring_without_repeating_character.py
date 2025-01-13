class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mmax = 0
        
        for i in range(len(s)):
            offset = mmax + i + 1   # +1 for a[start:stop] items start through stop-1
            while offset <= len(s):
                if len(s[i:offset]) == len(set(s[i:offset])):
                    mmax += 1
                    offset += 1
                else:
                    break
                
        return mmax