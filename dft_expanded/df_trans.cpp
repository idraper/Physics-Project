#include <cmath>
#include <iostream>
#include "df_trans.h"
#define DEBUG_ON

using namespace std;

// FIXME: don't assume that amplitudes size == sample_frequency

df_trans::df_trans(vector<double>& amplitudes, unsigned long sample_frequency) { 
    this->amplitudes = amplitudes;
    this->N = amplitudes.size();
    this->sample_frequency = sample_frequency;
    this->nyquist_limit = sample_frequency / 2;
    calc_parts();
    calc_magnitudes();
    calc_frequencies();
}

/**
 * Calculate the real and imaginary parts of the "amount
 * each frequency exists in the signal  for each sample
 * point.
 * 
 * Uses formula X_k = Sum[x_k * e^(i(2 Pi n k)/N)]
*/

void df_trans::calc_parts() {
    double tmp = 0.0;
    // Real parts (Real[e^(i theta)] = cos theta)
    for (unsigned long k = 0; k < N; k++) {
        for (unsigned long n = 0; n < N; n++) {
            tmp += this->amplitudes.at(n) * cos((2 * M_PI * k * n) / N);
        }
        this->real_part.push_back(tmp);
        tmp = 0;
    }
    
    // Imaginary parts (Imaginary[e^(i theta)] = sin theta)
    for (unsigned long k = 0; k < N; k++) {
        for (unsigned long n = 0; n < N; n++) {
            tmp += this->amplitudes.at(n) * sin((2 * M_PI * k * n )/ N);
        }
        this->imag_part.push_back(tmp);
        tmp = 0.0;
    }
    
#ifdef DEBUG_ON
    for (unsigned int i = 0; i < N; i++) {
        cout << "Re[f(" << i << ")] : " << this->real_part.at(i) << right << "\t\t" << "Im[f(" << i <<")] : " << this->imag_part.at(i) << endl;
    }
#endif
    
    return;
}

/**
 * Calculate the magnitudes using the Pythagorean theorem in the complex plane.
*/

void df_trans::calc_magnitudes() {
    double tmp = 0.0;
    for (unsigned long i = 0; i < N; i++) {
        tmp = sqrt(pow(this->real_part.at(i), 2.0) 
            + pow(this->imag_part.at(i), 2.0));
        this->magnitudes.push_back(tmp);
    }
 
#ifdef DEBUG_ON
    for (unsigned long i = 0; i < N; i++) {
        cout << "Magnitudes : " << i << " " <<  this->magnitudes.at(i) << endl;
    }
#endif
    
    return;
}

/**
 * Calculate the frequencies using samples below the nyquist limit, multiplying the magnitudes
 * by two and averaging out over the number of samples taken.
*/

void df_trans::calc_frequencies() {
    double tmp = 0.0;
    for (unsigned long i = 0; i < this->N - this->nyquist_limit; i++) {
        tmp = 2 * this->magnitudes.at(i) / N;
        this->frequencies.push_back(tmp);
    }
    return;
}        

vector<double>* df_trans::get_frequencies_ptr() {
    return &frequencies;
}
