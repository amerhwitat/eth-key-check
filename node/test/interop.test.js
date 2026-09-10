import { test } from 'node:test';
import assert from 'node:assert/strict';
import { normalizeEthAddress, validateEthAddress, encodeEnvelope, decodeEnvelope } from '../src/index.js';

test('normalizes a valid Ethereum address', () => {
  assert.equal(normalizeEthAddress('0xABCDEFabcdefABCDEFabcdefABCDEFabcdefABCD'), '0xabcdefabcdefabcdefabcdefabcdefabcdefabcd');
});

test('rejects malformed Ethereum addresses', () => {
  assert.equal(validateEthAddress('0x1234'), false);
});

test('round-trips interoperability envelopes', () => {
  const value = decodeEnvelope(encodeEnvelope('verify', { count: 2 }));
  assert.deepEqual(value.payload, { count: 2 });
});
