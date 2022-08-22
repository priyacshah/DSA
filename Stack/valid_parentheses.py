class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check=False
        i=0
        test = []
        top=-1
        
        while i <len(s):
            if s[i] in ['{', '(', '[']:
                test.append(s[i])
                top+=1
            else:
                if top >=0 and ((s[i] == '}' and test[top] == '{')
                or (s[i] == ']' and test[top] == '[')
                or (s[i] == ')' and test[top] == '(')):
                    test.pop(top)
                    top-=1
                else:
                    return False
            i+=1

        return len(test)==0
