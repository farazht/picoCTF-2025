In this challenge, we're given a script called `encrypt.py`, and a server which runs the script and gives us the output. The script is as follows:

```python
from sys import exit
from Crypto.Util.number import bytes_to_long, inverse
from setup import get_primes

e = 65537

def gen_key(k):
    """
    Generates RSA key with k bits
    """
    p,q = get_primes(k//2)
    N = p*q
    d = inverse(e, (p-1)*(q-1))

    return ((N,e), d)

def encrypt(pubkey, m):
    N,e = pubkey
    return pow(bytes_to_long(m.encode('utf-8')), e, N)

def main(flag):
    pubkey, _privkey = gen_key(1024)
    encrypted = encrypt(pubkey, flag) 
    return (pubkey[0], encrypted)

if __name__ == "__main__":
    flag = open('flag.txt', 'r').read()
    flag = flag.strip()
    N, cypher  = main(flag)
    print("N:", N)
    print("e:", e)
    print("cyphertext:", cypher)
    exit()
```

Upon connecting through netcat with `nc verbal-sleep.picoctf.net 52407`, we are given the output of the `encrypt.py` script. `N` is the product of two large primes, `e` is the public exponent, and `cyphertext` is the encrypted flag. There are differences in the output every time, but here's one example:

```
N: 17331888949958626322076349723693353586949992813330889311998177135851498252616136915169808708361454133739981105592238995956273616707947484352482472226002222
e: 65537
cyphertext: 14081377010238412082456693428860331885996760832113646341505686078787763394857283042098225924264012674754370194336100511650315050593559436515896344596305385
```

Taking a look at `N`, we can see that it's actually divisible by 2, meaning the prime factors of `N` are `2` and `N/2`. This is a huge vulnerability in the RSA encryption scheme, as we can easily factorize `N` and find the private key `d`. We can then decrypt the flag using the private key.

```python
def long_to_bytes(n):
    return n.to_bytes((n.bit_length() + 7) // 8, 'big')

def decrypt(N, e, cyphertext):
    p = 2
    q = N // 2
    d = pow(e, -1, (p-1)*(q-1))
    return long_to_bytes(pow(cyphertext, d, N))

print(decrypt(N, e, cyphertext))
```

Running the code above, we get the flag `picoCTF{tw0_1$_pr!m3605cd50e}` (two is prime!).