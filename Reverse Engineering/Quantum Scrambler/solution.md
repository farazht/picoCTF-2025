## Quantum Scrambler

Initially I thougth the algorithm might be reversable, seems pretty straight forward until I realized that we were doing destructive list operations.
In Python, if you do, `A = L`, A refers to L and vice-versa.

Bringing the input into python, we can see that it's pretty long (17) but not insanely long. Might be reversable but it appears deterministic for a given input. Doing a quick check of how long the input *might* be using
```python
print(len(input)) # 17

length = 1
scrambled = 5
while scrambled != 17:
  length += 1
  L = [[str(i)] for i in range(length)]
  scrambled = len(scramble(L))
  print(length, scrambled) # 32, 17
```

32... a nice number. Seems brute forceable :D

We can generate our own input that's a list of numbers from 0 - 31 so we can eventually tell where the original inputs went
```python
scrambled = scramble([[str(i)] for i in range(32)])
```

Next, we do some shenaniganery (asking claude) to traverse this nested list structure while noting where we are. As usual, claude one shot..
I just had to modify it to save the locations in a dictionary that we can use on the scrambled input.
```python
locations = {}
queue = deque([(scrambled, [])])
result = []

while True:
  if len(queue) == 0:
    break
  current_list, current_path = queue.popleft()

  for i, item in enumerate(current_list):
    item_path = current_path + [i]
    if isinstance(item, list):
      queue.append((item, item_path))
    else:
      locations[item] = item_path
```

Finally, we can use the unscrambler to get our flag
```python
for key, location in locations.items():
  char = input
  for subkey in location:
    char = char[subkey]
  print(chr(int(char, 16)), end="") # some nice python trickery
```
