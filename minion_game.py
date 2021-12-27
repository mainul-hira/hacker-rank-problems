import re

# def create_combination(string):
#     res = (string[i: j] for i in range(len(string))
#             for j in range(i + 1, len(string) + 1))
#     return res
    
def minion_game(string):
    vowel = ('A', 'E', 'I', 'O', 'U') # Kevin = Vowel

    # all_words = create_combination(string)
    # used_words = set()
    kevins_point, sturat_point = 0, 0
    for idx, i in enumerate(string):
        if i in vowel:
            #used_words.add(i)
            # kevins_point += len(re.findall(f'(?={i})',string))
            kevins_point += len(string[idx:])-1
            # print(counter[i])
            print('kev', kevins_point)
        else:
            sturat_point += len(string[idx:])-1
            # print('stu', sturat_point)
    
    if sturat_point>kevins_point:
        print(f"Stuart {sturat_point}")
    elif sturat_point==kevins_point:
        print(f"Draw")
    else:
        print(f"Kevin {kevins_point}")

if __name__ == '__main__':
    s = input()
    minion_game(s)