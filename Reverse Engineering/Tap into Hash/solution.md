## Tap into Hash

In this challenge, we're given a Python script (`block_chain.py`) that implements a custom blockchain with encryption. The goal is to decrypt the encrypted blockchain to find the flag.

```python
# Snippet of block_chain.py

def main(token):
    key = bytes.fromhex(random_string)

    print("Key:", key)

    genesis_block = Block(0, "0", int(time.time()), "EncodedGenesisBlock", 0)
    blockchain = [genesis_block]

    for i in range(1, 5):
        encoded_transactions = base64.b64encode(
            f"Transaction_{i}".encode()).decode('utf-8')
        new_block = proof_of_work(blockchain[-1], encoded_transactions)
        blockchain.append(new_block)

    all_blocks = get_all_blocks(blockchain)

    blockchain_string = blockchain_to_string(all_blocks)
    encrypted_blockchain = encrypt(blockchain_string, token, key)

    print("Encrypted Blockchain:", encrypted_blockchain)
```

The provided Python script generated a blockchain, encrypted it using a custom algorithm, and concealed the flag within the encryption process.

The main vulnerability is that the encryption function was inserting our flag (token) in the middle of the blockchain string before encrypting the entire data. The encryption method used XOR operations with a SHA-256 hash of a key.

Since both the encryption key and the encrypted blockchain were output in the original code, we had all the necessary components to write a script to decrypt the flag:
1. Compute the SHA-256 hash of the key
2. XOR each 16-byte block of ciphertext using the key hash
3. Remove padding from the plaintext
4. Decode the resulting bytes to a string

```python
# Snippet of solution.py

def decrypt(ciphertext, key):
    key_hash = hashlib.sha256(key).digest()
    block_size = 16
    plaintext = b''
    
    for i in range(0, len(ciphertext), block_size):
        cipher_block = ciphertext[i:i + block_size]
        plain_block = xor_bytes(cipher_block, key_hash)
        plaintext += plain_block
    
    padding_length = plaintext[-1]
    plaintext = plaintext[:-padding_length]
    
    plaintext_str = plaintext.decode('utf-8')
    
    return plaintext_str

print(decrypt(encrypted_blockchain, key))
```

```
040c8f6470b8dab78ea991fe655eb4bbd20c1c7a02e1942e725f24211eaa7e51-0040c6a8a46e897b5e0bc39936718417d34a4da3f135045552af215a530c166a-00df72d375c3674ca5d20f6e929c6ba8picoCTF{block_3SRhViRbT1qcX_XUjM0r49cH_qCzmJZzBK_c83eaee3}58d00578d78643fc1b558fc518dc1b88-007a7b08c465df5089f917c4c676c0b97fcc98b02b2852ce2986797fe51ab2c0-0085647cc554c0b13268025d8e655cba64c873fa6680936af6f2637b8ecd0ef2
```

The decrypted text contains the flag: `picoCTF{block_3SRhViRbT1qcX_XUjM0r49cH_qCzmJZzBK_c83eaee3}`.
