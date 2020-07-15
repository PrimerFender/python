height = int(input())

lines = ["", "#"]

if height < 1:
    print("\n".join(lines[:height + 1:]))
else:
    for index in range(1, height):
        new_line = "##" + lines[index]
        lines.append(new_line)
    width = len(lines[-1])
    centered_lines = []
    for line in lines:
        centered_lines.append(line.center(width))
    print("\n".join(centered_lines[1::]))