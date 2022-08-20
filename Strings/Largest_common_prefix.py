class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        small_list = []
        solution = ""
        
        for i in range(len(strs)):
            small_list.append(len(strs[i]))
            
        min_len = min(small_list)
        
        for i in range(min_len):
            temp = strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] == temp:
                    continue
                else:
                    return solution
            # temp.join(solution)
            solution = solution+temp
            
        return solution
