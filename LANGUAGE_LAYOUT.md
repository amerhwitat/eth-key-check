# Chimera Crypto language layout

The repository now exposes language-specific roots while preserving the legacy Python entry points for compatibility.

```text
eth-key-check/
  python/   Python reference implementation and research layer
  java/     Java 21 + JavaFX desktop application
  cpp/      C++20 + Qt 6 desktop application
  docs/     cross-language architecture and security documentation
```

The same logical modules are mapped across languages: public blockchain observation, deterministic verification, database access, CNN/RNN/GRU research, offline RL experiments, audit/provenance, and C8192/R8192 telemetry.

The Python reference remains compatible with existing users; new language implementations are additive until a release migration can be tested end-to-end.

Qt 6 uses CMake for the C++ GUI build, while the Java application uses Maven/JavaFX. The C++ GUI follows Qt's Widgets architecture and can later add Qt Quick visualizations.

Security scope remains unchanged: no address-to-private-key guessing, seed cracking, arbitrary private-key enumeration, or unauthorized wallet access.
