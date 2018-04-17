/*
 * Header file for the discrete fourier transform
 * program.
 *
 *
 *
*/ 


#ifndef FASTFT
#define FASTFT

#include <iostream>
#include <cmath>
#include <vector>

typedef struct compl_num {
    double real;
    double imag;
} compl_num;

typedef struct frequency {
    double value; // What is the frequency?
    double magnitude; // How much of the frequency?
//  double phase_shift;
} frequency;

class FastFT {
    public:

        /* FastFT constructor
        * Description: performs a discrete fourier transform on a vector of amplitudes where the
        * index represents time at that location and the value is the amplitude of the signal at that time.
        *
        * Arguments: unsigned long sample frequency--> the sample rate of the signal analyzed.
        *            vector<double>& amplitudes--> a vector passed by reference containing the signal data vs time
        *            vector<double>& frequencies--> a vector passed by reference of size 0 to contain the calculated
        *                                           frequencies.
        */

        FastFT(unsigned long sample_rate, std::vector<double> amplitudes, 
            std::vector<frequency>& frequencies, char useWindow = ' ');

    private:
        
        /**
         * Prepare the data for fourier analysis.
         * 1) Zero padding increases the length of the
         *    input data to the next power of two.
         * 2) ApplyHanningWindow applies the hanning
         *    window function to the data to reduce aliasing.
         * 3) ReverseBitVector reduces the bit order of the vector to make it work well with the Cooley-Tuckey FFT algorithm.
        */
        bool IsPowOfTwo(unsigned long val);
        unsigned long MakePowOfTwo(unsigned long val);
        unsigned TakeLogTwo(unsigned long val);
        void ZeroPad();
        void ApplyHanningWindow();
        void BitReverseVector(std::vector<double>& vector_to_reverse, unsigned long size);
        
    
        /**
         * Calculate the real and imaginary parts of the "amount
         * each frequency exists in the signal  for each sample
         * point.
        */

        void CalcFFT();
        void CalcFrequencies();
        unsigned long sample_rate; 
        unsigned long spectral_lines;
        unsigned long N; // Number of samples
        double frame_size;
           
        /**
         * Holds the amplitude data of samples in a signal.
        */ 
        std::vector<double> amplitudes;
        std::vector<compl_num> compl_amplitudes;        

        /** Pointer to an array of calculated frequencies */	

        std::vector<frequency>* frequencies;
};

#endif
