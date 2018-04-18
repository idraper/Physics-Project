#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>
#include <string>
#include <limits>
#include "FastFT.h"

//#ifndef DEBUG_ON
//#define DEBUG_ON
//#endif

using namespace std;

const long long CIN_IGNORE = std::numeric_limits<streamsize>::max();

unsigned long GetInput(unsigned long inputType) {
    unsigned long input = 0;
    cin >> input;
    if (cin.fail()) {
        cin.clear();
    }
    cin.ignore(CIN_IGNORE,'\n');
    return input;
}
 
long double GetInput(long double inputType) {
    long double input = 0.0;
    cin >> input;
    if (cin.fail()) { 
        cin.clear();
    }
    cin.ignore(CIN_IGNORE,'\n');
    return input;
}

char GetInput(char inputType) {
    char input = ' ';
    cin >> input;
    if (cin.fail()) {
        cin.clear();
    }
    cin.ignore(CIN_IGNORE,'\n');
    return input;
}

void GetInput(string& input) {
    getline(cin, input);
    return;
}

/**
 * ReadInFile: takes in a .csv file of format long double,long double (#,#)
 * where the first column represents the time and the second column
 * represents the value at that time and pushes those values into the
 * vector amplitudes.
 *
 * arguments;
 * ifsteam& infile: the input file
 * amplitudes: the vector to push values to.
 * sample_rate: sample frequency of the signal.
 *
*/

int ReadInFile(ifstream& inFile, vector<long double>& amplitudes, unsigned long& sample_size) {
    long double tmp = 0.0;
    istringstream iString;
    char separator = ',';
    string line;
    string fluff;
         
    if (inFile.fail()) {
        cerr << "Error in reading data. Terminating program." << endl;
        return 1;
    }

    // check for end of file
    while (!inFile.eof() && (amplitudes.size() != sample_size)) {        
        getline(inFile, line);
        iString.str(line);
        // get rid of unnecessary info to extract amplitude values
        getline(iString, fluff, separator);
        iString >> tmp;
        amplitudes.push_back(tmp); 
        iString.clear();
    }

    return 0;
}

/**
 * ReadInInput returns a sampling frequency and modifies the vector amplitudes.
 * vector<long double> amplitudes: the vector in which to store data from user input.
*/

unsigned long ReadInInput(vector<long double>& amplitudes, unsigned long sample_size) {
    unsigned long sample_rate = 0;
    long double input = 0.0; 
    cout << "Please enter a sample frequency: " << endl;
    sample_rate = GetInput(sample_rate);
    cout << "Please enter the y-coordinate of the point at n/N (where N/f = 1s and n is the current point): "
        << endl;

    for (unsigned i = 0; i < sample_size; i++) {
        input = GetInput(input);
        cout << "You entered: f(" << i << ") = " << input << endl;
        amplitudes.push_back(input);
    }
    return sample_rate;
}

/**
 * Output the frequency data to a file.
*/

int OutputData (vector<frequency>& frequencies) {
    cout << "Outputting data to file output.csc";
    ofstream outFile("output.csv");

    if (outFile.fail()) {
        cerr << "Error opening file for writing. Terminating program." << endl;
        return 1;
    }

    for (unsigned long i = 0; i < frequencies.size(); i++) {
        outFile << frequencies.at(i).value << "," << frequencies.at(i).magnitude << endl;
    }

    outFile.close();    
    return 0;
}
    


int main() {

    vector<long double> amplitudes;
    vector<frequency> frequencies; 
    unsigned long sample_size = 0;
    unsigned long sample_rate = 0;
    char choice = ' ';
    string path;
    bool useFile = false;

    cout << endl;


    cout << "Please enter the sample size of the data to process." << endl;
    cin >> sample_size;
    
    // Repeat until user enters correct input to choose input type
    while (!((choice == 'y') || (choice == 'n'))) { 
        cout << "Do you wish to enter data using a file or by hand? Enter 'y' for file input." << endl;
        choice = GetInput(choice); 
    }

    useFile = (choice == 'y');

    // Procedures to use a file
    // File must be in format: #,#
    if (useFile) {
       cerr << "What is the path to the .csv file you wish to open?" << endl;
       GetInput(path);
       ifstream inFile(path.c_str());
   
       // Was there an error opening the file?
       if (inFile.fail()) {
           cerr << "Error reading file. Terminating execution." << endl;
           return 1;
        }
        
        cout << "Please enter the sample frequency." << endl;
        sample_rate = GetInput(sample_rate);
        cout << "You entered: " << sample_rate << endl;
        if (ReadInFile(inFile, amplitudes, sample_size)) {
            inFile.close();
            return 1;
         
        }
        inFile.close();
        
    }

    // User inputs data by hand.   
    else {
        sample_rate = ReadInInput(amplitudes, sample_size);    
    }

    cout << "Do you wish to apply the Hann window function? Enter 'w' to do so." << endl;
    cin >> choice;

    // Perform the computations
    cout << "ampltidues.size()" << amplitudes.size();
    FastFT fft(sample_rate, amplitudes, frequencies, choice);

    for (unsigned i = 0; i < frequencies.size(); i++) {
        if (frequencies.at(i).magnitude > 0.0) {
            cout << frequencies.at(i).value << "hz : " << frequencies.at(i).magnitude << endl;
        }
    }
    
    OutputData(frequencies);

    return 0;

}
