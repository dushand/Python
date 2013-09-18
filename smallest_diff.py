#The file football.txt contains the results from the English Premier League for 2001/2. The columns labeled ‘F’ and ‘A’ contain the total number of goals scored for and against each team in that season (so Arsenal scored 79 goals against opponents, and had 36 goals scored against them). Need a java program to print the name of the team with the smallest difference in ‘for’ and ‘against’ goals. 
#-------------------------------------------------------------------------------------------------------------
#Main objective of this question is to identify the activities we will be able to write the code and demonstrate some of the practices and techniques that we would use in best practices under industry. This is mainly be looking for the thought process and how we can complete this task. But points goes to the first/best post.

import re

def getTheXTeam(fname, rex=re.compile(r'''^\s*\d+\.
                     \s+(?P<Team>.+?)
                     \s+(?P<P>\d+)
                     \s+(?P<W>\d+)
                     \s+(?P<L>\d+)
                     \s+(?P<D>\d+)
                     \s+(?P<F>\d+)
                     \s+-
                     \s+(?P<A>\d+)
                     \s+(?P<Pts>\d+)
                     \s*$''', re.VERBOSE)):

    diff =  10000     # init -- impossible result in reality
    team_name = None  # init

    with open(fname) as f:              # open in text mode for reading
        for line in f:                  # loop throught the text file lines
            print line.rstrip()
            m = rex.match(line)         
            if m:                       # if it is the line with results
                f = int(m.group('F'))   # convert the wanted numbers to int
                a = int(m.group('A'))
                
                if abs(f - a) < abs(diff):      # if smaller difference 
                    diff = f - a                # remember the result
                    team_name = m.group('Team') # and the team
    return team_name, diff            
                

team_name, result = getTheXTeam('football.txt')

print team_name, 'is the team with the result', result