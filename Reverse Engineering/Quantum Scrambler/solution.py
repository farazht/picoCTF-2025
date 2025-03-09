from input import input

def scramble(L):
  A = L # flag
  i = 2
  while (i < len(A)):
    A[i-2] += A.pop(i-1)
    A[i-1].append(A[:i-2])
    i += 1
  return L

scrambled = scramble([[str(i)] for i in range(32)])

# ok so it seems possible to use our initial input as a key for the scrambled solution we received. We can do a breadth first search to get all of the keys.

from collections import deque

# Initialize the queue with the top-level list and its path
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

for key, location in locations.items():
    char = input
    for subkey in location:
        char = char[subkey]
    print(chr(int(char, 16)), end="")
