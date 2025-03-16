## Flag Hunters

### Background

Reading through the program source provided there are several important pieces of syntax used in the song data:

#### REFRAIN

This command causes an immediate jump to the song location labeled [REFRAIN].

#### RETURN `line: integer`

This command causes an immediate jump to line `i`.

#### CROWD `_: any`

This command requests user input `data`, then replaces itself with `Crowd: <data>`.

#### END

This command immediately halts the song.

#### ;

If present on any line, the semicolon will split the song line at its location, effectively treating one line as several.

### Solution

Because the `CROWD` command causes user input to be directly inserted into the song data, it can be exploited to add arbitrary commands to the execution flow. Prefixing a `;` to the user input results in the resulting line `Crowd: ;<data>`, which gives us the ability to use whatever commands we like. In this case, we want to somehow get the program to print the beginning of the song.

`RETURN` allows us to describe a line we would like to jump to, so we can input `;RETURN 0` when prompted, and the next time the program encounters that position it will jump to line 0 and continue execution, leaving us with the flag: `picoCTF{70637h3r_f0r3v3r_250bd6ef}`