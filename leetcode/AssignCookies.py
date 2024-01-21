class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        j = 0
        # loop through the g list 
        for i in range(len(g)):
            #for every value in g see if a value in s whihc is equal or greater than that 
            while j < len(s):
                # if yes then take that value position as the next jth value to search for the next value in g
                if s[j] >= g[i]:
                    #s.remove(s[j])
                    count += 1
                    j += 1
                    break
                else:
                    j +=1
            # if s is small and we exceed the limit so break the last loop
            if count > len(s):
                break
        return count
        
