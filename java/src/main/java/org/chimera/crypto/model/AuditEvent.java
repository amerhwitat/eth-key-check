package org.chimera.crypto.model;

import java.time.Instant;
import java.util.UUID;

public record AuditEvent(UUID id, String event, String component, String detail, Instant timestamp) {
    public static AuditEvent now(String event, String component, String detail) {
        return new AuditEvent(UUID.randomUUID(), event, component, detail, Instant.now());
    }
}
