# LAB 2 - HOCKEY TEAM
#Write a program that will ask the user to enter the name of a hockey team, how many wins the team has and 
# how many losses #the team has.

#The program should calculate and display a single string output containing the team name, it's win-loss 
# ratio and the win #percentage formatted to 4 decimal places.

#Ex: The Calgary Flames have 10 wins and 5 losses, with a win percentage of 0.6667.

#Purpose/Concepts: Input and output to screen, string concatentation, string formatting, datatype casting, 
# simple math operations

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    teamName = input("Enter the name a hockey team.")                   #Taking in team name
    teamWins = int(input("Enter how many wins that team has "))         #wins
    teamLosses = int(input("Enter how many losses that team has "))     #losses
    gamesPlayed = teamWins + teamLosses                                 #calculating total games used in next operation
    winPercentage = f"{((teamWins * 100) / gamesPlayed):.4f}"           #calculating win percentage wins x 100 / games played   it is then turned into an f string so it can be printed without doing so in the print line 
                            
    
    print("The " + teamName + " have " + str(teamWins) + " wins and " + str(teamLosses) + " losses, with a win percentage of "  +  winPercentage)           #print format line turns team wins and team losses into strings using casting     

    # YOUR CODE ENDS HERE

main()