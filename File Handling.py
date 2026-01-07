filename = 'Trial.txt'
with open(filename, 'r') as file:
    text = file.read()
    lines = text.split('\n')
    words = text.split()
    characters = len(text)
    print(f"Total lines: {len(lines)}")
    print(f"Total words: {len(words)}")
    print(f"Total characters: {characters}")
with open('Trial.txt', 'r') as src:
    with open('Dupe.txt', 'w') as dst:
        for line in src:
            dst.write(line)
print("File copied successfully!")