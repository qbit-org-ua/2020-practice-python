import sys

position = 0
direction = 1j
for line in sys.stdin:
    action = line.strip()
    if action == "L":
        direction *= 1j
        print("New direction", direction)
    elif action == "R":
        direction *= -1j
        print("New direction", direction)
    else:
        position += direction
        print("New position", position)

print(int(position.real), int(position.imag))
