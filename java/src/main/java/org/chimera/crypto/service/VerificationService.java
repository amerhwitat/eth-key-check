package org.chimera.crypto.service;

import org.chimera.crypto.model.AuditEvent;
import java.util.ArrayList;
import java.util.List;

public final class VerificationService {
    public record Result(List<String> addresses, AuditEvent audit) {}
    public Result verify(List<String> addresses) {
        List<String> normalized = new ArrayList<>(addresses.size());
        for (String address : addresses) normalized.add(AddressService.normalizeEthereum(address));
        return new Result(List.copyOf(normalized), AuditEvent.now("verify-address-inventory", "java", "count=" + normalized.size()));
    }
}
