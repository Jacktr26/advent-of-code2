with open('input.txt', 'r') as file:
    lines = file.readlines()

safe = 0
for line in lines:

    levels = list(map(int, line.strip().split()))

    is_increasing = True
    is_decreasing = True

    # Check differences and order
    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])

        if not (1 <= diff <= 3):
            pass
            break

        if levels[i] < levels[i + 1]:
            is_decreasing = False
        elif levels[i] > levels[i + 1]:
            is_increasing = False


    else:
        if is_increasing or is_decreasing:
            safe += 1
        else:
            pass

print(safe)
