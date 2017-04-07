"""Input: coins- a list of available coin vaues
          value- an amount of change to be made
 This function will take in a list of possible coins and a value amount and
 return the smallest number of coins needed to equal that value. """


def find_change(coins, value):
    coins.sort(reverse=True)
    x = 0
    rem=0
    for coin in coins:
        if value/coin > 1:
            #print(value, coin, value/coin, value%coin,x)
            x += int(value/coin)
            value = value%coin
    return x


def main():
    coins = [1, 5, 10, 25]
    #print(find_change(coins, 100))
    print(find_change(coins, 73))



if __name__ == '__main__':
    main()
