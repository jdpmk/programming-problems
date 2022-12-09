DIM opp_move AS STRING
DIM outcome AS STRING
DIM score AS INTEGER
DIM t AS STRING
DIM rc AS LONG

FUNCTION OutcomeScore(outcome AS STRING) AS INTEGER
    /' loss '/
    IF outcome = "X" THEN
        RETURN 0
        /' draw '/
    ELSEIF outcome = "Y" THEN
        RETURN 3
        /' win '/
    ELSE
        RETURN 6
    ENDIF
END FUNCTION

FUNCTION MoveScore(opp_move AS STRING, outcome AS STRING) AS INTEGER
    /' rock '/
    IF opp_move = "A" THEN
        IF outcome = "X" THEN
            RETURN 3
        ELSEIF outcome = "Y" THEN
            RETURN 1
        ELSE
            RETURN 2
        ENDIF
    /' paper '/
    ELSEIF opp_move = "B" THEN
        IF outcome = "X" THEN
            RETURN 1
        ELSEIF outcome = "Y" THEN
            RETURN 2
        ELSE
            RETURN 3
        ENDIF
    /' scissors '/
    ELSE
        IF outcome = "X" THEN
            RETURN 2
        ELSEIF outcome = "Y" THEN
            RETURN 3
        ELSE
            RETURN 1
        ENDIF
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
    outcome  = INPUT(1, 1)
    t        = INPUT(1, 1)  /' read the newline '/

    score += OutcomeScore(outcome)
    score += MoveScore(opp_move, outcome)
LOOP

PRINT score

CLOSE
