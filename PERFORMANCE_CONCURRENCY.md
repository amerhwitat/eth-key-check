# Performance & Concurrency Policy

General parsing, RPC, and reporting code may use bounded concurrency for independent I/O workloads. Cryptographic key-search, private-key enumeration, credential recovery, or brute-force paths are not to be parallelized for increased guessing throughput.

Preserve validation correctness, deterministic tests, bounded resources, and secure library usage. Benchmark any benign concurrency change before adopting it.
