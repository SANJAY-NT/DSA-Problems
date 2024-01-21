class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        count = 0
        j = bank[0]
        i = 1
        # loop throught the list and find the row with 1
        while i < len(bank):
            #if "1" in j:
            if "1" in bank[i]:
                # count and get the sum of the 1's in i and jth rows and set j as the jth row
                count += (j.count('1') * bank[i].count('1'))
                j =  bank[i]
                i += 1
            else:
                i += 1
            #if j has no 1's make the temp 
            # else:
            #     j =  bank[i] 
            #     i += 1

        return count
