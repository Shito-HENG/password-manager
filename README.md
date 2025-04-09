# Simple Password Manager 🔒

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-green.svg)
![Fernet](https://img.shields.io/badge/Encryption-Fernet-yellow.svg)

A secure local password manager that encrypts credentials using AES-256.

## Features

- 🔐 **Military-grade encryption** (Fernet/AES-256)
- 💾 **Local SQLite storage** - No cloud dependencies
- ✨ **Simple CLI interface** - Easy to use
- 🔑 **Auto-generated encryption key** - Stored securely

## Installation

1. Ensure Python 3.6+ is installed
2. Install dependencies:

```bash
pip install cryptography
```

## Usage
```bash
python pass_manager.py
```

## File Structure
```bash
.
├── password_manager.py   # Main application
├── passwords.db          # Encrypted credential storage
└── secret.key            # Encryption key (DO NOT SHARE)
```
