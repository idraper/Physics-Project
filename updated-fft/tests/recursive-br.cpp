#include <iostream>
#include <vector>
using namespace std; 

/**
 * Slow algorithm to reverse the bits of a value, but it works. Perhaps there is a faster way?
 * Description: Take a list that has a size of a power of two and split it into "odd" and "even"
 * parts until each part is of size two, then compile it back together into the bit-reversed list.
 * 
 * Arguments: vector<unsigned long>& vector_to_reverse --> the vector to have bit reversed.
 *            size --> the size of the vector to reverse.
*/

void RecursiveBitReverseVector(vector<unsigned long>& vector_to_reverse, unsigned long size) {
    vector<unsigned long> even;
    vector<unsigned long> odd;

    // Base case: a vector of size 2 is already bit-reversed.
    if (size == 2) {
        return;
    }

    // Populate the even and odd vectors with their respective values.   
    for (unsigned long i = 0; i < (vector_to_reverse.size()); i += 2) {
         even.push_back(vector_to_reverse.at(i));
    }
    
    for (unsigned long i = 1; i < (vector_to_reverse.size()); i += 2) {
        odd.push_back(vector_to_reverse.at(i));
    }

    // Perform the recursion on each subset of even / odd vectors.
    RecursiveReverseBits(even, even.size());
    RecursiveReverseBits(odd, odd.size()); 

    // Compile the even vector to the first half of the starting vector...
    for (unsigned long i = 0; i < size / 2; i++) {
        vector_to_reverse.at(i) = even.at(i);
    }

    // ...and the odd to the second half.
    for (unsigned long i = 0; i < size / 2; i++) { 
        vector_to_reverse.at(size/2 + i) = odd.at(i);
    }

    return;
    
}

/**
 * 
*/

unsigned long RecursiveReverseBits(unsigned long val, unsigned long size) {
    vector<unsigned long> reversal_vector;
    unsigned long new_val_index = 0;
    for (unsigned long i = 0; i < size; i++) {
        reversal_vector.push_back(i);
        if (i == val) {
            new_val_index = i;
        }
    }
    _RecursiveReverseBits(reversal_vector, size);
    cout << "compiled vector" << endl;
    for (unsigned long i = 0; i < size; i++) {
        cout << reversal_vector.at(i) << " ";
    }
    cout << endl;
    return reversal_vector.at(new_val_index);
}

int main() {
    unsigned long val;
    unsigned long size;
    cout << "Please enter a value to bit-reverse." << endl;
    cin >> val;
    cout << "Please enter a power of two over which to perform the reversal." << endl;
    cin >> size;
    
    cout << ReverseBits(val, size) << endl;
    return 0;
}   
