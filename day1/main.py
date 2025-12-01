with open("input.txt", "r") as f:
    file_content = f.readlines()
    clear_line = []
    for line in file_content:
        if len(line.strip()):
            clear_line.append(
                (int(line[1:].strip()), True if line[0] == "R" else False)
            )


def rotate_index(current_index, steps, list_length, clockwise=True):
    if clockwise:
        new_index = (current_index + steps) % list_length
    else:
        new_index = (current_index - steps) % list_length
    return new_index


def part1(possition):
    curr_indx = possition
    part1answer = 0
    for steps, clock in clear_line:
        curr_indx = rotate_index(curr_indx, steps, len(init_list), clock)
        if init_list[curr_indx] == 0:
            part1answer += 1
    return part1answer


def part2(position):
    curr_indx = position
    part2answer = 0
    for steps, clock in clear_line:
        for _ in range(steps):
            curr_indx = rotate_index(curr_indx, 1, len(init_list), clock)
            if curr_indx == 1:
                part2answer += 1
        if curr_indx == 0:
            part2answer -= 1

    return part2answer


init_list = [i for i in range(0, 100)]
curr_indx = 50
old_indx = None

part1answer = part1(curr_indx)
part2answer = part2(curr_indx)
print("Part 1: ", part1answer)
print("Part 2: ", part2answer)
print("Final Results: ", part1answer + part2answer)
