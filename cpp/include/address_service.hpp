#pragma once
#include <string>
#include <stdexcept>
#include <algorithm>
#include <cctype>

namespace chimera::crypto {
inline std::string normalizeEthereum(std::string value) {
    if (value.rfind("0x", 0) == 0) value.erase(0, 2);
    if (value.size() != 40 || !std::all_of(value.begin(), value.end(), [](unsigned char c){ return std::isxdigit(c) != 0; }))
        throw std::invalid_argument("invalid Ethereum address");
    std::transform(value.begin(), value.end(), value.begin(), [](unsigned char c){ return static_cast<char>(std::tolower(c)); });
    return "0x" + value;
}
inline bool validEthereum(const std::string& value) noexcept {
    try { normalizeEthereum(value); return true; } catch (...) { return false; }
}
}
