#include "address_service.hpp"
#include <iostream>
int main() {
    if (chimera::crypto::normalizeEthereum("0xABCDEFabcdefABCDEFabcdefABCDEFabcdefABCD") != "0xabcdefabcdefabcdefabcdefabcdefabcdefabcd") return 1;
    if (chimera::crypto::validEthereum("0x1234")) return 2;
    std::cout << "C++ crypto core checks passed\n";
    return 0;
}
