#include <stdio.h>
int main()
{
    int temp, x, y, z;
    for (int i=100; i<1000; i++)
    {
        temp = i;
        z = temp%10;
        temp = temp/10;
        y = temp%10;
        temp = temp/10;
        x = temp%10;
        if (i == (x*x*x)+(y*y*y)+(z*z*z))
        {
            printf("Armstrong is %d\n",i);
        }
    }
    return 0;
}