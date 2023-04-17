import sys

#To Run: python3 fibdp.py [insert n here]

def fib(n: int) -> int:
    saved = {}
    def fibDP(n: int, saved: dict):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            if n in  saved:
                return saved[n]
            else:
                saved[n] = fibDP(n - 1, saved) + fibDP(n-2, saved)
                return saved[n]

    return fibDP(n, saved)


if __name__ == "__main__":
    print(fib(int(sys.argv[1])))