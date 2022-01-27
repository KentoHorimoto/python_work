import random
import sort
import time
import datetime

random_list = random.sample(range(1000),k=1000)

#print(*random_list)


def calc_time_sort(a:list):
    print("ソート時間を計測 \nソート方法を選択: bubble insert quick merge")
    inp = input('>>')
    #print(input)

    start = time.time()
    if inp == "bubble":
        ans = sort.bubble_sort(a)
    elif inp == "insert":
        ans = sort.insert_sort(a)
    elif inp == "quick":
        ans = sort.insert_sort(a)
    elif inp == "merge":
        ans = sort.msort(a)
    else:
        print("ソート方法を選択してください。")
        return 

    end = time.time()
    elapsed_time = end - start

    print(f"{inp} sort :{elapsed_time*1000}ミリ秒かかりました。")
    #print(ans)


calc_time_sort(random_list)
