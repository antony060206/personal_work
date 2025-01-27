# Name: Antony Feng
# ccid: zfeng8
# studentId: 1802829
# operating system: windows 11
# python version: 3.12

#count the coins utilizing methods of recursion
def min_coins(coins, S):

    memo = [[-1] * (S + 1) for _ in range(len(coins))]

    def sub_min_coins(i, S, coins, memo):
        if S == 0:
            return 0 # Base Case

        if S < 0 or i == len(coins):
            return float('inf') #condition case

        if memo[i][S] != -1:
            return memo[i][S]

        include = 1 + sub_min_coins(i, S - coins[i], coins, memo) # continue to run recursion using the same denomination buy subtract from total amount
        exclude = sub_min_coins(i + 1, S, coins, memo)# run recursion using the next denomination.

        memo[i][S] = min(exclude, include)# pick the minimum between exclusion side and inclusion side
        return memo[i][S]

    value = sub_min_coins(0, S, coins, memo)
    return value if (value) != float('inf') else -1

def main():
    coins = list(map(int, input().split()))
    S = int(input())
    print(min_coins(coins, S))

if __name__ == "__main__":
    main()