import re


with open("input.txt", "r") as f:
    # lines = [line.strip()[:-1] for line in f.readlines()]
    lines = f.readline().split(',')

# print(lines)

def duplicate_detector(num:str):
    # numbers = re.findall(r'(?:10|[1-9])', str(num))
    part1, part2 = num[:len(num)//2], num[len(num)//2:]
    return part1 == part2 
    

regex1 = re.compile(r"^(\d+?)\1$")
regex2 = re.compile(r"^(\d+?)\1+$")
dublicates = []  
regex_list = []
regexparttwo = []
for pair in lines:
    lower, upper = pair.split("-")
    # print(lower, upper)
    for i in range(int(lower), int(upper)+1):
        if duplicate_detector(str(i)):
            # print(i)
            dublicates.append(i) 
        # 
        if regex1.search(str(i)):
            regex_list.append(i)
        
        if regex2.search(str(i)):
            regexparttwo.append(i)
# print(duplicate_detector(str(1188511885)))
print("Solution asnwer:")
# print(sum(dublicates))
print(sum(regex_list))
print(sum(regexparttwo))



# part 2
# 
# kk
# 
# def part_two(number:str)-> bool:
#     for j in range(2, len(number)): # how many parts to do
#         x = len(number)
#         if x//j >= 1
#     return False
        