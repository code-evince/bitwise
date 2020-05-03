using namespace std;
#include<iostream>


int main()
{
    int x;
    cin>>x;
    cout<<x<<" ";
    
    while(x!=1)
    {
        
        if(x%2==0)
        {
            x/=2;
            cout<<x<<" ";
        }
        else
        {
            x= x*3 +1;
            cout<<x<<" ";
        }

    }
}