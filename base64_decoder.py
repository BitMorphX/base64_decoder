#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import argparse
import hashlib
from ecdsa import SigningKey, SECP256k1
from Crypto.Hash import RIPEMD160
import base58
from termcolor import colored
import os
import platform


def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")


def print_colored(text, color="green"):
    try:
        print(colored(text, color))
    except Exception:
        print(text)


def sha256(data):
    return hashlib.sha256(data).digest()


def ripemd160_sha256(data):
    sha = sha256(data)
    ripemd = RIPEMD160.new()
    ripemd.update(sha)
    return ripemd.digest()


def wif_encode(private_key_bytes, compressed=False):
    prefix = b"\x80"
    extended_key = prefix + private_key_bytes
    if compressed:
        extended_key += b"\x01"
    checksum = sha256(sha256(extended_key))[:4]
    return base58.b58encode(extended_key + checksum).decode()


def generate_bitcoin_address(public_key_bytes):
    pubkey_hash = ripemd160_sha256(public_key_bytes)
    versioned_payload = b"\x00" + pubkey_hash
    checksum = sha256(sha256(versioned_payload))[:4]
    full_payload = versioned_payload + checksum
    return base58.b58encode(full_payload).decode()


def main():
    clear_screen()

    parser = argparse.ArgumentParser(description="Decode Base64 private key and generate Bitcoin key info.")
    parser.add_argument(
        "-b", "--base64",
        type=str,
        help="Base64-encoded private key"
    )
    args = parser.parse_args()

    if args.base64:
        encoded_text = args.base64
    else:
        print_colored("Enter Base64-encoded private key:", "cyan")
        encoded_text = input("> ")

    try:
        # Decode Base64 to private key bytes
        private_key_bytes = base64.b64decode(encoded_text)
        private_key_hex = private_key_bytes.hex()

        # WIF formats
        wif_uncompressed = wif_encode(private_key_bytes, compressed=False)
        wif_compressed = wif_encode(private_key_bytes, compressed=True)

        # Generate key pair
        sk = SigningKey.from_string(private_key_bytes, curve=SECP256k1)
        vk = sk.get_verifying_key()
        pubkey_uncompressed = b'\x04' + vk.to_string()
        pubkey_compressed = (
            (b'\x02' if vk.to_string()[32] < 128 else b'\x03') + vk.to_string()[:32]
        )

        # Generate addresses
        address_uncompressed = generate_bitcoin_address(pubkey_uncompressed)
        address_compressed = generate_bitcoin_address(pubkey_compressed)

        # Final output sequence
        print_colored(f"Bitcoin Address (Uncompressed): {address_uncompressed}", "green")
        print_colored(f"Bitcoin Address (Compressed):   {address_compressed}", "green")
        print_colored(f"WIF (Uncompressed): {wif_uncompressed}", "cyan")
        print_colored(f"WIF (Compressed):   {wif_compressed}", "cyan")
        print_colored(f"Public Key (Uncompressed HEX): {pubkey_uncompressed.hex()}", "white")
        print_colored(f"Public Key (Compressed HEX):   {pubkey_compressed.hex()}", "white")
        print_colored(f"Private Key (HEX): {private_key_hex}", "yellow")

    except Exception as e:
        print_colored(f"Error: {e}", "red")


if __name__ == "__main__":
    main()
