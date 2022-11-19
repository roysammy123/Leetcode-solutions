/*
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
/*


//  SOLUTION:

int reverse(int x){
    int n,a;
    long double sum;
    sum=0;
    a=x;
    while (x!=0)
    {
        n=x%10;
        sum=(sum*10)+n;
        x=x/10;
    }

    if (-2147483648 <=sum && sum <= 2147483647)    
        return sum;
    else
        return 0;
}
