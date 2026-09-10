package org.chimera.crypto.service;

public final class AddressService {
    private AddressService() {}
    public static String normalizeEthereum(String value) {
        if (value == null) throw new IllegalArgumentException("address must not be null");
        String v = value.trim();
        if (v.startsWith("0x")) v = v.substring(2);
        if (!v.matches("[0-9a-fA-F]{40}")) throw new IllegalArgumentException("invalid Ethereum address");
        return "0x" + v.toLowerCase(java.util.Locale.ROOT);
    }
    public static boolean isValidEthereum(String value) {
        try { normalizeEthereum(value); return true; } catch (IllegalArgumentException ex) { return false; }
    }
}
