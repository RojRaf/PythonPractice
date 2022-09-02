#!/usr/bin/env python3
'''
Number of best-of-5 set matches won
Number of best-of-3 set matches won
Number of sets won
Number of games won
Number of sets lost
Number of games lost'''
# lines = ()
with open('matches.txt') as f:
  lines = f.readlines()

#Get an uniquer list of winners
def winnersList(matches):
   winners = []
   for line in lines:
      line = line.split(':')
      winner = line[0]
      winners.append(winner) if winner not in winners else winners  
   return(winners)      

#Function to get number of sets won and lost regardless of game won or lost
def analyzeSets(match):
   won = 0
   lost = 0
   for i in match:
      scoreA = int(i.split("-")[0])
      scoreB = int(i.split("-")[1])
      if scoreA > scoreB:
         won +=1
      elif scoreA < scoreB:
         lost +=1
   return(won,lost)  
      

# Python code to convert string to list 
def getScores(string):
   match = []
   amatch = list(string.split(","))
   for i in amatch:
      match.append(i.strip())   
   return match

report = {}

print('Player,5SW,3SW,TSW,TGW,TSL,TGL')

##Loop for games won
for winner in winnersList(lines):
   gamesWon = 0
   gamesLost = 0
   threeSets = 0
   fiveSets = 0
   matchWinCounter = 0
   matchloseCounter = 0   
   report['winner'] = winner
   for line in lines:
      line = line.split(':')
      gameWinner = line[0]
      gameLoser = line[1]
      match = getScores(line[2])
      win,lose = analyzeSets(match)
 
      # loop to count the number mot matches of 3 & 5 won by the player
      if gameWinner == winner:      
         if len(match) <= 3:
            threeSets += 1
         elif len(match) >= 4:
            fiveSets += 1
      
      # loop to get win and lose sets
      if winner == gameWinner:
         win,lose = analyzeSets(match)
         matchWinCounter = matchWinCounter + win
         matchloseCounter = matchloseCounter + lose
         # get the games won and the ones lost
         for i in match:
              scoreA = int(i.split("-")[0]) # count only scores on the left. He's a winner
              scoreB = int(i.split("-")[1])
              gamesWon = gamesWon + scoreA
              gamesLost = gamesLost + scoreB
      elif winner == gameLoser:
         lose,win = analyzeSets(match)
         matchWinCounter = matchWinCounter + win
         matchloseCounter = matchloseCounter + lose
         for i in match:
            scoreA = int(i.split("-")[0]) 
            scoreB = int(i.split("-")[1])  # count only scores on the right. He's a loser
            gamesWon = gamesWon + scoreB
            gamesLost = gamesLost + scoreA

      # full the report    
      report['5sets'] =  fiveSets
      report['3sets'] =  threeSets
      report['setsWon'] = matchWinCounter
      report['gamesWon'] = gamesWon
      report['Setslose'] = matchloseCounter
      report['gamesLost'] = gamesLost
   

   reportList = list(report.values())
   print(reportList)
syllabus = """
Syllabus:
Player: Player's name
5SW: 5 sets game won.
3SW: 3 sets game won.
TSW: Total sets won
TGW: Total of games won.
TSL: Total sets lost.
TGL: Total games lost.
GL: Number of games lost.
"""
#print(syllabus)