#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#define N_PI 3.1415926535897

using std::cout;
using std::cerr;
using std::cin;
using std::endl;
using std::ofstream;

typedef struct signal {
    double t; // time
    double x; // displacement
} signal;


int main() {
    unsigned long sample_rate = 0;
    unsigned long sample_size = 0;
    double frame_size = 0.0;
    double deltaT = 0.0; 
    double omega = N_PI * 2.0;
    double frequency = 0.0;
    signal tmp;
    tmp.t = 0.0;
    tmp.x = 0.0;
    std::vector<signal> data; 
     
    // Do cosine wave
    cout << "What should be the sample frequency?" << endl;
    cin >> sample_rate;
    cout << "You entered: " << sample_rate << endl;;
    
    cout << "How many samples should be generated?" << endl;
    cin >> sample_size;
    cout << "You entered: " << sample_size << endl;

    cout << "What frequency should be used?" << endl;
    cin >> frequency;
    cout << "You entered: " << frequency << endl;

    omega = omega * frequency;
    frame_size = (double) sample_size / (double) sample_rate;
    deltaT = 1.0 / (double)sample_rate;
   
    cout << endl << "Derived constants: " << endl;
    cout << "Omega: " << omega << endl;
    cout << "Total time: " << frame_size << endl;
    cout << "Spacing in time: " << deltaT << endl;


    for (unsigned int i = 0; i < sample_size; i++) {
        tmp.t = (double)i * deltaT;
        tmp.x = 100 * cos(omega * tmp.t);

#ifdef DEBUG_ON
        cout << "@time: " << tmp.t << "; x = " << tmp.x << endl;
#endif

        data.push_back(tmp);
    }
   
 
    cout << "Writing to file data_sig.csv... " << endl;
    ofstream outFile("data_sig.csv");

    if (outFile.fail()) {
        cerr << "Unable to write to file. Terminating program." << endl;
        return 1;
    }
    
    for (unsigned int i = 0; i < data.size(); i++) {
        outFile << data.at(i).t << "," << data.at(i).x << endl;
    }
    
    outFile.close();
    cout << "...Done." << endl;

    return 0;
}  
