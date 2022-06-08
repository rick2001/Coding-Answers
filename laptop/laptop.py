from collections import Counter

T = int(input())

for _ in range(T):
    n = int(input())
    friends_recom = list(map(int, input().split()))
    if n == 1:
        print(friends_recom[0])
    else:
        counts_dict = Counter(friends_recom)
        print(counts_dict)
        counts_dict = dict(sorted(counts_dict.items(), key=lambda item: item[1]))
        count_list = list(counts_dict.values())

        print(count_list[-1], count_list[-2])
        if count_list[-1] == count_list[-2]:
            print('CONFUSED')
        else:
            v = list(counts_dict.keys())
            print(v[-1])
            print(f'{list(counts_dict.keys())[-1]}')
