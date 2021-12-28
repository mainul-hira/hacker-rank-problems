def minion_game(string):
    vowel = ('A', 'E', 'I', 'O', 'U') # Kevin = Vowel
    # vowel = 'AEIOU'

    kevins_point, sturat_point = 0, 0
    # for idx, i in string time limit exceeded
    for i in range(len(string)):
        if string[i] in vowel:
            kevins_point += len(string)-i
            # kevins_point += len(string[idx:]) time limit exceeded
        else:
            sturat_point += len(string)-i
    if sturat_point>kevins_point:
        print(f"Stuart {sturat_point}")
    elif sturat_point==kevins_point:
        print(f"Draw")
    else:
        print(f"Kevin {kevins_point}")

if __name__ == '__main__':
    s = input()
    minion_game(s)