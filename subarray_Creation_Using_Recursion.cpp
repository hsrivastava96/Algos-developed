#include <bits/stdc++.h>
#include <vector>
using namespace std;

void subarray(vector<int> a, vector<int> subset, int i)
{
    if(i == a.size())
    {
        for(int j = 0; j<subset.size(); j++)
            cout<<subset[j]<<"\t";
        cout<<endl;
        return;
    }
    else
    {
        subset[i] = NULL;
        subarray(a, subset, i+1);
        subset[i] = a[i];
        subarray(a, subset, i+1);
    }
    return;
}

int main()
{
    vector<int> a = {1, 2, 3, 4};
    vector<int> subset = {NULL, NULL, NULL, NULL};
    
    subarray(a, subset, 0);
    
    return 0;
}
