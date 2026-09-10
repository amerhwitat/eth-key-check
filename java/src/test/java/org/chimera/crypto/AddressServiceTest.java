package org.chimera.crypto;

import org.chimera.crypto.service.AddressService;

public final class AddressServiceTest {
    public static void main(String[] args) {
        if (!"0xabcdefabcdefabcdefabcdefabcdefabcdefabcd".equals(AddressService.normalizeEthereum("0xABCDEFabcdefABCDEFabcdefABCDEFabcdefABCD"))) throw new AssertionError();
        if (AddressService.isValidEthereum("0x1234")) throw new AssertionError();
        System.out.println("AddressService checks passed");
    }
}
