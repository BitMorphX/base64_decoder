<p align="center">
  <img src="assets/banner.png" alt="base64_decoder banner" width="100%" />
</p>

# 🔐 BASE64 DECODER

**base64_decoder** is a fast and reliable tool for decoding Base64-encoded private keys and generating Bitcoin address data.

It takes a Base64-encoded private key and outputs:
- Bitcoin address (compressed & uncompressed)
- WIF format (compressed & uncompressed)
- Public key (HEX)
- Private key (HEX)

---

## ⚙️ Features

- 🔐 Decodes Base64 private keys
- 📬 Outputs Bitcoin address (compressed & uncompressed)
- 🔑 Shows WIF formats
- 🔎 Public + private key in HEX
- 🖥️ Terminal color output

---

## 📁 File Overview

- `base64_decoder.py` – Main decoding and key derivation script  
- `base64_decoder.bat` – Windows launcher for quick use  
- `.vscode/`  
  - `settings.json` – Editor preferences  
  - `launch.json` – Debugging configuration  
  - `tasks.json` – Task runner integration  
  - `extensions.json` – Recommended VS Code extensions  
- `assets/`  
  - `banner.png` – Project banner  
  - `demo.gif` – Demo preview  
- `README.md` – This documentation  
- `LICENSE` – Apache 2.0 License  
- `NOTICE` – Attribution and notices  
- `ETHICS` – Responsible use notice  
- `requirements.txt` – Python dependencies

---

## 🛠️ Dependencies

```
ecdsa
pycryptodome
base58
termcolor
```

Install with:

```bash
pip install -r requirements.txt
```

> Python 3.8+ is recommended.

---

## 🚀 Usage

### Option 1 – via Python:
```bash
python base64_decoder.py
```

### Option 2 – via `.bat` launcher (Windows):
```cmd
base64_decoder.bat
```

---

## 📦 Example Output

```
Bitcoin Address (Uncompressed): 1...
Bitcoin Address (Compressed):   1...
WIF (Uncompressed): 5...
WIF (Compressed):   K...
Public Key (Uncompressed HEX): 04...
Public Key (Compressed HEX):   02...
Private Key (HEX): a3...
```

---

## 📂 Project Structure

```text
base64_decoder/
├── assets/
│   ├── banner.png
│   └── demo.gif
├── .vscode/
│   ├── settings.json
│   ├── launch.json
│   ├── tasks.json
│   └── extensions.json
├── base64_decoder.py
├── base64_decoder.bat
├── LICENSE
├── NOTICE
├── ETHICS
├── README.md
└── requirements.txt
```

---

## 🎬 DEMO

<p align="center">
  <img src="assets/demo.gif" alt="DEMO: BASE64 DECODER" width="90%" />
</p>

---

## ⚠️ DISCLAIMER

This software is provided strictly for **educational, analytical, and research purposes only**.

The author **does not promote or condone** any unethical behavior, unauthorized access, or abuse of blockchain systems or cryptographic tools.

This project **does not include or generate any real private keys** linked to actual cryptocurrency holdings.
It is designed to operate in **offline environments** or for simulation/testing purposes.

**The author accepts no liability** for any damages, losses, or illegal use resulting from this software.
All responsibility lies solely with the end user.

> **Use responsibly. Learn ethically. Contribute honestly.**

---

## ⚖️ Ethical Use

This tool is created strictly for **research and educational purposes**.  
See [ETHICS](./ETHICS.md) for the full statement.

---

## 📜 License

Licensed under the [Apache 2.0 License](./LICENSE)

---

## 📣 NOTICE

See [`NOTICE`](./NOTICE) for important information about attribution, DMCA protection, and reuse permissions.

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
