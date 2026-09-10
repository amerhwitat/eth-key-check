import { verifyAddressInventory } from './index.js';

const args = process.argv.slice(2);
if (args.length === 0) {
  console.error('usage: npm run verify -- <ethereum-address> [address...]');
  process.exitCode = 2;
} else {
  try {
    console.log(JSON.stringify(verifyAddressInventory(args), null, 2));
  } catch (error) {
    console.error(error.message);
    process.exitCode = 1;
  }
}
