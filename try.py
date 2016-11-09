import heapq
def nthSuperUglyNumber(n, primes):
    uglies = [1]
    def gen(prime):
        for ugly in uglies:
        	print("yield: ", ugly, uglies, ugly*prime)
        	yield ugly * prime
    merged = heapq.merge(*map(gen, primes))
    while len(uglies) < n:
        ugly = next(merged)
        print(ugly)
        if ugly != uglies[-1]:
            uglies.append(ugly)
    return uglies[-1]



def nthSuperUglyNumber2(n, primes):
        indexs, uglies = [0] * len(primes), [1]
        while len(uglies) < n:
            uglies.append(min([p * uglies[indexs[i]] for i, p in enumerate(primes)]))
            for i, p in enumerate(primes):
                if p * uglies[indexs[i]] == uglies[-1]:
                    indexs[i] += 1
        return uglies[-1]

a = nthSuperUglyNumber2(10, [2,3,5])
print(a)


