import sys

position = 0
direction = 1j
for line in sys.stdin:
    action = line.strip()
    if action == "L":
        direction *= 1j
    elif action == "R":
        direction *= -1j
    else:
        position += direction

print(int(position.real), int(position.imag))
