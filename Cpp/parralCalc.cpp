#include <omp.h>
#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, const char* argv[]){
    int num_steps=0;
    double delta=0.0;
    double sum=0.0;
    double expVal=0.0;
    
    
    cin>>num_steps;
    delta=log(2)/(7*num_steps);
    
    #pragma omp for
    for (int i=0;i<num_steps;i++){
        sum += exp(7*(delta)*i)+exp(7*(delta)*(i+1));
    }
    expVal=7*delta*sum;
    cout<<expVal<< endl;
    
    return 0;
}
