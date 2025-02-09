energy = float(input())
artifact_pieces = 0
terrains_mountain_count = 0

while True:

    command = input()

    if command == 'Journey ends here!':
        break

    if command == 'mountain':
        energy -= 10
        terrains_mountain_count += 1
        if terrains_mountain_count % 3 == 0:
            artifact_pieces += 1
    elif command == 'desert':
        energy -= 15
    elif command == 'forest':
        energy += 7

    if energy <= 0:
        print(f'The character is too exhausted to carry on with the journey.')
        break
    if artifact_pieces == 3:
        print(f"The character reached the legendary artifact with {energy:.2f} energy left.")
        break

if artifact_pieces < 3 and energy > 0:
    needed_artifacts = 3 - artifact_pieces
    print(f"The character could not find all the pieces and needs {needed_artifacts} more to complete the legendary artifact.")

