#include <iostream>
#include <vector>
using namespace std;

// max_val is power of two
unsigned long ReverseBits(unsigned long val, unsigned long max_val) {
    int num_bits = 0;
    unsigned long new_val = 0;
    unsigned long mask_lsb = 1;
    unsigned long mask_msb = 1;
    unsigned long tmp1 = 0;
    unsigned long tmp2 = 0;

    while (max_val >= 1) {
        num_bits++;
        max_val >>= 1;
    }
    mask_msb <<= num_bits - 1;

    for (int i = 1; i <= (num_bits) / 2; i++) {
        new_val |= (val & mask_lsb) << (num_bits/i - 1);
        new_val |= (val & mask_msb) >> (num_bits/i - 1);
        mask_msb >>= 1;
        mask_lsb <<= 1;
    }

    return new_val;
}

int main() {
    unsigned long size = 0;
    unsigned long tmp = 0;
    unsigned long swap_index = 0;
    vector<unsigned long> linear_vector;
    vector<unsigned long> reversed_vector;
    cout << "Please enter a number (power of two) of the size of vector to sort in bit-reversed order." << endl;
    cin >> size;

    for (unsigned long i = 0; i < size; i++) {
        linear_vector.push_back(i);
    }

    cout << "Original vector: " << endl;

    for (unsigned int i = 0; i < size; i++) {
        cout << "[" << i << "] -> " << linear_vector.at(i) << endl;
    }

    for (unsigned long i = 0; i < (size + 1) / 2; i++) {
        cout << "Swapping {" << linear_vector.at(i) << "} with {"; //FIXME: not needed in regular function
        swap_index = ReverseBits(i, size >> 1);
        tmp = linear_vector.at(i);
        linear_vector.at(i) = linear_vector.at(swap_index);
        linear_vector.at(swap_index) = tmp;
        cout << linear_vector.at(i) << "}" << endl; //FIXME: not needed in regular function
    }

    cout << "Bit reversed vector: " << endl;

    for (unsigned int i = 0; i < size; i++) {
        cout << "[" << i << "] -> " << linear_vector.at(i) << endl;
    }

    return 0;
}
    
