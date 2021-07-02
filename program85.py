#User function Template for python3

class Solution:
    def secFrequent(self, arr, n):
        # code here
        self.arr = arr
        self.n = n
        self.dic = { self.arr[0] : 1}
        for i in range(self.n):
            if i != 0:
                if self.arr[i] in self.dic.keys():
                    
                    self.dic[self.arr[i]] +=1
                    #print(self.arr[i] )
                    #print(self.dic)
                    #print(self.dic[arr[i]])
                else:
                    #print(self.arr[i] )
                    
                    self.dic[self.arr[i]]  =1
                    #print(self.dic)
            else:
                #self.v = self.dic[self.arr[i]] 
                #self.dic[self.v] = 1
                pass
                
        #print(self.dic)
        #print(sorted(self.dic.values())[-1])
        self.val = sorted(self.dic.values())[-2]
        #print(list(self.dic.keys())[list(self.dic.values()).index(self.val)])
        return (list(self.dic.keys())[list(self.dic.values()).index(self.val)])
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends