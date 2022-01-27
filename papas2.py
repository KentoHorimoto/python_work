import random
import time
nuwa = "パパスぬわ"
nuwa_seed = list(nuwa)
i = 0
try:
    while True:
        rand = random.sample(nuwa_seed, len(nuwa_seed))
        ans = ''.join(rand)
        print(ans)
        time.sleep(0.2)
        i += 1
        if ans == nuwa:
            break
except KeyboardInterrupt:
    print('!!FINISH!!')

print(f"{i}回目で成功しました。")
