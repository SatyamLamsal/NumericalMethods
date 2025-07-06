#include<stdio.h>
#include<math.h>
#include<stdlib.h>

int main()
{
    int i,j,n,k;
    float a[50][50],r,s=0,x[50];
    printf("Enter the number of equations");
    scanf("%d",&n);
    printf("Enter the coefficients of equation");
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n+1;j++)
        {
            scanf("%f",&a[i][j]);
        }
    }
    for(j=1;j<=n-1;j++)
    {
        for(i=j+1;i<=n;i++)
        {
            r=a[i][j]/a[j][j];
            for(k=1;k<=n+1;k++)
            {
                a[i][k]=a[i][k]-r*a[j][k];
            }
        }
    }
    x[n]=a[n][n+1]/a[n][n];
    for(i=n-1;i>=1;i--)
    {
        s=0;
        for(j=i+1;j<=n;j++)
        {
            s=s+a[i][j]*x[j];
        }
        x[i]=(a[i][n+1]-s)/a[i][i];
    }
    printf("The solutions are:\n");
    for(i=1;i<=n;i++)
    {
        printf("x[%d]=%f\n",i,x[i]);
    }
    return 0;
}



