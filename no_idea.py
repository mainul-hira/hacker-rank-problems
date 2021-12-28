
def calculate_happiness(array_data, set_a, set_b):
    happiness = 0
    for i in array_data:
        if i in set_a:
            happiness += 1
        elif i in set_b:
            happiness -= 1
    return happiness

if __name__ == '__main__':
    x, y = input().split()
    # for _ in range(int(x)):
    #     input().split()

    array_ = [int(x) for x in input().split()]
    set_a = set([int(y) for y in input().split()])
    set_b = set([int(y) for y in input().split()])
    # set_a = set(map(int, input().split()))
    # set_b = set(map(int, input().split()))
    print(calculate_happiness(array_, set_a, set_b))
