from posix import PRIO_DARWIN_BG
import tqdm
from utils.utils import read_input

input_data = read_input('input.txt').split('\n')
# input_data = read_input('test.txt').split('\n')

sum1 = 0
sum2 = 0

def largest_joltage(bank: str, k: int):
    n = len(bank)
    pos = 0
    batteries = []
    for remaining in range(k, 0, -1):
        end = n - remaining + 1
        best_digit = max(bank[pos:end])
        # print(best_digit)
        pos = bank.index(best_digit, pos, end) + 1
        # print(pos)
        batteries.append(best_digit)
    return ''.join(batteries)


for bank in tqdm.tqdm(input_data):
    sum1 += int(largest_joltage(bank, 2))
    sum2 += int(largest_joltage(bank, 12))
    
print(sum1)
print(sum2)