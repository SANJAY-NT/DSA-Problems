class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        # if len(arr)==1:
        #     return len(arr[0])
        # if len(arr) == 0:
        #     return 0
        # else:
        #     long_char = max(arr, key = len)
        #     if len(set(long_char)) != len(long_char):
        #         return 0
        #     arr.remove(long_char)
        #     for i in long_char:
        #         for j in arr:
        #             if i in j:
        #                 arr.remove(j)
        #     print(arr)
        #     return sum ([len(long_char),self.maxLength(arr)])

        def can_concatenate(s1, s2):
            """
            Check if s2 can be concatenated to s1 without introducing duplicate characters.
            """
            return len(set(s1) & set(s2)) == 0 and len(s2) == len(set(s2))

        def backtrack(arr, path="", max_length=[0]):
            """
            Backtrack through the array of strings to find the maximum length of a unique character string.
            """
            # Update the maximum length
            max_length[0] = max(max_length[0], len(path))

            # Iterate over the array to concatenate strings
            for i in range(len(arr)):
                if can_concatenate(path, arr[i]):
                    # Choose the current string to concatenate and move to the next
                    backtrack(arr[i+1:], path + arr[i], max_length)

        max_length = [0]
        backtrack(arr, "", max_length)
        return max_length[0]




        
