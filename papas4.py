import random
import time
from sys import breakpointhook

# ランダムに文字列を並び替えた後
# バブルソートで正しい順に並べ替え

nuwa = "パパスぬわ"

# nuwa:str = "パパスぬわ"から nuwa_dict:dict = {0:"パ", 1:"ス", 2:"ぬ",3:"わ"}を作成
nuwa_list = list(nuwa)
nuwa_val = list(dict.fromkeys(list(nuwa)))
nuwa_key = range(len(nuwa_val))
nuwa_dict = {key: val for key, val in zip(nuwa_key, nuwa_val)}


def value_to_key(val: list):
    '''
    ["パ","パ","ス","ぬ","わ"]を[0, 0, 1, 2, 3]に変換
    '''
    # ValueからKeyを取得する
    # print( [k for k, v in nuwa_dict.items() if v == "ぬ"][0])
    ans = []
    for i, d in enumerate(val):
        ans.append([k for k, v in nuwa_dict.items() if v == val[i]][0])
    return ans


def key_to_value(key: list):
    '''
    [0, 0, 1, 2, 3]を["パ","パ","ス","ぬ","わ"]に変換
    '''
    ans = [nuwa_dict[i] for i in key]
    return ans


# def bubbleSort(a:list):
#     for i in range(len(a)):
#        for j in range(len(a)-1, i, -1):
#             if a[j] < a[j-1]:
#                 a[j], a[j-1] = a[j-1], a[j]
#
#    return a

# print(value_to_key(["パ","ぬ","ス","わ","パ"]))
# print(key_to_value([0, 0, 1, 2, 3]))

try:
    change = True
    ans: list = random.sample(nuwa_list, len(nuwa_list))
    print("{}{}{}「{}{}ーー!!".format(*ans))
    ans_num = value_to_key(ans)
    count = 0

    # バブルソート
    for i in range(len(ans_num)):
        for j in range(len(ans_num)-1, i, -1):
            if ans_num[j] < ans_num[j-1]:
                ans_num[j], ans_num[j-1] = ans_num[j-1], ans_num[j]
                # print(*ans_num)
                ans = key_to_value(ans_num)
                print("{}{}{}「{}{}ーー!!".format(*ans))
                count += 1
                time.sleep(0.2)

    print(f"{count}回の入れ替えで成功しました。")
except KeyboardInterrupt:
    print('!!FINISH!!')
