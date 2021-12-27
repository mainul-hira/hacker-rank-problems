import re

def create_combination(string):
    res = (string[i: j] for i in range(len(string))
            for j in range(i + 1, len(string) + 1))
    return res
    
def minion_game(string):
    vowel = ('A', 'E', 'I', 'O', 'U') # Kevin = Vowel

    all_words = create_combination(string)
    used_words = set()
    kevins_point, sturat_point = 0, 0

    for i in all_words:
        if not i in used_words and i[0] in vowel:
            used_words.add(i)            
            kevins_point += len(re.findall(f'(?={i})', string))
            print('kev', kevins_point)
        elif not i in used_words and i[0] not in vowel:
            used_words.add(i)
            sturat_point += len(re.findall(f'(?={i})', string))
            print('stu', sturat_point)
    
    if sturat_point>kevins_point:
        print(f"Stuart {sturat_point}")
    elif sturat_point==kevins_point:
        print(f"Draw")
    else:
        print(f"Kevin {kevins_point}")

if __name__ == '__main__':
    s = input()
    minion_game(s)