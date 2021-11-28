"""
--- Part Two ---
You lost to the small crab! Fortunately, crabs aren't very good at recursion. To defend your honor as a Raft Captain, you challenge the small crab to a game of Recursive Combat.

Recursive Combat still starts by splitting the cards into two decks (you offer to play with the same starting decks as before - it's only fair). Then, the game consists of a series of rounds with a few changes:

        Before either player deals a card, if there was a previous round in this game that had exactly the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1. Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
        Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.
        If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat (see below).
        Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the round is the player with the higher-value card.
        As in regular Combat, the winner of the round (even if they won the round by winning a sub-game) takes the two cards dealt at the beginning of the round and places them on the bottom of their own deck (again so that the winner's card is above the other card). Note that the winner's card might be the lower-valued of the two cards if they won the round due to winning a sub-game. If collecting cards by winning the round causes a player to have all of the cards, they win, and the game ends.

                Here is an example of a small game that would loop forever without the infinite game prevention rule:

                Player 1:
                43
                19

                Player 2:
                2
                29
                14
                During a round of Recursive Combat, if both players have at least as many cards in their own decks as the number on the card they just dealt, the winner of the round is determined by recursing into a sub-game of Recursive Combat. (For example, if player 1 draws the 3 card, and player 2 draws the 7 card, this would occur if player 1 has at least 3 cards left and player 2 has at least 7 cards left, not counting the 3 and 7 cards that were drawn.)

                To play a sub-game of Recursive Combat, each player creates a new deck by making a copy of the next cards in their deck (the quantity of cards copied is equal to the number on the card they drew to trigger the sub-game). During this sub-game, the game that triggered it is on hold and completely unaffected; no cards are removed from players' decks to form the sub-game. (For example, if player 1 drew the 3 card, their deck in the sub-game would be copies of the next three cards in their deck.)

                Here is a complete example of gameplay, where Game 1 is the primary game of Recursive Combat:

                    === Game 1 ===

                    -- Round 1 (Game 1) --
                    Player 1's deck: 9, 2, 6, 3, 1
                    Player 2's deck: 5, 8, 4, 7, 10
                    Player 1 plays: 9
                    Player 2 plays: 5
                    Player 1 wins round 1 of game 1!

                    -- Round 2 (Game 1) --
                    Player 1's deck: 2, 6, 3, 1, 9, 5
                    Player 2's deck: 8, 4, 7, 10
                    Player 1 plays: 2
                    Player 2 plays: 8
                    Player 2 wins round 2 of game 1!

                    -- Round 3 (Game 1) --
                    Player 1's deck: 6, 3, 1, 9, 5
                    Player 2's deck: 4, 7, 10, 8, 2
                    Player 1 plays: 6
                    Player 2 plays: 4
                    Player 1 wins round 3 of game 1!

                    -- Round 4 (Game 1) --
                    Player 1's deck: 3, 1, 9, 5, 6, 4
                    Player 2's deck: 7, 10, 8, 2
                    Player 1 plays: 3
                    Player 2 plays: 7
                    Player 2 wins round 4 of game 1!

                    -- Round 5 (Game 1) --
                    Player 1's deck: 1, 9, 5, 6, 4
                    Player 2's deck: 10, 8, 2, 7, 3
                    Player 1 plays: 1
                    Player 2 plays: 10
                    Player 2 wins round 5 of game 1!

                    -- Round 6 (Game 1) --
                    Player 1's deck: 9, 5, 6, 4
                    Player 2's deck: 8, 2, 7, 3, 10, 1
                    Player 1 plays: 9
                    Player 2 plays: 8
                    Player 1 wins round 6 of game 1!

                    -- Round 7 (Game 1) --
                    Player 1's deck: 5, 6, 4, 9, 8
                    Player 2's deck: 2, 7, 3, 10, 1
                    Player 1 plays: 5
                    Player 2 plays: 2
                    Player 1 wins round 7 of game 1!

                    -- Round 8 (Game 1) --
                    Player 1's deck: 6, 4, 9, 8, 5, 2
                    Player 2's deck: 7, 3, 10, 1
                    Player 1 plays: 6
                    Player 2 plays: 7
                    Player 2 wins round 8 of game 1!

                    -- Round 9 (Game 1) --
                    Player 1's deck: 4, 9, 8, 5, 2
                    Player 2's deck: 3, 10, 1, 7, 6
                    Player 1 plays: 4
                    Player 2 plays: 3
                    Playing a sub-game to determine the winner...

                    === Game 2 ===

                    -- Round 1 (Game 2) --
                    Player 1's deck: 9, 8, 5, 2
                    Player 2's deck: 10, 1, 7
                    Player 1 plays: 9
                    Player 2 plays: 10
                    Player 2 wins round 1 of game 2!

                    -- Round 2 (Game 2) --
                    Player 1's deck: 8, 5, 2
                    Player 2's deck: 1, 7, 10, 9
                    Player 1 plays: 8
                    Player 2 plays: 1
                    Player 1 wins round 2 of game 2!

                    -- Round 3 (Game 2) --
                    Player 1's deck: 5, 2, 8, 1
                    Player 2's deck: 7, 10, 9
                    Player 1 plays: 5
                    Player 2 plays: 7
                    Player 2 wins round 3 of game 2!

                    -- Round 4 (Game 2) --
                    Player 1's deck: 2, 8, 1
                    Player 2's deck: 10, 9, 7, 5
                    Player 1 plays: 2
                    Player 2 plays: 10
                    Player 2 wins round 4 of game 2!

                    -- Round 5 (Game 2) --
                    Player 1's deck: 8, 1
                    Player 2's deck: 9, 7, 5, 10, 2
                    Player 1 plays: 8
                    Player 2 plays: 9
                    Player 2 wins round 5 of game 2!

                    -- Round 6 (Game 2) --
                    Player 1's deck: 1
                    Player 2's deck: 7, 5, 10, 2, 9, 8
                    Player 1 plays: 1
                    Player 2 plays: 7
                    Player 2 wins round 6 of game 2!
                    The winner of game 2 is player 2!

                    ...anyway, back to game 1.
                    Player 2 wins round 9 of game 1!

                    -- Round 10 (Game 1) --
                    Player 1's deck: 9, 8, 5, 2
                    Player 2's deck: 10, 1, 7, 6, 3, 4
                    Player 1 plays: 9
                    Player 2 plays: 10
                    Player 2 wins round 10 of game 1!

                    -- Round 11 (Game 1) --
                    Player 1's deck: 8, 5, 2
                    Player 2's deck: 1, 7, 6, 3, 4, 10, 9
                    Player 1 plays: 8
                    Player 2 plays: 1
                    Player 1 wins round 11 of game 1!

                    -- Round 12 (Game 1) --
                    Player 1's deck: 5, 2, 8, 1
                    Player 2's deck: 7, 6, 3, 4, 10, 9
                    Player 1 plays: 5
                    Player 2 plays: 7
                    Player 2 wins round 12 of game 1!

                    -- Round 13 (Game 1) --
                    Player 1's deck: 2, 8, 1
                    Player 2's deck: 6, 3, 4, 10, 9, 7, 5
                    Player 1 plays: 2
                    Player 2 plays: 6
                    Playing a sub-game to determine the winner...

                    === Game 3 ===

                    -- Round 1 (Game 3) --
                    Player 1's deck: 8, 1
                    Player 2's deck: 3, 4, 10, 9, 7, 5
                    Player 1 plays: 8
                    Player 2 plays: 3
                    Player 1 wins round 1 of game 3!

                    -- Round 2 (Game 3) --
                    Player 1's deck: 1, 8, 3
                    Player 2's deck: 4, 10, 9, 7, 5
                    Player 1 plays: 1
                    Player 2 plays: 4
                    Playing a sub-game to determine the winner...

                    === Game 4 ===

                    -- Round 1 (Game 4) --
                    Player 1's deck: 8
                    Player 2's deck: 10, 9, 7, 5
                    Player 1 plays: 8
                    Player 2 plays: 10
                    Player 2 wins round 1 of game 4!
                    The winner of game 4 is player 2!

                    ...anyway, back to game 3.
                    Player 2 wins round 2 of game 3!

                    -- Round 3 (Game 3) --
                    Player 1's deck: 8, 3
                    Player 2's deck: 10, 9, 7, 5, 4, 1
                    Player 1 plays: 8
                    Player 2 plays: 10
                    Player 2 wins round 3 of game 3!

                    -- Round 4 (Game 3) --
                    Player 1's deck: 3
                    Player 2's deck: 9, 7, 5, 4, 1, 10, 8
                    Player 1 plays: 3
                    Player 2 plays: 9
                    Player 2 wins round 4 of game 3!
                    The winner of game 3 is player 2!

                    ...anyway, back to game 1.
                    Player 2 wins round 13 of game 1!

                    -- Round 14 (Game 1) --
                    Player 1's deck: 8, 1
                    Player 2's deck: 3, 4, 10, 9, 7, 5, 6, 2
                    Player 1 plays: 8
                    Player 2 plays: 3
                    Player 1 wins round 14 of game 1!

                    -- Round 15 (Game 1) --
                    Player 1's deck: 1, 8, 3
                    Player 2's deck: 4, 10, 9, 7, 5, 6, 2
                    Player 1 plays: 1
                    Player 2 plays: 4
                    Playing a sub-game to determine the winner...

                    === Game 5 ===

                    -- Round 1 (Game 5) --
                    Player 1's deck: 8
                    Player 2's deck: 10, 9, 7, 5
                    Player 1 plays: 8
                    Player 2 plays: 10
                    Player 2 wins round 1 of game 5!
                    The winner of game 5 is player 2!

                    ...anyway, back to game 1.
                    Player 2 wins round 15 of game 1!

                    -- Round 16 (Game 1) --
                    Player 1's deck: 8, 3
                    Player 2's deck: 10, 9, 7, 5, 6, 2, 4, 1
                    Player 1 plays: 8
                    Player 2 plays: 10
                    Player 2 wins round 16 of game 1!

                    -- Round 17 (Game 1) --
                    Player 1's deck: 3
                    Player 2's deck: 9, 7, 5, 6, 2, 4, 1, 10, 8
                    Player 1 plays: 3
                    Player 2 plays: 9
                    Player 2 wins round 17 of game 1!
                    The winner of game 1 is player 2!


                    == Post-game results ==
                    Player 1's deck: 
                    Player 2's deck: 7, 5, 6, 2, 4, 1, 10, 8, 9, 3
                    After the game, the winning player's score is calculated from the cards they have in their original deck using the same rules as regular Combat. In the above game, the winning player's score is 291.

                    Defend your honor as Raft Captain by playing the small crab in a game of Recursive Combat using the same two decks as before. What is the winning player's score?
"""

import collections

def play(p1, p2, g=1, r=1):
    seen = set()
    p1 = collections.deque(p1)
    p2 = collections.deque(p2)

    while p1 and p2:
        if (tuple(p1), tuple(p2)) in seen:
            return "p1", p1
        seen.add((tuple(p1), tuple(p2)))
        c1 = p1.popleft()
        c2 = p2.popleft()
        if c1 <= len(p1) and c2 <= len(p2):
            winner, _ = play(list(p1)[:c1], list(p2)[:c2], g=g+1)
            if winner == "p1":
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        else:
            if c1 > c2:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        r += 1

    return ("p1", p1) if p1 and not p2 else ("p2", p2)

def solve(data):
    p1, p2 = data
    p1 = [int(card) for card in p1[1:] if card]
    p2 = [int(card) for card in p2[1:] if card]
    _, win= play(p1, p2)

    score = 0
    idx = 1
    while win:
        score += win.pop() * idx
        idx += 1

    return score

def main():
    with open("input/22.sample") as f:
        data = ""
        for line in f:
            data += line
        print(solve([player.split("\n") for player in data.split("\n\n")]))

if __name__ == "__main__":
    main()
