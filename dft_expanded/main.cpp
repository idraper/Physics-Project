#include <iostream>
#include <fstream>
#include <sstream>
#include "df_trans.h"
#include <vector>
#include <cmath>
#include <string>
#include <limits>
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
 
double GetInput(double inputType) {
    double input = 0.0;
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
 * ReadInFile: takes in a .csv file of format double,double (#,#)
 * where the first column represents the time and the second column
 * represents the value at that time and pushes those values into the
 * vector amplitudes.
 *
 * arguments;
 * ifsteam& infile: the input file
 * amplitudes: the vector to push values to.
 * sample_frequency: sample frequency of the signal.
 *
*/

int ReadInFile(ifstream& inFile, vector<double>& amplitudes, unsigned long sample_frequency = 128000) {
    double tmp = 0.0;
    char extra_char = ' ';
    istringstream inStream;
    string line;
         
    getline(inFile, line);
    if (inFile.fail()) {
        cout << "Error in reading data. Terminating program." << endl;
        return 1;
    }

    // check for end of file
    while (!inFile.eof() && !(amplitudes.size() == sample_frequency)) { 
        // process data line by line
        cout << line << endl; 
        //Remove commas from input .csv file
        inStream.str(line);
        inStream >> extra_char;
        inStream >> tmp; // get rid of time value
        inStream >> extra_char; //get rid of comma
        cout << tmp;
        inStream >> tmp; // value to use
        cout << tmp << endl;
        amplitudes.push_back(tmp);
        getline(inFile, line);
    }
    
   
    return 0;
}

/**
 * ReadInInput returns a sampling frequency and modifies the vector amplitudes.
 * vector<double> amplitudes: the vector in which to store data from user input.
*/

unsigned long ReadInInput(vector<double>& amplitudes) {
    unsigned long sample_frequency = 0;
    double input = 0.0; 
    cout << "Please enter a sample frequency: " << endl;
    sample_frequency = GetInput(sample_frequency);
    cout << "Please enter the y-coordinate of the point at n/N (where N/f = 1s and n is the current point): "
        << endl;

    for (unsigned i = 0; i < sample_frequency; i++) {
        input = GetInput(input);
        cout << "You entered: f(" << i << ") = " << input << endl;
        amplitudes.push_back(input);
    }
    return sample_frequency;
}

int main() {

    vector<double> amplitudes;
    vector<double> frequencies; 
    unsigned long sample_frequency = 8;
    char choice = ' ';
    string path;
    bool useFile = false;

    cout << endl;
    
    // Repeat until user enters correct input to choose input type
    while (!((choice == 'y') || (choice == 'n'))) { 
        cout << "Do you wish to enter data using a file or the command line? enter y/n" << endl;
        choice = GetInput(choice); 
    }
    useFile = (choice == 'y');

    // Procedures to use a file
    // File must be in format: #,#
    if (useFile) {
       cout << "What is the path to the .csv file you wish to open?" << endl;
       GetInput(path);
       ifstream inFile(path.c_str());
   
       // Was there an error opening the file?
       if (inFile.fail()) {
           cout << "Error reading file. Terminating execution." << endl;
           return 1;
        }

        cout << "Please enter the sample frequency. (Default = 128000)." << endl;
        sample_frequency = GetInput(sample_frequency);
        cout << "You entered: " << sample_frequency << endl;
        if(ReadInFile(inFile, amplitudes, sample_frequency)) {
            return 1;
        }
    }
    
    // User inputs data by hand.   
    else {
        sample_frequency = ReadInInput(amplitudes);    
    }
    
    // Perform the computations
    df_trans dft(amplitudes, sample_frequency);
    frequencies = *(dft.get_frequencies_ptr());

    // Print calculated frequencies with weights >= 1 to screen.
    for (unsigned i = 0; i < frequencies.size(); i++) {
        if ((round(frequencies.at(i)))) {
            cout << i << "hz : " << (frequencies.at(i)) << endl;
        }
    }

    return 0;

}
