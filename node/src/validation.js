export function normalizeEthAddress(value) {
  if (typeof value !== 'string') throw new TypeError('address must be a string');
  let v = value.trim();
  if (v.startsWith('0x')) v = v.slice(2);
  if (!/^[0-9a-fA-F]{40}$/.test(v)) throw new TypeError('invalid Ethereum address');
  return `0x${v.toLowerCase()}`;
}

export function validateEthAddress(value) {
  try { normalizeEthAddress(value); return true; } catch { return false; }
}
