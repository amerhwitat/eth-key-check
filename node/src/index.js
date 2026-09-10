import { normalizeEthAddress, validateEthAddress } from './validation.js';
import { auditEvent } from './audit.js';
import { encodeEnvelope, decodeEnvelope } from './contracts.js';

export { normalizeEthAddress, validateEthAddress, auditEvent, encodeEnvelope, decodeEnvelope };

export function verifyAddressInventory(addresses) {
  const normalized = addresses.map(normalizeEthAddress);
  return { valid: normalized.length === addresses.length, addresses: normalized, audit: auditEvent('verify-address-inventory', 'node', `count=${normalized.length}`) };
}
