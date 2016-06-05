def palindrome_chain_length(n):
    count = 0
    n_reversed = int(str(n)[::-1])
    while n_reversed != n:
        n += n_reversed
        n_reversed = int(str(n)[::-1])
        count += 1
        print n
    return count