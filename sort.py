#基本的なソート　https://qiita.com/maiyama18/items/257e8b9b49d891137d56 https://qiita.com/suecharo/items/30f5d817da4c948c3be6
# bubble sort
def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1, i, -1):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]

    return a


# insert sort
def insert_sort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j] >= a[j-1]:
                break
            else:
                a[j], a[j-1] = a[j-1], a[j]

    return a


# quick sort
def quick_sort(a):
    if len(a) in (0, 1):
        return a

    p = a[-1]
    l = [x for x in a[:-1] if x <= p]
    r = [x for x in a[:-1] if x >  p]

    return qSort(l) + [p] + qSort(r)


# merge sort
def merge(l, r):
    n = len(l + r) # マージ後の配列のサイズ
    s = max(l + r) + 1 # 番兵

    l.append(s)
    r.append(s)

    a = []
    while len(a) < n:
        a.append(l.pop(0)) if l[0] <= r[0] else a.append(r.pop(0))

    return a

def msort(a):
    if len(a) == 1:
        return a

    mid = len(a) // 2
    l = msort(a[:mid])
    r = msort(a[mid:])

    return merge(l, r)