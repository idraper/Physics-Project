#include <sstream>
#include <iostream>
#include <string>
using namespace std;

// usage: testss <string>
int main(int argc, char* argv[]) {
    istringstream iStream;
    string tmp;
    string tmp1;

    // check for correct program usage
    if (argc != 2) {
        cout << endl << "Usage: " << endl;
        cout << "testss <string>" << endl;
    }

    else {
        tmp = argv[argc - 1];
        iStream.str(tmp);
        iStream >> tmp1;
        cout << endl << tmp1 << endl << endl;
    }
    
    return 0;
}
        
        
    
        
