package org.chimera.crypto;

import org.chimera.crypto.service.AddressService;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AddressServiceTest {
    @Test void normalizesValidAddress() {
        assertEquals("0xabcdefabcdefabcdefabcdefabcdefabcdefabcd",
            AddressService.normalizeEthereum("0xABCDEFabcdefABCDEFabcdefABCDEFabcdefABCD"));
    }

    @Test void rejectsMalformedAddress() {
        assertFalse(AddressService.isValidEthereum("0x1234"));
    }
}
