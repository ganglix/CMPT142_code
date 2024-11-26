import time

def print_time(m):
    s = m * 60
    for i in range(s):
        print(f"time: {s // 60}: {s % 60}")
        s -= 1
        time.sleep(1)

print_time(30)
