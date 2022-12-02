#include <stdio.h>
#include <stdlib.h>

#define O_ROCK ('A')
#define O_PAPR ('B')
#define O_SCIS ('C')

#define R_LOSE ('X')
#define R_DRAW ('Y')
#define R_WINN ('Z')

int player_move_score(int opponent, int outcome) {
    if (opponent == O_ROCK) {
        if (outcome == R_LOSE) return 3;
        if (outcome == R_DRAW) return 1;
        if (outcome == R_WINN) return 2;
    }

    if (opponent == O_PAPR) {
        if (outcome == R_LOSE) return 1;
        if (outcome == R_DRAW) return 2;
        if (outcome == R_WINN) return 3;
    }

    if (opponent == O_SCIS) {
        if (outcome == R_LOSE) return 2;
        if (outcome == R_DRAW) return 3;
        if (outcome == R_WINN) return 1;
    }

    return -1;
}

int outcome_score(int outcome) {
    if (outcome == R_LOSE) return 0;
    if (outcome == R_DRAW) return 3;
    if (outcome == R_WINN) return 6;

    return -1;
}

int main(int argc, char **argv) {
    FILE *f = fopen("input/2.data", "r");

    char *line;
    size_t len;
    int player_score = 0;

    while (getline(&line, &len, f) != -1) {
        int opponent = line[0];
        int outcome = line[2];

        player_score += player_move_score(opponent, outcome) + outcome_score(outcome);
    }

    printf("%d\n", player_score);

    free(line);
    fclose(f);

    return 0;
}
