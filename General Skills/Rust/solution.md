## Rust General Skills

### fixme1

Comments basically tell you what to do. First error is a missing semicolon at the end of the line hinted at by `// How do we end statements in Rust?`

```rust
let key = String::from("CSUCKS");
```

Second error is hinted at by `// How do we print out a variable in the println function?`.  Solved using the [documentation](https://doc.rust-lang.org/rust-by-example/hello/print.html).

```rust
println!(
    "{}", // How do we print out a variable in the println function?
    String::from_utf8_lossy(&decrypted_buffer)
);
```
    
```bash
cargo run
```
    
Super nice developer experience, just ran one command to install rust and the documentation is really clear.

### fixme 2

The next challenge deals with variable mutability. The first change was to change the function argument `borrowed_string` to be mutable which can be done by marking it as a &mut as [documented](https://doc.rust-lang.org/rust-by-example/fn/closures/input_parameters.html).
```rust
borrowed_string: &mut String
```

My editor automatically installed an LSP for rust so I followed its reccomendation to change party\_foul to be mutable:
```rust
let mut party_foul
```
and followed its reccomendation to mutability of party\_foul in the function call to:
```rust
decrypt(encrypted_buffer, &mut party_foul);
```

### fixme 3

It just tells you to read the [documentation](https://doc.rust-lang.org/book/ch20-01-unsafe-rust.html) and the challenge can be solved by un-commenting the `unsafe {}` wrapper.
