// solution structure
/* struct Interval
 {
     int buy;
     int sell;
 };*/
// This function finds the buy sell schedule for maximum profit
void stockBuySell(int a[], int n)
{
    Interval in[n/2];
    int l=0;
    int c=0;
    while(l<n-1){
        while(a[l]>a[l+1] && l<n-1) l++;
        if(l==n-1) break;
        in[c].buy=l;
        l++;
        
        while(a[l]>a[l-1] && l<n) l++;
        in[c].sell=l-1;
        c++;
    }
    if(c==0) cout<<"No Profit";
    for(int i=0;i<c;i++){
        cout<<"("<<in[i].buy<<" "<<in[i].sell<<")"<<" ";
    }
    
}