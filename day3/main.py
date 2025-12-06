from utils.utils import read_input

input_data = read_input('input.txt').split('\n')
# input_data = read_input('test.txt').split('\n')


def get_biggest_voltage(x):
    x_val = -1
    x_idx = -1
    for i in range(len(x)-1):
        if x[i] > x_val:
            x_val = x[i]
            x_idx = i
    
    y_val = -1
    for item in x[x_idx+1:]:
        if item > y_val:
            y_val = item
            # y_idx = i
    return x_val * 10 + y_val
        
# print(get_biggest_voltage(x))


print(input_data)
batteries_voltage = []
for line in input_data:
    # print(line)
    # print(get_biggest_voltage([int(x) for x in line]))
    batteries_voltage.append(get_biggest_voltage([int(x) for x in line]))
print("Part 1:")
print(sum(batteries_voltage))