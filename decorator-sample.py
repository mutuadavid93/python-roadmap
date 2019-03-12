import time

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper

@elapsed_time
def hugeSum():
    num_list = []
    for n in (range(0, 10000)):
        num_list.append(n)
    print(f'Huge sum {sum(num_list)}')

def main():
    hugeSum()

if __name__ == '__main__': main()
