# Tennis scores challenge

 A tennis match is made up of sets. A set is made up of games.

To win a set, a player has to win 6 games with a difference of 2 games. At 6-6, there is often a special tie-breaker. In some cases, players go on playing till one of them wins the set with a difference of two games.

Tennis matches can be either 3 sets or 5 sets. The player who wins a majority of sets wins the match (i.e., 2 out 3 sets or 3 out of 5 sets) The score of a match lists out the games in each set, with the overall winner's score reported first for each set. Thus, if the score is 6-3, 5-7, 7-6 it means that the first player won the first set by 6 games to 3, lost the second one 5 games to 7 and won the third one 7 games to 6 (and hence won the overall match as well by 2 sets to 1).

You will read input from the keyboard (standard input) containing the results of several tennis matches. Each match's score is recorded on a separate line with the following format:

    Winner:Loser:Set-1-score,...,Set-k-score, where 2 ≤ k ≤ 5

For example, an input line of the form

Osaka:Barty:3-6,6-3,6-3
indicates that Osaka beat Barty 3-6, 6-3, 6-3 in a best of 3 set match.

The input is terminated by a blank line.

You have to write a Python program that reads information about all the matches and compile the following statistics for each player:

1. Number of best-of-5 set matches won
2. Number of best-of-3 set matches won
3. Number of sets won
4. Number of games won
5. Number of sets lost
6. Number of games lost

You should print out to the screen (standard output) a summary in decreasing order of ranking, where the ranking is according to the criteria 1-6 in that order (compare item 1, if equal compare item 2, if equal compare item 3 etc, noting that for items 5 and 6 the comparison is reversed).

For instance, given the following data

    Zverev:Medvedev:2-6,6-7,7-6,6-3,6-1
    Barty:Osaka:6-4,6-4
    Medvedev:Zverev:6-3,6-3
    Osaka:Barty:1-6,7-5,6-2
    Zverev:Medvedev:6-0,7-6,6-3
    Osaka:Barty:2-6,6-2,6-0
    Medvedev:Zverev:6-3,4-6,6-3,6-4
    Barty:Osaka:6-1,3-6,7-5
    Zverev:Medvedev:7-6,4-6,7-6,2-6,6-2
    Osaka:Barty:6-4,1-6,6-3
    Medvedev:Zverev:7-5,7-5
    Osaka:Barty:3-6,6-3,6-3

your program should print out the following

    Player,5SW,3SW,TSW,TGW,TSL,TGL
    ['Zverev', 2, 1, 10, 104, 11, 106]
    ['Barty', 0, 2, 8, 74, 9, 76]
    ['Medvedev', 1, 2, 11, 106, 10, 104]
    ['Osaka', 0, 4, 9, 76, 8, 74]

You can assume that there are no spaces around the punctuation marks ":", "-" and ",". Each player's name will be spelled consistently and no two players have the same name.


You have the following test cases and their expected output.

Test case 1.

    Zverev:Medvedev:2-6,6-7,7-6,6-3,6-1
    Barty:Osaka:6-4,6-4
    Medvedev:Zverev:6-3,6-3
    Osaka:Barty:1-6,7-5,6-2
    Zverev:Medvedev:6-0,7-6,6-3
    Osaka:Barty:2-6,6-2,6-0
    Medvedev:Zverev:6-3,4-6,6-3,6-4
    Barty:Osaka:6-1,3-6,7-5
    Zverev:Medvedev:7-6,4-6,7-6,2-6,6-2
    Osaka:Barty:6-4,1-6,6-3
    Medvedev:Zverev:7-5,7-5
    Osaka:Barty:3-6,6-3,6-3

Expected output:

    ['Zverev', 2, 1, 10, 104, 11, 106]
    ['Barty', 0, 2, 8, 74, 9, 76]
    ['Medvedev', 1, 2, 11, 106, 10, 104]
    ['Osaka', 0, 4, 9, 76, 8, 74]


Test case 2:

    Gauff:Zverev:2-6,6-7,7-6,6-3,6-1
    Tsitsipas:Zverev:6-3,4-6,6-4,6-3
    Zverev:Thiem:6-0,7-6,6-7,6-3
    Thiem:Zverev:6-4,6-4
    Gauff:Zverev:2-6,6-2,6-0
    Thiem:Zverev:6-3,4-6,6-3,6-4
    Zverev:Thiem:7-6,4-6,7-6,2-6,6-2
    Thiem:Tsitsipas:7-5,7-5
    Gauff:Tsitsipas:3-6,6-3,6-3
    Gauff:Thiem:0-6,0-6,6-0,6-0,7-5
    Tsitsipas:Thiem:6-3,4-6,7-6,0-6,7-5

Expected output:

    ['Gauff', 2, 2, 10, 75, 6, 60]
    ['Tsitsipas', 2, 0, 7, 68, 7, 71]
    ['Zverev', 2, 0, 11, 122, 16, 139]
    ['Thiem', 1, 2, 14, 133, 13, 128]    


Test case 3:

    Djokovic:Nadal:2-6,6-7,7-6,6-3,6-1
    Nadal:Djokovic:6-3,4-6,6-4,6-3
    Djokovic:Nadal:6-0,7-6,6-7,6-3
    Nadal:Djokovic:6-4,6-4
    Djokovic:Nadal:2-6,6-2,6-0
    Nadal:Djokovic:6-3,4-6,6-3,6-4
    Djokovic:Nadal:7-6,4-6,7-6,2-6,6-2
    Nadal:Djokovic:7-5,7-5
    Williams:Muguruza:3-6,6-3,6-3
    Muguruza:Williams:6-4,6-4
    Williams:Muguruza:2-6,6-2,6-0
    Muguruza:Williams:6-3,4-6,6-4,6-3
    Williams:Muguruza:6-0,7-6,6-7,6-3
    Muguruza:Williams:6-3,4-6,6-4,6-3
    Williams:Muguruza:6-0,7-6,6-7,6-3
    Muguruza:Williams:6-3,4-6,6-4,6-3
    Williams:Muguruza:6-0,7-6,6-7,6-3

Expected output:

    ['Djokovic', 3, 1, 13, 142, 16, 143]
    ['Nadal', 2, 2, 16, 143, 13, 142]
    ['Williams', 3, 2, 16, 160, 16, 146]
    ['Muguruza', 3, 1, 16, 146, 16, 160]