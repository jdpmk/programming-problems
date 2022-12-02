#include <stdio.h>
#include <stdlib.h>

#define O_ROCK ('A')
#define O_PAPR ('B')
#define O_SCIS ('C')

#define P_ROCK ('X')
#define P_PAPR ('Y')
#define P_SCIS ('Z')

int player_move_score(int player) {
    return player - (P_ROCK - 1);
}

int outcome_score(int a, int b) {
    if ((a == O_ROCK && b == P_ROCK) ||
        (a == O_PAPR && b == P_PAPR) ||
        (a == O_SCIS && b == P_SCIS))
    {
        return 3;
    }

    if ((a == O_ROCK && b == P_PAPR) ||
        (a == O_PAPR && b == P_SCIS) ||
        (a == O_SCIS && b == P_ROCK))
    {
        return 6;
    }

    return 0; 
}

int main(int argc, char **argv) {
    FILE *f = fopen("input/2.data", "r");

    char *line;
    size_t len;
    int player_score = 0;

    while (getline(&line, &len, f) != -1) {
        int opponent = line[0];
        int player = line[2];

        player_score += player_move_score(player) + outcome_score(opponent, player);
    }

    printf("%d\n", player_score);

    free(line);
    fclose(f);

    return 0;
}
