def is_safe(levels):
    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if diff < 1 or diff > 3:
            return False
        if levels[i] == levels[i + 1]:
            return False
    return levels == sorted(levels) or levels == sorted(levels, reverse=True)


with open('input.txt', 'r') as file:
    lines = file.readlines()

safe_count = 0

for line in lines:
    levels = list(map(int, line.strip().split()))

    # check if report is safe
    if is_safe(levels):
        safe_count += 1
        continue

    # check if report can be made safe by removing a level
    dampener_safe = False
    for i in range(len(levels)):
        temp_levels = levels[:i] + levels[i + 1:]
        if is_safe(temp_levels):
            dampener_safe = True
            break

    if dampener_safe:
        safe_count += 1

print(safe_count)
