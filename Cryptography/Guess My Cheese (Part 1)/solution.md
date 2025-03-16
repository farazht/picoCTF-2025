## Guess My Cheese (Part 1)

Spoiler: This challenge caused me a lot of pain. 

The challenge begins with connecting to a server (`nc verbal-sleep.picoctf.net 64700`), where you're tasked with decoding the secret cheese in order to prove your identity as the real Squeexy.

Note: the challenge uses a random cheese and a random encryption every time you connect to the server, so for the rest of this writeup, I will be showing how to do one specific example.

```
*******************************************
***             Part 1                  ***
***    The Mystery of the CLONED RAT    ***
*******************************************

The super evil Dr. Lacktoes Inn Tolerant told me he kidnapped my best friend, Squeexy, and replaced him with an evil clone! You look JUST LIKE SQUEEXY, but I'm not sure if you're him or THE CLONE. I've devised a plan to find out if YOU'RE the REAL SQUEEXY! If you're Squeexy, I'll give you the key to the cloning room so you can maul the imposter...

Here's my secret cheese -- if you're Squeexy, you'll be able to guess it:  NLYSGWPJPAJOOIORMM
Hint: The cheeses are top secret and limited edition, so they might look different from cheeses you're used to!
Commands: (g)uess my cheese or (e)ncrypt a cheese
What would you like to do?
```

Since the cheese is encrypted, we can't begin with guessing it. We need to encrypt our own cheese first, so we can figure out the encryption method used.

My first attempt was `CHEDDAR` (obviously), which was encrypted to `AJOHHMB`:

```
What cheese would you like to encrypt? CHEDDAR
Here's your encrypted cheese:  AJOHHMB
Not sure why you want it though...*squeak* - oh well!

I don't wanna talk to you too much if you're some suspicious character and not my BFF Squeexy!
You have 2 more chances to prove yourself to me!

Commands: (g)uess my cheese or (e)ncrypt a cheese
What would you like to do?
```

I noticed that the `DD` was replaced with `HH`, making it likely to be some kind of substitution cypher.

After a lot of trial and error, I finally figured out that the cheeses were encrypted using an **Affine Cypher**, where `a` and `b` are randomly chosen every time you connect to the server.

After many failed attempts, I came up with a method I would use every time I connected to the server. 

First, I would encrypt `MASCARPONE`, as it had a lot of unique letters. I didn't need to use a second guess after this, as it was almost always enough to figure out the `a` and `b` values.

Next, I would ask the script to guess the cheese:

```
   _   _
  (q\_/p)
   /. .\.-.....-.     ___,
  =\_t_/=     /  `\  (
    )\ ))__ __\   |___)
   (/-(/`  `nn---'

SQUEAK SQUEAK SQUEAK

         _   _
        (q\_/p)
         /. .\
  ,__   =\_t_/=
     )   /   \
    (   ((   ))
     \  /\) (/\
      `-\  Y  /
         nn^nn


Is that you, Squeexy? Are you ready to GUESS...MY...CHEEEEEEESE?
Remember, this is my encrypted cheese:  NLYSGWPJPAJOOIORMM
So...what's my cheese?
```

I made the following script where I would put in the encrypted version of `MASCARPONE` and the encrypted cheese, and it would output the decrypted cheese:

Here's the script I used:

```python
mappings = []
mascarpone = "MASCARPONE"
mascarpone_enc = input("Enter the encoded version of MASCARPONE: ") # in this specific case, it was SMIAMBNGZO
pwd = input("Enter the password: ") # in this specific case, it was NLYSGWPJPAJOOIORMM

# find affine cipher values for A and B such that MASCARPONE encodes to the given encoded string
for i in range(26):
    for j in range(26):
        decoded = ""
        for c in mascarpone:
            decoded += chr(((ord(c) - 65) * i + j) % 26 + 65)
        if decoded == mascarpone_enc:
            mappings.append((i, j))

# try each mapping to decode the password
for i, j in mappings:
    decoded = ""
    for c in pwd:
        decoded += chr(((ord(c) - 65 - j) * pow(i, -1, 26)) % 26 + 65)
    print(decoded)
```

Using the script, I was able to find the decrypted output, which was `PLYMOUTHTCHEESEXAA`

Little did I know, I had already solved the challenge. However, this is where the pain began. 

I tried submitting `PLYMOUTHTCHEESEXAA` as the answer, but it was incorrect. I tried about 10 more times with different cheeses, analyzing the pattern:
- When the decrypted string was `SOURIRETLOZERIENBNF`, it contained `SOURIRE LOZERIEN`.
- When the decrypted string was `BRAUDOSTURLBNTZ`, it contained `BRAUDOSTUR`.
- When the decrypted string was `RACLETTEPGQZ`, it contained `RACLETTE`.
- When the decrypted string was `PAVETDETCHIRACDPIZ`, it contained `PAVE DE CHIRAC`.
- When the decrypted string was `GRANAXXDZ`, it contained `GRANA`.

The pattern was clear: any spaces in the cheese were replaced with `T`s, and there were always 3 random letters at the end of the cheese.

I spent another 30+ attempts trying the following things, over and over:
- Submitting the full decoded message (e.g. `PLYMOUTHTCHEESEXAA`)
- Submitting just the name of the cheese (e.g. `Plymouth Cheese`)
- Submitting just the name of the cheese, in lowercase (e.g. `plymouth cheese`)
- Submitting just the name of the cheese, in uppercase (e.g. `PLYMOUTH CHEESE`)
- Submitting the message, turning the `T`s back into spaces (e.g. `PLYMOUTH CHEESEXAA`)
- Submitting the message, removing the last 3 letters (e.g. `PLYMOUTHTCHEESE`)
- Submitting the name of the cheese, without spaces (e.g. `PLYMOUTHCHEESE`)

I then spent a long time thinking about what the last 3 letters could mean - surely, as the only thing I had no explanation for, they must be important. 

I assumed the most likely explanation was that the `n-3` first letters were a distraction, and the actual cheese was hidden somewhere in the last 3 letters of the decrypted message.

However, after a lot of trial and error, I decided to ask Allan for help.

He followed my method, and on his first attempt, it worked.

It turns out that copy-pasting the decrypted message `PLYMOUTHTCHEESEXAA` into the terminal was causing an issue on my end - I have no idea why, as this output was also copied straight from the terminal output of my script. I then tried typing out `PLYMOUTHTCHEESEXAA` manually, and it worked.

It turns out that none of the other things I had looked into mattered at all. 

```
         _   _
        (q\_/p)
         /. .\         __
  ,__   =\_t_/=      .'o O'-.
     )   /   \      / O o_.-`|
    (   ((   ))    /O_.-'  O |
     \  /\) (/\    | o   o  o|
      `-\  Y  /    |o   o O.-`
         nn^nn     | O _.-'
                   '--`

munch...

         _   _
        (q\_/p)
         /. .\         __
  ,__   =\_t_/=      .'o O'-.
     )   /   \      / O o_.-`|
    (   ((   ))      ).-'  O |
     \  /\) (/\      )   o  o|
      `-\  Y  /    |o   o O.-`
         nn^nn     | O _.-'
                   '--`

munch...

         _   _
        (q\_/p)
         /. .\         __
  ,__   =\_t_/=      .'o O'-.
     )   /   \      / O o_.-`|
    (   ((   ))        )'  O |
     \  /\) (/\          )  o|
      `-\  Y  /         ) O.-`
         nn^nn        ) _.-'
                   '--`

MUNCH.............

YUM! MMMMmmmmMMMMmmmMMM!!! Yes...yesssss! That's my cheese!
Here's the password to the cloning room:  picoCTF{ChEeSy6320b114}
```