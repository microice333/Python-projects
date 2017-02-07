#program to find minimum number of nominals to return change
import math

def change(n, nominals):
    nominals.append(0)
    nominals.sort()
    number_of_nominal_value = len(nominals)
    dp = [[0 for i in range(0, n + 1)] for j in range(0, number_of_nominal_value)]

    for i in range(1, n + 1):
        dp[0][i] = math.inf - 1

    for i in range(1, number_of_nominal_value):
        j = 0
        while j < nominals[i]:
            dp[i][j] = dp[i - 1][j]
            j +=1

        while j <= n:
            dp[i][j] = min(dp[i][j - nominals[i]] + 1, dp[i - 1][j])
            j+=1

    return dp[number_of_nominal_value - 1][n]

def main():
    how_many_nominals = int(input("Type number of nominals: "))
    nominals = []
    for _ in range(0, how_many_nominals):
        i = int(input())
        nominals.append(i)
    cost = int(input("Enter the cost: "))
    money_given = int(input("Enter amonut of money: "))
    if cost > money_given:
        print("Sorry you dont have enough money")
    else:
        print(change(money_given - cost, nominals))

if __name__ == '__main__':
    main()

