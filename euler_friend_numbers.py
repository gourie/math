import time

def main():

    N = 1e18

    def sum(N):
        start = time.time()
        result = 0
        for i in range(N):
            if i % 1000:
                print("** step %i **" %i)
            result += i
        end = time.time()
        print("Sum till %N: %s, took %s seconds" %(N,result, end-start))
        return result, end-start

    sum(N)

if __name__ == "__main__":
    main()