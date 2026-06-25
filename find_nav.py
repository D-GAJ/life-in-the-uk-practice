with open('js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("--- switchTab function ---")
for i in range(9109, 9120):
    print(lines[i].rstrip())

print("--- DOM init ---")
for i in range(8940, 8960):
    print(lines[i].rstrip())
