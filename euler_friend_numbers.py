from math import log
import time

def main():
    """ main loop """
    #TODO: enable parallezation to use multiple cores

    N = int(1e18)

    def sum(N):
        start = time.time()
        result = 0
        for i in range(N):
            if i % int(1e9) == 0:
                print("** step %i **" % int(i/1e9))
            result += i
        end = time.time()
        print("Sum till %N yields %s, took %s seconds" %(N,result, end-start))
        return result, end-start

    def count_friend_numbers(N, base=10):
        """
        Project Euler problem 612 - https://projecteuler.net/problem=612
        Let's call two numbers friend numbers if their representation in base 10 has at least one common digit.
        E.g. 1123 and 3981 are friend numbers.
        Let f(N) be the number of pairs (p,q) with 1≤p<q<N such that p and q are friend numbers.
        This function will calculate f(N)

        :param N: ceiling number to calculate the number of friend numbers
        :return: number of friend number (p,q) s.t. 1≤p<q<N
        """

        start = time.time()
        result = 0
        for i in range(1,base):
            # 1. till N=100=1e2
            # single digit: friends XX
            result += 2*base-2
            # double digits: friends XX
            result += int( ((base-1)+(base-i))*i/2 )
            result += int(( 1 + base-i-2)*(base-i-2)/2 )
            result += (i+1)*2*(base-i-1)
            result += (base-i-1)*(base-2 + 2*(base-i-1))

            # 2. till N=1000=1e3
            # single digits: extra friends XXX
            result += base^2 + (base-2)*(2*base-1)
            # double digits: extra friends XXX
            result += (base-2)*( 2*base^2 + (base-2)*(2*base-1) + (base-3)*(2*base-1) )
            result += 2*( base^2 + (base-2)*base + 2*(base-2)*(base-1) )
            # triple digits: friends XXX

            # 3. till N=10000=1e4
            # single digits: extra friends XXXX
            # result += base^3 + (base-2)*( base^2 + (base-1)*(2*base-1) )

        end = time.time()
        print("Counting friend numbers till %s yields %s, took %0.5f seconds" %(N,result, end-start))
        return result, end-start

    # sum(N)
    count_friend_numbers(100)


if __name__ == "__main__":
    main()