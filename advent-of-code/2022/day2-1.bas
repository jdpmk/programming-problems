DIM opp_move AS STRING
DIM my_move AS STRING
DIM score AS INTEGER
DIM t AS STRING
DIM rc AS LONG

FUNCTION MoveScore(move AS STRING) AS INTEGER
    /' rock '/
    IF move = "X" THEN
        RETURN 1
    /' paper '/
    ELSEIF move = "Y" THEN
        RETURN 2
    /' scissors '/
    ELSE
        RETURN 3
    ENDIF
END FUNCTION

FUNCTION ResultScore(opp_move AS STRING, my_move AS STRING) AS INTEGER
    /' draw '/
    IF (opp_move = "A" AND my_move = "X") OR (opp_move = "B" AND my_move = "Y") OR (opp_move = "C" AND my_move = "Z") THEN
        RETURN 3
    /' win '/
    ELSEIF (opp_move = "A" AND my_move = "Y") OR (opp_move = "B" AND my_move = "Z") OR (opp_move = "C" AND my_move = "X") THEN
        RETURN 6
    /' lose '/
    ELSE
        RETURN 0
    ENDIF
END FUNCTION

rc = OPEN("input/2.data" FOR INPUT AS #1)
IF rc <> 0 THEN
    PRINT "Failed to find input file"
    END 1
ENDIF

DO UNTIL EOF(1)
    opp_move = INPUT(1, 1)
    t        = INPUT(1, 1)  /' read the space '/
    my_move  = INPUT(1, 1)
    t        = INPUT(1, 1)  /' read the newline '/

    score += MoveScore(my_move)
    score += ResultScore(opp_move, my_move)
LOOP

PRINT score

CLOSE
