import time
def decorate(func):
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print('runtime:', round(time.perf_counter() - start, 5), 'seconds')
        return result
    return _wrapper

@decorate
def strcounter(s): # сложность O(N**2)
    for sym in set(s):
        counter = 0
        for sub_sym in s:
            if sym == sub_sym:
                counter += 1
        print(sym, counter)

@decorate
def strcounter_new(s): # сложность O(N)
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym, count)
strcounter('aabbbbccccccddddd')

strcounter_new('aabbbbccccccddddd')