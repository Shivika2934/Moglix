class Solution(object):
    def longestValidParentheses(self, s):
        openlist=[-1]
        substr=0
        for i in range(len(s)):
            if s[i] =="(":
                openlist.append(i)
            else:
                openlist.pop()
                if len(openlist)==0:
                    openlist.append(i)
                else:
                    substr=max(substr,i-openlist[-1])                
        return substr
        
