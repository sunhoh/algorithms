# def get_all_letters(str):
#     print(list(str.strip()))

# output = get_all_letters('Radagast')
# print(output)


# my_list = [10, 9, 8, 7, 6]

# def list_loop(list):
#     result = 0
#     for i in range(len(list)): 
#         result = result + list[i]
#     return result

# output = list_loop(my_list)
# print(output)

# my_list = [10, 9, 8, 7, 6]

# def list_loop(lst):
#     return sum(lst)

# output = list_loop(my_list)
# print(output)


# abc1abc1abc
def solution(code):
    print("".join('abc1abc1abc'.split('1'))[::2])

    return "".join(code.split("1"))[::2] or "EMPTY"

print(solution('abc1abc1abc'))