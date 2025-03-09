import sys

def exit():
  sys.exit(0)

def scramble(L):
  A = L
  i = 2
  while (i < len(A)):
    A[i-2] += A.pop(i-1)
    A[i-1].append(A[:i-2])
    i += 1

  return L

def get_flag():
  flag = open('flag.txt', 'r').read()
  flag = flag.strip() # remove whitespace from ends
  hex_flag = []
  for c in flag:
    hex_flag.append([str(hex(ord(c)))]) # hex codes of all the ascii character

  return hex_flag

def main():
  flag = get_flag() # ok so it's a list of ascii codes in hex for all characters
  cypher = scramble(flag)
  print(cypher)

if __name__ == '__main__':
  main()
