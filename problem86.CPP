// { Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

 // } Driver Code Ends
class Solution{   
public:
    int minimumNumberOfSwaps(string s){
        // code here 
            int open = 0, close = 0;//open for storing count of '[' and close for ']'
     
    // ans stores the number of swaps
    //imbalance stores the current imbalance count
    int ans = 0 , imbalance = 0;
      
    for(int i = 0; i < s.length(); i++)
    {
        if (s[i] == '[')
        {
            // Incrementing open bracket count
            open++;
            if (imbalance > 0)//checking if imbalance>0 => close > open
            {
                // ans count is last ans count + imbalance
                ans += imbalance;
                // imbalance decremented by 1 as it solved
                imbalance--;    
            }
        }
        else if(s[i] == ']' )
        {
            // Incrementing close bracket count
            close++;
            // imbalance is calculated by substracting close bracket count from open.
            imbalance = (close - open);
        }
    }
    return ans;
    }
};

// { Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        string S;
        cin >> S;
        Solution ob;
        cout << ob.minimumNumberOfSwaps(S) << endl;
    }
    return 0; 
}   // } Driver Code Ends