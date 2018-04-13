#include <iostream>
#include "df_trans.h"
#include <vector>
#include <cmath>
using namespace std;




int main() {

    vector<double> amplitudes;
    vector<double> frequencies; 
    long sample_frequency = 8;
    double input;

    cout << endl << "Please enter a sample frequency: " << endl;
    cin >> sample_frequency;
    cout << "Please enter the y-coordinate of the point at n/N (where N/f = 1s and n is the current point): "
         << endl;
    for (int i = 0; i < sample_frequency; i++) {
        cin >> input;
        cout << "You entered: f(" << i << ") = " << input << endl;
        amplitudes.push_back(input);
    }

    df_trans dft(amplitudes, sample_frequency);
    frequencies = *(dft.get_frequencies_ptr());

    for (unsigned i = 0; i < frequencies.size(); i++) {
        if ((round(frequencies.at(i)))) {
            cout << i << "hz : " << round(frequencies.at(i)) << endl;
        }
    }

    return 0;

}
