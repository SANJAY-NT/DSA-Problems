class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
      #define a list
        final_list = []
      # for numbers in the list 
        for i in nums:
            present =  0
          #iterate the list of list and check ifits not present in any list 
            for j in final_list:
                if i not in j:
                  # if not present add the number to that list 
                    j.append(i)
                    present = 1
                    break
            # if its present in all the list create a new list and append 
            if present == 0:
                final_list.append([i])
            
        return final_list
        
