# Chimera Crypto language layout

The repository exposes language-specific roots while preserving legacy Python entry points for compatibility.

```text
eth-key-check/
  python/
    chimera_crypto/      unified Python facade and shared contracts
  node/                  Node.js ESM integration package
  java/                  Java 21 + JavaFX desktop application
  cpp/                   C++20 + Qt 6 desktop application
  docs/                  cross-language architecture and security documentation
```

The same logical modules are mapped across languages: public blockchain observation, deterministic verification, database access, CNN/RNN/GRU research, offline RL experiments, audit/provenance, and C8192/R8192 telemetry.

Python remains the reference research layer; Node.js is the web/integration layer; Java is the desktop/JVM layer; C++ is the native/Qt layer. Shared JSON/JSONL envelopes and deterministic public/synthetic vectors define interoperability.

Qt 6 uses CMake for the C++ GUI build, while Java uses Maven/JavaFX and Node uses npm/ESM. Existing entry points remain supported until an end-to-end migration is verified.

Security scope remains unchanged: no address-to-private-key guessing, seed cracking, arbitrary private-key enumeration, credential harvesting or unauthorized wallet access.