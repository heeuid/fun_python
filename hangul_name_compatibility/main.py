#!/usr/bin/env python3

try:
    from hangul_utils import split_syllable_char
except:
    print("No Module Error: please install 'hangul_utils' module with 'pip'")
    exit(1)

strok_jamo = [
        { # [0]: non-traiditonal (선분수)
            'ㄱ': 2, 'ㄴ': 2, 'ㄷ': 3, 'ㄹ': 5,
            'ㅁ': 4, 'ㅂ': 4, 'ㅅ': 2, 'ㅇ': 1,
            'ㅈ': 3, 'ㅊ': 4, 'ㅋ': 3, 'ㅌ': 4,
            'ㅍ': 4, 'ㅎ': 3, 'ㄲ': 4, 'ㄸ': 6,
            'ㅃ': 8, 'ㅆ': 4, 'ㅉ': 6,
            'ㅏ': 2, 'ㅑ': 3, 'ㅓ': 2, 'ㅕ': 3,
            'ㅗ': 2, 'ㅛ': 3, 'ㅜ': 2, 'ㅠ': 3,
            'ㅡ': 1, 'ㅣ': 1, 'ㅐ': 3, 'ㅔ': 3,
            'ㅒ': 4, 'ㅖ': 4, 'ㅘ': 4, 'ㅝ': 4,
            'ㅢ': 2, 'ㅚ': 3, 'ㅟ': 3, 'ㅙ': 5,
            'ㅞ': 5
        },
        { # [1]: traditional (획수)
            'ㄱ': 1, 'ㄴ': 1, 'ㅇ': 1, 'ㄷ': 2,
            'ㅅ': 2, 'ㅈ': 2, 'ㅋ': 2, 'ㄲ': 2,
            'ㄹ': 3, 'ㅁ': 3, 'ㅊ': 3, 'ㅌ': 3,
            'ㅎ': 3, 'ㅂ': 4, 'ㅍ': 4, 'ㄸ': 4,
            'ㅆ': 4, 'ㅉ': 4, 'ㅃ': 8,
            'ㅡ': 1, 'ㅣ': 1, 'ㅏ': 2, 'ㅓ': 2,
            'ㅗ': 2, 'ㅜ': 2, 'ㅢ': 2, 'ㅐ': 3,
            'ㅔ': 3, 'ㅚ': 3, 'ㅟ': 3, 'ㅑ': 3,
            'ㅕ': 3, 'ㅠ': 3, 'ㅟ': 3, 'ㅘ': 4,
            'ㅝ': 4, 'ㅒ': 4, 'ㅖ': 4, 'ㅙ': 5,
            'ㅞ': 5,
        }
]

# static
def count_strokes(korean_ch, tradition):
    strokes = 0
    tradition = 1 if tradition else 0

    chs = split_syllable_char(korean_ch)
    for ch in chs:
        strokes += strok_jamo[tradition][ch]

#    print("{}: {}".format(korean_ch, chs))

    return strokes % 10


# static
def name_to_strok_list(name: str, tradition):
    strok = []
    for w in name:
        strok.append(count_strokes(w, tradition))
    return strok


# static
def merge_strok_lists(strok1: list, strok2: list):
    if len(strok1) > len(strok2):
        short_len = len(strok2)
        long_strok = strok1
    else:
        short_len = len(strok1)
        long_strok = strok2
    
    tot_strok = []
    for (n1, n2) in zip(strok1, strok2):
        tot_strok.append(n1)
        tot_strok.append(n2)

    for n in long_strok[short_len:]:
        tot_strok.append(n)
    return tot_strok


#static
def print_strok(strok: list, tot_cnt: int):
    cnt = len(strok) 
    spaces = " " * (tot_cnt - cnt)
    print(spaces, end='')
    for n in strok[:-1]:
        print(f"{n}", end=' ')
    print(strok[-1])


def calculate_love(name1: str, name2: str, tradition=True):
    print("이름 궁합 [{}]: {}, {}".format("획수" if tradition else "선분수", name1, name2))

    strok1 = name_to_strok_list(name1, tradition)
    strok2 = name_to_strok_list(name2, tradition)
    strokes = merge_strok_lists(strok1, strok2)

    first_len = len(strokes)

    res = [strokes, []]
    current = 0
    next = 1 - current

    while len(res[current]) > 2:
        print_strok(res[current], first_len)
        for (n1, n2) in zip(res[current], res[current][1:]):
            res[next].append((n1 + n2) % 10)

        next = current
        current = 1 - next

        res[next].clear()

    print_strok(res[current], first_len)
    ans = res[current][0] * 10 + res[current][1]

    return ans


me = input("본인 이름: ")
lo = input("애인 이름: ")

love = calculate_love(me, lo, tradition=False)
print(love)
#love = calculate_love(lo, me, tradition=False)
#print(love)
#love = calculate_love(me, lo, tradition=True)
#print(love)
#love = calculate_love(lo, me, tradition=True)
#print(love)
