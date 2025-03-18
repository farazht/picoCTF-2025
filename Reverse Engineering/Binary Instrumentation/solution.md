## Binary Instrumentation 1 and 2

A few hours before the end of the competition, I really wanted to finish just one more challenge. Of the unsolved challenges we had left, this seemed the most likely, though Allan was not available to turn on his Windows VM for me.

As a last ditch effort, I went through a few of the Reverse Engineering and Binary Exploitation challenges on my own Kali Linux VM and ran a standard set of commands on the binaries/executables to see if I could get any leads.

After some trial and error, I found that `binwalk` was able to detect and extract some files from both `bininst1.exe` and `bininst2.exe`. 

Maybe I was lucky that I didn't have quick access to Windows, as this somehow led me to the solution faster than the `frida-trace` approach.

```bash
$ ls

bininst1.exe
bininst1.zip

$ binwalk -e bininst1.exe

$ ls 

bininst1.exe
_bininst1.exe.extracted
bininst1.zip

$ cd _bininst1.exe.extracted

$ ls

6000 
6000.7z

$ strings 6000

...
<base64 encoded flag>
...
```

The exact same process worked for `bininst2.exe`.