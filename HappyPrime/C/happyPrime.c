#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>


bool primeCheck(int prime)
{
    if (prime == 1 || prime % 2 == 0)
    {
        return false;
    }
    double root = sqrt((double)prime) + 1;
    for (int i = 3; i < root; i++)
    {
        if (prime % i == 0)
        {
            return false;
        }
    }
    return true;
}

int breakDown(int prime)
{
    if (prime < 7)
    {
        return prime;
    }
    int sum = 0;
    while (prime > 0) {
        sum += (int)pow(prime % 10,2);
        prime /= 10;
    }
    return breakDown(sum);
}

int main()
{
    int cases;
    scanf("%d", &cases);
    for (int i = 0; i < cases; i++)
    {
        int k, prime;
        scanf("%d %d", &k, &prime);
        if (prime > 6 && primeCheck(prime) && breakDown(prime) == 1)
        {
            printf("%d %d YES\n", k, prime);;
        }
        else
        {
            printf("%d %d NO\n", k, prime);;

        }
    }
}