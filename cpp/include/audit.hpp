#pragma once
#include <string>
#include <utility>

namespace chimera::crypto {
struct AuditEvent { std::string event; std::string component; std::string detail; };
inline AuditEvent auditEvent(std::string event, std::string component, std::string detail) {
    return {std::move(event), std::move(component), std::move(detail)};
}
}
