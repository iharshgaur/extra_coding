def print_formatted(number):
    # your code goes here
    w = len("{0:b}".format(n))
    for i in range(1,n+1):
        print (("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width=w)).upper())

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)