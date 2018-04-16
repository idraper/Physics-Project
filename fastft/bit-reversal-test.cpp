#include <iostream>
#include <vector>
using namespace std;

// max_val is power of two
unsigned long ReverseBits(unsigned long val, unsigned long max_val) {
    int num_bits = -1;
    unsigned long new_val = 0;
    unsigned long mask_lsb = 1;
    unsigned long mask_msb = 1;
    unsigned long tmp1 = 0;
    unsigned long tmp2 = 0;

    while (max_val >= 1) {
        num_bits++;
        max_val >>= 1;
    }
    cout << num_bits << endl;
    mask_msb <<= num_bits - 1;
    cout << "Swapping {" << val << "}";
    cout << endl;
 
    for (int i = 1; i <= (num_bits); i++) {
        cout << mask_msb << " : " << mask_lsb << endl;
        new_val |= (val & mask_lsb) << (num_bits/i - 1);
        new_val |= (val & mask_msb) >> (num_bits/i - 1);
        mask_msb >>= 1;
        mask_lsb <<= 1;
    }

    cout << " with {" << new_val << "}" << endl;
    return new_val;
}

int main() {
    unsigned long size = 0;
    unsigned long tmp = 0;
    cout << "Please enter a number to bit-reverses." << endl;
    cin >> tmp;
    cout << "Please enter a power of two to test with the bit-reversal." << endl;
    cin >> size;
    ReverseBits(tmp, size);
    return 0;
}
    
