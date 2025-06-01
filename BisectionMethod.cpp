#include <iostream>
#include <vector>

// this is test for git ok ??
using namespace std;

class BisectionMethod
{
    // for function     ax^2 + bx + c = 0;
    private :    
    int a,b,c;
    double root;
    int NoOfIterations = 100;
    double range_1,range_2,tempc;
    
    
    public:
    BisectionMethod(){}

    BisectionMethod(int a,int b, int c): a(a),b(b),c(c), root(-1.0){range_1=6; range_2= 7; tempc = 0;}

    double FunctionVal(double x)
    {
        
        return (a*x*x + b*x + c);
    }

    bool CalculateRoot()
    {   
      
        if((FunctionVal(range_1) * FunctionVal(range_2) )> 0 ) return false;
        while(NoOfIterations>0)
        {
        
              
        tempc= (range_1 + range_2)/2;
        if((FunctionVal(tempc)>0 )&& (FunctionVal(range_1)<0)) {range_2 = tempc;} else {range_1 = tempc;}
         
        NoOfIterations--;
            
        }
      
        root = tempc;
        return true;
    }

    void displayRoot()
    {
            cout << " Positive Root : "<< root<<endl;
    }


};

class Interpolation
{
    private:
    vector<vector <float>> Val;

    public:
    Interpolation(){}
    Interpolation(vector<vector <float>> Value) : Val(Value){}

    bool CreateFxn()
    {

        return false;
    }
    
    double ValueAt(int x)
    {
        return 0.0;
    }
        


};

int main ()

{
    int a =1, b=-7, c = 2;
    BisectionMethod SqFxn(a,b,c);
    if(SqFxn.CalculateRoot()) SqFxn.displayRoot(); else { cout << "Error !! "<<endl;}

    vector<vector<float>> Val = {{2,3},{3,6},{4,12},{5,24}};
    Interpolation Intp;
    Intp.CreateFxn();
    cout << " Val : " << Intp.ValueAt(3);


} //cout<<"Before ::" <<"range_1 : "<<range_1<<" range_2: "<<range_2<< " Tempc: " << tempc << " Fxn val : "<< FunctionVal(tempc)*FunctionVal(range_1)<<endl;
    


#include <iostream>
int main (int argc, char* argv[])
{
    std::cout<<"Hello World"<<std::endl;
    return 0;
}


class Person{
private:
    int a,b,c,d,e;
public:

Person(int a,int b,int c,int d, int e):a(a),b(b),c(c),d(d),e(e){}


};

