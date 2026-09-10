# Cross-Language Crypto Research Consolidation Implementation Plan

**Goal:** Consolidate Python utilities and provide aligned Java, C++/Qt, and Node.js implementations with shared JSON/JSONL contracts.

**Architecture:** Python is the reference research implementation; Java and C++ provide desktop/native applications; Node.js provides CLI/integration services. Shared schemas and deterministic vectors define behavior across languages.

**Tech Stack:** Python 3, Java 21+/JavaFX, C++20/Qt 6/CMake, Node.js ESM/npm, JSON/JSONL, SQLite-compatible persistence.

**Global constraints:** preserve restore-and-verify only; no address-to-private-key recovery or seed guessing; keep existing Python entry points backward compatible; use deterministic public/synthetic vectors; keep wallet signing external.

## Tasks
1. Consolidate Python behind a package facade and shared contracts.
2. Add Node.js ESM package, CLI, validation, audit and conformance tests.
3. Split JavaFX into model/service/view packages with tests.
4. Split C++/Qt into core/UI/test targets with CMake.
5. Synchronize Node/Java/C++ language documentation across related repositories.
6. Verify changed files, commits and available CI checks.
