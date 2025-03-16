## Ph4nt0m 1ntrud3r

The file provided describes several network packets. Many of the payloads contained `=` or `==` at the trailing end, so I inferred that they were all base64 encoded.

Decoding all of these payloads resulted in one of the packets reading picoCTF so I assumed I was on the right track.

Reordering all the packets by relative time, in increasing time order, and joining all the decoded payloads together in that order, the flag appeared, prepended by nonsense data: `picoCTF{1t_w4snt_th4t_34sy_tbh_4r_d4b57909}`