## Bitlocker-1

Pretty straight forwards challenge. Decrypt an encrypted drive image by getting the insecure bitlocker key.

Following a [guide](https://openwall.info/wiki/john/OpenCL-BitLocker#Recovery-Password-authentication-method), we first extract the hashes from the image after installing [**john**](https://github.com/openwall/john)

```bash
./bitlocker2john -i ../../bitlocker-1.dd > hash
```

Then, we can use hashcat to guess the password using the rockyou passowrd list.
```bash
./hashcat.exe -m 22100 bitlocker_hash.txt rockyou.txt
```

It took about 2 seconds of hashing using my 3050 GPU for hashcat to find the password.
```bash
$ cat hashcat.potfile
$bitlocker$0$16$cb4809fe9628471a411f8380e0f668db$1048576$12$d04d9c58eed6da010a000000$60$68156e51e53f0a01c076a32ba2b2999afffce8530fbe5d84b4c19ac71f6c79375b87d40c2d871ed2b7b5559d71ba31b6779c6f41412fd6869442d66d:jacqueline
```

I'm lazy and didn't feel like messing around with a CLI tool to mount/unlock the drive in linux so I simply installed this [Passmark OSFMount](https://www.osforensics.com/tools/mount-disk-images.html). In step 4, `Physical Disk Emulation` needs to be selected for Windows to recognize it as a bitlocker encrypted drive. Once that was done, windows helpfully prompted me for the password which decrypted the drive. Inside we find the `flag.txt`!
