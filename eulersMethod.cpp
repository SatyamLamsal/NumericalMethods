#include <iostream>
using namespace std;

float f(float x, float y)
    {
        return x - y;
    }

float euler(float x0, float y0, float h = 0.2)
    {
        float Data[2][100];
        cout << " x0\t\ty0"<<endl;
        for(int i=0; i < 100; i ++)
        {
            cout <<x0<<"\t\t"<<y0<<endl;
            y0 = (y0 + h * f(x0,y0));
            x0 += h; 

        }        
    }

    int main ()
    {

        euler(0,1,0.2);
        return 0;
    }