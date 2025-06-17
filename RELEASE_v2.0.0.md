# 📎 RELEASE NOTES – base64_decoder.py  
**Version:** 2.0.0  
**Release Date:** 2025-06-17

---

## 🚀 Overview

**base64_decoder** is a compact CLI tool that decodes Base64-encoded Bitcoin private keys and derives all related key material and addresses.

It enables fast offline transformation of raw Base64 input into WIF formats, Bitcoin addresses, and public/private key HEX representations — suitable for cryptographic testing, tool development, and educational use.

---

## 🔧 Core Features

- 🔓 Decodes Base64-encoded private keys  
- 🔑 Outputs WIF formats (compressed & uncompressed)  
- 🏷️ Generates Bitcoin addresses (compressed & uncompressed)  
- 🔍 Displays public and private keys in HEX  
- 🎨 Colored CLI output with `termcolor`  
- 🖥️ Optional command-line argument or interactive prompt  
- 🔒 Fully offline usage — no internet dependency

---

## ✅ Included in v2.0.0

- ✅ `base64_decoder.py` – CLI decoding and key conversion tool  
- ✅ `base64_decoder.bat` – Windows launcher for one-click execution  
- ✅ WIF encoding and Bitcoin address derivation  
- ✅ Interactive fallback if `--base64` argument is missing  
- ✅ SHA-256 and RIPEMD160 hash logic  
- ✅ Robust Base64 decoding with error handling  
- ✅ Clean terminal display using `clear()` and `termcolor`

---

## ⚠️ Notes

- Accepts only valid Base64-encoded 32-byte private keys  
- Uncompressed and compressed formats are both generated  
- WIF outputs use Bitcoin mainnet prefix  
- Use in air-gapped or isolated environments is recommended  
- No actual blockchain interaction or validation is performed

---

## 📌 Related Files

- [README.md](./README.md) – Main documentation  
- [base64_decoder.py](./base64_decoder.py) – CLI decoder script  
- [base64_decoder.bat](./base64_decoder.bat) – Windows launcher  
- [ETHICS](./ETHICS) – Responsible usage statement  
- [RELEASE_v2.0.0.md](./RELEASE_v2.0.0.md) – This file  
- [LICENSE](./LICENSE) – Apache 2.0 license  
- [NOTICE](./NOTICE) – Attributions and legal mentions

---

## 📜 License  
Licensed under the [Apache 2.0 License](./LICENSE) by **BitMorphX**

---

## 🍱 Support

★ **Bitcoin (BTC)**  
`1MorphXyhHpgmYSfvwUpWojphfLTjrNXc7`

★ **Monero (XMR)**  
`86VAmEogaZF5WDwR3SKtEC6HSEUh6JPA1gVGcny68XmSJ1pYBbGLmdzEB1ZzGModLBXkG3WbRv12mSKv4KnD8i9w7VTg2uu`

★ **Dash (DASH)**  
`XtNuNfgaEXFKhtfxAKuDkdysxUqaZm7TDX`

**We also value early privacy coins such as:**  
★ **Bytecoin (BCN)**  
`bcnZNMyrDrweQgoKH6zpWaE2kW1VZRsX3aDEqnxBVEQfjNnPK6vvNMNRPA4S7YxfhsStzyJeP16woK6G7cRBydZm2TvLFB2eeR`

🙏 *Thank you for supporting independent research and ethical technology.*

---

## 👤 Author & Contact

🔗 GitHub: https://github.com/BitMorphX  
✉️ Email: BitMorphX@proton.me  
💬 Telegram: https://t.me/BitMorphX

> _“I morph bits, not to break, but to understand.”_  
> — **BitMorphX**

---

© BitMorphX – All rights reserved.
