package org.chimera.crypto.model;

public record InteropEnvelope(String schema, int version, String operation, String payloadJson) {
    public static final String SCHEMA = "chimera.crypto.interop";
    public InteropEnvelope {
        if (!SCHEMA.equals(schema) || version != 1) throw new IllegalArgumentException("unsupported interoperability envelope");
    }
    public String toJson() {
        return "{\"schema\":\"" + schema + "\",\"version\":" + version + ",\"operation\":\"" + operation + "\",\"payload\":" + payloadJson + "}";
    }
}
