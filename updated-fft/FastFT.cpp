#include <cmath>
#include <iostream>
#include <vector>
#include "FastFT.h"
//#define DEBUG_ON

using std::cout;
using std::pow;
using std::sqrt;
using std::endl;

/* FastFT constructor
 * Description: performs a discrete fourier transform on a vector of amplitudes where the
 * index represents time at that location and the value is the amplitude of the signal at that time.
 *
 * Arguments: unsigned long sample frequency--> the sample rate of the signal analyzed.
 *            vector<long double> amplitudes--> a vector passed containing the signal data vs time
 *            vector<long double>& frequencies--> a vector passed by reference of size 0 to contain the calculated
 *                                           frequencies.
*/

FastFT::FastFT(unsigned long sample_rate, std::vector<long double> amplitudes, 
    std::vector<frequency>& frequencies, char useWindow) :
        sample_rate(sample_rate), amplitudes(amplitudes), frequencies(&frequencies) { 
    char window = 'w';

    // Derived quantities //
    this->N = this->amplitudes.size();
    cout << this->N << " How is this a power of two? " << endl;

    // tmp val for initizalizing complex vector
    compl_num tmp;
    tmp.real = 0.0;
    tmp.imag = 0.0;

    // Apply windowing function to data if desired
    if (useWindow == window) {
        cout << "Applying Hann Window " << endl;
        ApplyHanningWindow();
    }

    // Change the length of the data block to a power of two.
   

    if (!IsPowOfTwo(this->N)) {
        cout << "Zero padding vector " << endl; 
        ZeroPad();  
        cout  << "...Done zero padding." << endl;
    }

    this->spectral_lines = N / 2;
    this->N = this->amplitudes.size();
    this->frame_size = (long double)N / (long double)sample_rate; 

    // Order the vector in bit-reversed index order. (See Readme for more details).
    cout << "Starting bit reversal" << endl;
    BitReverseVector(this->amplitudes, this->N);
    cout << "... Bit reversal done." << endl;

    cout << "Initializing complex vector..." << endl;
    // Prepare data for complex operations
    for (unsigned long i = 0; i < N; i++) { 
        tmp.real = this->amplitudes.at(i);
        this->compl_amplitudes.push_back(tmp);
    }
    cout << "Initialization done..." << endl;

      
 
    // Calculations to determine magnitude of each frequency //
    cout << "Calculating FFT..." << endl;
    CalcFFT();
    cout << "...FFT analysis done." << endl;
    cout << "Processing frequencies..." << endl;
    CalcFrequencies();
    cout << "...Done" << endl;
    return;
}

/**
 * Check if a value is a power of two.
 *
*/

bool FastFT::IsPowOfTwo(unsigned long val) {

    unsigned long comparator = 1;
    bool isPow = false;

    while (comparator < val) {
        comparator = comparator << 1;
    }

    if (val == comparator) {
        isPow = true;
    }
    cout << "is power of two: " <<  isPow << endl;
    return isPow;
}

/**
 * Make a value into the next power of two.
 *
*/

unsigned long FastFT::MakePowOfTwo(unsigned long val) {
    unsigned long comparator = 1;
    
   if (val > comparator) {

        while (val > comparator) {
            comparator <<= 1;
            cout << val << " " << comparator << endl;
        }
    }

    else if (val < comparator) {
        comparator = 1;
    }

    return comparator;
}

/**
 * Take log two of a number--assume power of two
*/

unsigned FastFT::TakeLogTwo(unsigned long val) {
    unsigned result = 0;
    while (val > 1) {
        val >>= 1;
        result++;
    }
    return result;
}

/**
 *
 * Zero pad the signal data to the next power of two.
 *
*/

void FastFT::ZeroPad() {
    unsigned int oldN = this->N;

    this->N = MakePowOfTwo(this->N);
    for (unsigned int i = 0; i < this->N - oldN; i++) {
        this->amplitudes.push_back(0);
    }

    return;
}

/** 
 * Applies the Hanning window function to input signal data.
 * The function is: w[n] = 1/2 (1 - cos ((2 Pi n) / (N - 1)))
*/

void FastFT::ApplyHanningWindow() {
    const long double k = 2 * M_PI / (this->N - 1);
    
    for (unsigned long n = 0; n < this->N; n++) {
        this->amplitudes.at(n) = this->amplitudes.at(n) * (1.0/2.0 * (1.0 - cos(k * (long double)n)));
    }

    return;
}

/**
 * Recursive algorithm to shuffle the elements of the input signal to
 * be in bit-reversed order.
*/

void FastFT::BitReverseVector(std::vector<long double>& vector_to_reverse, unsigned long size) {
    std::vector<long double> even;
    std::vector<long double> odd;
    unsigned long stride = 2;

    // Base case: a vector of size 2 is already bit-reversed.
    if (size == stride) {
        return;
    }

    // Populate the even and odd vectors with their respective values.   
    for (unsigned long i = 0; i < (size); i += stride) {
         even.push_back(vector_to_reverse.at(i));
    }
    
    for (unsigned long i = 1; i < (size); i += stride) {
        odd.push_back(vector_to_reverse.at(i));
    }

    // Perform the recursion on each subset of even / odd vectors.
    BitReverseVector(even, even.size());
    BitReverseVector(odd, odd.size()); 

    // Compile the even vector to the first half of the starting vector...
    for (unsigned long i = 0; i < size/stride; i++) {
        vector_to_reverse.at(i) = even.at(i);
    }

    // ...and the odd to the second half.
    for (unsigned long i = 0; i < size/stride; i++) { 
        vector_to_reverse.at(size/stride + i) = odd.at(i);
    }

#ifdef DEBUG_ON
    cout << "Reversed vector : " << endl;
    for (unsigned long i = 0; i < size; i++) {
        cout << vector_to_reverse.at(i) << " ";
    }   
    cout << endl;
#endif
    return;
}

/**
 * Calculate the real and imaginary parts of the "amount
 * each frequency exists in the signal  for each sample
 * point.
 * 
 * Uses formula X_k = Sum[x_k * e^(i(2 Pi n k)/N)]
*/

void FastFT::CalcFFT() {
    unsigned long num_stages = TakeLogTwo(N) - 1; 
    unsigned long curr_stage = N;

    // Complex numbers
    // Hold the even val of the FFT
    compl_num even;
    even.real = 0.0;
    even.imag = 0.0;

    // Hold the odd val of the FFT
    compl_num odd;
    odd.real = 0.0;
    odd.imag = 0.0;

    // Hld the twiddle factor
    compl_num twiddle1;
    twiddle1.real = 0.0;
    twiddle1.imag = 0.0;

    compl_num twiddle2;
    twiddle2.real = 0.0;
    twiddle2.imag = 0.0;

    // Tmp number for the WnK table creation
    compl_num tmp;
    tmp.real = 0.0;
    tmp.imag = 0.0;

    // The twiddle factor base value
    long double WN = M_PI * 2.0 / (long double)N;
    cout << " WN: " << WN << endl;
    
    for (int i = 0; i < 0; i++) {}    


    /** This is the actual FFT.
     * It operates based on the Cooley & Tukey method--taking an N sample DFT and subdividing it
     * into 2 N/2 sample DFTS, breaking up the signal vector until it operates on 2 1point DFTS (which is easy to calculate).
     * This algorithm works in place instead of recursively, though it can also be done with recursion.
     * 
     * Example of flow for N = 2 FFT, where W_N^k = e^(-i 2 Pi K / N)
     *         x1
     * x[0]---------_-- 
     *     `-.    .-`| xW_N^k   
     *        `-.`
     *     .-`   `_| x1
     * x[1]-------------
     *         x -W_N^k   
    */      
 
    for (unsigned long big_jump = N >> num_stages; big_jump <= N; big_jump <<= 1) {
        unsigned long little_jump = big_jump >> 1;
        curr_stage = curr_stage >> 1;
        cout << "Current stage : " << TakeLogTwo(curr_stage) << endl;
        cout << "Big jump: " << big_jump << endl;
        cout << "Little jump: " << little_jump << endl;
        // Step through "big jump" of elements 
        for (unsigned long i = 0; i < N; i += big_jump) {
            for (unsigned long k = 0; k < little_jump; k++) {

                unsigned long index1 = k + i; 
                unsigned long index2 = k + i + little_jump;                

                // Get the Wn^K Twiddle factors
                unsigned long k_1 = (k * curr_stage);
                unsigned long k_2 = k_1 + N/2;
                long double WnK_1 = WN * (long double) k_1;
                long double WnK_2 = WN * (long double) k_2;                

                

/*
                twiddle1.real = cos (WnK_1);
                twiddle1.imag = sin (WnK_1); 
                twiddle2.real = cos (WnK_2);
                twiddle2.imag = sin (WnK_2);             
*/

                // Get the real & imaginary parts for the "odd" index
                twiddle1.real = cos (WnK_1);
                twiddle1.imag = sin (WnK_1); 

                // Get the real & imaginary  parts for the "even" index
                even.real = compl_amplitudes.at(index1).real;
                even.imag = compl_amplitudes.at(index1).imag;
                odd.real = twiddle1.real * compl_amplitudes.at(index2).real 
                    - twiddle1.imag * compl_amplitudes.at(index2).imag;
                odd.imag = twiddle1.real * compl_amplitudes.at(index2).imag 
                    + twiddle1.imag * compl_amplitudes.at(index2).real;

                compl_amplitudes.at(index1).real = even.real + odd.real;
                compl_amplitudes.at(index1).imag = even.imag + odd.imag;
                compl_amplitudes.at(index2).real = even.real - odd.real;
                compl_amplitudes.at(index2).imag = even.imag - odd.imag;
                
/*

                // Top part of butterfly               
                // Real calculations
                compl_amplitudes.at(index1).real = even.real + twiddle1.real * odd.real - twiddle1.imag * odd.imag;
 
                // Imaginary calculations
                compl_amplitudes.at(index1).imag = even.imag + twiddle1.real * odd.imag + twiddle1.imag * odd.imag;

                // Lower part of butterfly
                // Real calculations
                compl_amplitudes.at(index2).real = even.real + twiddle2.real * odd.real - twiddle2.imag * odd.imag;
                
                // Imaginary Calculations
                compl_amplitudes.at(index2).imag = even.imag + twiddle2.real * odd.imag + twiddle2.imag * odd.imag;

*/
            }
        }
    }
 
#ifdef DEBUG_ON
    cout << endl;
    for (unsigned long i = 0; i < N/2; i++) {
        cout << "Re[f(" << i << ")] : " << compl_amplitudes.at(i).real << " " << " Im[f(" << i << ")] : " << compl_amplitudes.at(i).imag << endl;
    }
    cout << endl;
#endif
    
    return;
}

/**
 * Calculate the amount of each frequency
  1st. Calculate the magnitude of each frequency below
       the Nyquist limit.
  2nd. Mulitply by 2 and average out over the # of samples.

*/

void FastFT::CalcFrequencies() {
    frequency tmp;
    tmp.value = 0.0;
    tmp.magnitude = 0.0;

    for (unsigned long i = 0; i < spectral_lines;  i++) {
        
        // Calculate the actual frequnecy of the frequency bin
        tmp.value = i / frame_size;
        
        // Find the magnitude of the frequency
        tmp.magnitude = sqrt(pow(compl_amplitudes.at(i).real, 2.0) + pow(compl_amplitudes.at(i).imag, 2.0)); 

        // Normalize the results
        tmp.magnitude = (tmp.magnitude * 2.0) / (long double) N; 
        frequencies->push_back(tmp);

    }
   
#ifdef DEBUG_ON
    unsigned abs_max_i = 0;
    for (unsigned long i = 0; i < spectral_lines; i++) {
        if (tmp.magnitude < frequencies->at(i).magnitude) {
            tmp.magnitude = frequencies->at(i).magnitude;
            abs_max_i = i;
        }
        cout << "Frequencies : " << this->frequencies->at(i).value << " " <<
            this->frequencies->at(i).magnitude << endl;
    }

    cout << "abs_max_i: " << abs_max_i;
#endif
    
    return;
}

