#!/usr/bin/env python3

try:
    from hangul_utils import split_syllable_char
except:
    print("No Module Error: please install 'hangul_utils' module with 'pip'")
    exit(1)

strok_jamo = [
        { # [0]: line_num_method (선분수)
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
        { # [1]: strok_method (획수)
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
def count_strokes(korean_ch: str, strok_method: bool) -> int:
    """count strokes or lines for a character"""
    strokes = 0
    _strok_method = 1 if strok_method else 0

    chs = split_syllable_char(korean_ch)
    for ch in chs:
        strokes += strok_jamo[_strok_method][ch]

#    print("{}: {}".format(korean_ch, chs))

    return strokes % 10


# static
def name_to_strokes(name: str, strok_method: bool) -> list[int]:
    """get strokes from a name"""
    strokes = []
    for w in name:
        strokes.append(count_strokes(w, strok_method))
    return strokes


# static
def merge_lists(list1: list[str], list2: list[str]) -> list[str]:
    """merge 2 names: 이철수, 김영희 -> 이김철영수희"""
    if len(list1) > len(list2):
        short_len = len(list2)
        long_list = list1
    else:
        short_len = len(list1)
        long_list = list2
    
    tot_list = []
    for (n1, n2) in zip(list1, list2):
        tot_list.append(n1)
        tot_list.append(n2)

    for n in long_list[short_len:]:
        tot_list.append(n)
    return tot_list


#static
def print_strokes(strok_list: list, tot_cnt: int):
    """
    for progress
    1 2 3 4 5 6
     1 2 3 4 5
      1 2 3 4
       1 2 3
        1 2
    """
    cnt = len(strok_list) 
    spaces = " " * (tot_cnt - cnt)

    print(spaces, end='')
    for n in strok_list[:-1]:
        print(f"{n}", end=' ')
    print(strok_list[-1])


def calculate_love(name1: str, name2: str, strok_method) -> int:
    """calculate 이름 궁합"""
    # print title
    print("이름 궁합 [{}]: {}, {}".format("획수" if strok_method else "선분수", name1, name2))

    # 이철수, 김영희 -> 이김철영수희
    name = ''.join(merge_lists(list(name1), list(name2)))

    # 이김철영수희 -> [num1, num2, num3, num4, num5, num6]
    strokes = name_to_strokes(name, strok_method)
    
    # len(num1~num6)
    first_len = len(strokes)

    # current strokes, next strokes
    # (res[current], res[next], next = 1 - current)
    # next strokes: calculated once from current strokes
    res = [strokes, []]
    current = 0
    next = 1 - current

    print('\n' + name)
    
    # calculate until 2 strokes left
    while len(res[current]) > 2:
        # print a progress (print current strokes)
        print_strokes(res[current], first_len)

        # calculate next strokes
        for (n1, n2) in zip(res[current], res[current][1:]):
            res[next].append((n1 + n2) % 10)

        next = current
        current = 1 - next

        res[next].clear()

    # print a progress (print current strokes)
    print_strokes(res[current], first_len)

    return res[current][0] * 10 + res[current][1]


#static
def is_korean(name: str) -> bool:
    for character in name:
        if ord('가') <= ord(character) <= ord('힣'):
            return True
    return False


#main
def main():
    me = input("본인 이름: ")

    if not is_korean(me):
        print("Please input korean name~")
        exit(1)

    lo = input("애인 이름: ")

    if not is_korean(lo):
        print("Please input korean name~")
        exit(1)

    strok_method = int(input("계산 방법은? (0:선분수, 1:획수) "))

    print()

    love = calculate_love(me, lo, True if strok_method == 1 else False)

    print("\n이름 궁합: {}%\n".format(love))


#call main
main()
