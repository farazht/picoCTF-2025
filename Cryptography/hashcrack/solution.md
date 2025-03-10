## hashcrack

This puzzle was mostly about identifying the type of hash, then feeding it to a hash cracker. None of the passwords were particularly unique, so they were easy to crack. I used [hashcat](https://hashcat.net/hashcat/) to crack the hashes.

The first hash was 32 characters, which made MD5 the most likely candidate. The second was 40 characters, which made SHA-1 the most likely candidate. The third was 64 characters, which made SHA-256 the most likely candidate. 

All three happened to be the first hashing algorithm I tried to crack them with. 

Here's the complete terminal output, along with my responses:
```
> nc verbal-sleep.picoctf.net 52014
Welcome!! Looking For the Secret?

We have identified a hash: 482c811da5d5b4bc6d497ffa98491e38
Enter the password for identified hash: 

> password123
Correct! You've cracked the MD5 hash with no secret found!

Flag is yet to be revealed!! Crack this hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Enter the password for the identified hash: 

> letmein
Correct! You've cracked the SHA-1 hash with no secret found!

Almost there!! Crack this hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
Enter the password for the identified hash: 

> qwerty098
Correct! You've cracked the SHA-256 hash with a secret found.
The flag is: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_7f29c9da}
```