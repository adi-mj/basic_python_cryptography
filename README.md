# Baby Crypter
This simple Python script provides basic encryption and decryption functionalities using a custom algorithm. It works by encoding text using a specific encryption core and decoding it using a corresponding decryption method.

## Usage

### Encryption
To encrypt a message, use the following command:

```bash
python3 baby_crypter -e <message>
Replace <message> with the text you want to encrypt. This will output the encrypted text in hexadecimal format.
```

### Decryption
To decrypt an encrypted message, use the following command:

```bash
python3 baby_crypter -d <encrypted_message>
Replace <encrypted_message> with the hexadecimal representation of the encrypted text. This will output the decrypted text.
```

### How It Works
The script utilizes a custom encryption algorithm, which involves the following steps:

Encryption: It encodes each character of the input message using a specific formula ((123 * char + 18) % 256).
Decryption: It reverses the encryption process by performing calculations that involve modular arithmetic and the inverse of the encryption formula.

# XOR Crypter
This Python script provides simple encryption and decryption functionalities using the XOR operation with a dynamic key. It utilizes the XOR operation to encrypt and decrypt text based on a key generated randomly or provided in hexadecimal format.

## Usage
### Encryption
To encrypt a message, use the following command:

```bash
python3 xor_crypter -e <message>
Replace <message> with the text you want to encrypt. This will output the encrypted text in hexadecimal format along with the randomly generated key.
```

### Decryption
To decrypt an encrypted message, use the following command:

```bash
python3 xor_crypter -d <encrypted_message>
Replace <encrypted_message> with the hexadecimal representation of the encrypted text and the key used during encryption. This will output the decrypted text.
```

### How It Works
The script utilizes the XOR operation with a key to encrypt and decrypt messages. Here's a brief overview:

Encryption: It performs an XOR operation between each byte of the input data and the key.
Decryption: It uses the same XOR operation with the key to reverse the encryption process and retrieve the original message.