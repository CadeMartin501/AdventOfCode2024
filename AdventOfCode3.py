import re

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]


def find_multiply_pairs(find_line):
    # Takes a line of instructions, locates all mul(x,y), multiplies each x and y
    # then returns the sum
    p_sum = 0
    p_list = re.findall("mul\((\d+,\d+)\)", find_line)
    for pair in p_list:
        int_pair = [int(a) for a in pair.split(",")]
        p_sum += int_pair[0] * int_pair[1]
    return p_sum

mul_result = 0
all_line = ""
for line in lines:
    all_line+=line
    mul_result = find_multiply_pairs(all_line)
 # print(mul_result)

mul_result=0
blocks=all_line.split("don't()")

mul_result = find_multiply_pairs(blocks[0])
for n in range(1,len(blocks)):
    i = blocks[n].find("do()")

doMultiply = blocks[n][i:]
mul_result += find_multiply_pairs(doMultiply)
print(mul_result)
