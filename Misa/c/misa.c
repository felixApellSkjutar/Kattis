#include <stdio.h>
#include <stdlib.h>

int printSeats(int** seats, int r, int s)
{
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < s; j++)
        {
            printf("%d", seats[i][j]);
        }
        printf("\n");
    }
}

int cntShakes(int** seats, int r, int s, int i, int j)
{
    int temp = 0;
    if (j < s-1 && seats[i][j+1])
    {
        temp++;
    }
    if (i < r-1 && j < s-1 && seats[i+1][j+1])
    {
        temp++;
    }
    if (i < r-1 && seats[i+1][j])
    {
        temp++;
    }
    if (i < r-1 && j > 0 && seats[i+1][j-1])
    {
        temp++;
    }

    return temp;
}

int cntMirko(int** seats, int r, int s, int i, int j) 
{
        int temp = 0;
    if (j < s-1 && seats[i][j+1])
    {
        temp++;
    }
    if (i < r-1 && j < s-1 && seats[i+1][j+1])
    {
        temp++;
    }
    if (i < r-1 && seats[i+1][j])
    {
        temp++;
    }
    if (i < r-1 && j > 0 && seats[i+1][j-1])
    {
        temp++;
    }
        if (j > 0 && seats[i][j-1])
    {
        temp++;
    }
        if (i > 0 && j > 0 && seats[i-1][j-1])
    {
        temp++;
    }
        if (i > 0 && seats[i-1][j])
    {
        temp++;
    }
        if (i > 0 && j < s-1 && seats[i-1][j+1])
    {
        temp++;
    }

    return temp;
}

int main() 
{
    int r, s;
    int **seats;
    scanf("%d %d", &r, &s);
    
    seats = calloc(r, sizeof(int*));

    for (int i = 0; i < r; i++)
    {
        seats[i] = calloc(s, sizeof(int));
        for (int j = 0; j < s; j++)
        {
            char seat;
            scanf(" %c", &seat);
            if (seat == '.')
            {
                seats[i][j] = 0;
            }
            else
            {
                seats[i][j] = 1;
            }
        }
    }
    
    //printSeats(seats, r, s);

    int mirkoMax = 0;
    int shakes = 0;
    for (int i = 0; i < r; i++) 
    {
        for (int j = 0; j < s; j++)
        {
            if (seats[i][j])
            {
                shakes += cntShakes(seats, r, s, i, j);
            }
            else {
                int mirko = cntMirko(seats, r, s, i, j);
                if (mirko > mirkoMax) 
                {
                    mirkoMax = mirko;
                }
            }
        }
    }

    printf("%d", shakes+mirkoMax);
    
}