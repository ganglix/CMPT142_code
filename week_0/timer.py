import time


def print_time (m):
    s = m * 60
    for i in range(s):
        time.sleep(1)
        s -= 1
        print(f"time: {s // 60}: {s % 60}")


print_time(10)
