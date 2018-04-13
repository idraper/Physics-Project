/*
 * Header file for the discrete fourier transform
 * program.
 *
 *
 *
*/ 


#ifndef DF_TRANS
#define DF_TRANS


#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

class df_trans {
    public:
        /**
         * Constructors
        */

        df_trans(vector<double>& amplitudes, unsigned long sample_frequency);
        vector<double>* get_frequencies_ptr(); 
        

    private:
           
        /**
         * Calculate the real and imaginary parts of the "amount
         * each frequency exists in the signal  for each sample
         * point.
        */
         
        void calc_parts();
        void calc_magnitudes();
        void calc_frequencies();
      
        /**
         * Holds the amplitude data of samples in a signal.
        */ 
        vector<double> amplitudes;        

        /**
         *  Holds the real part of "how much" each
         *  vector is in each frequncy
        */
        vector<double> real_part;
        vector<double> imag_part;
        vector<double> magnitudes;

        /** Array of calculated frequencies */	
        vector<double> frequencies;
        unsigned long nyquist_limit;
        unsigned long N; // Number of samples
        unsigned long sample_frequency; 
};

#endif
