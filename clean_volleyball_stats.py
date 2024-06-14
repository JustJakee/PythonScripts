import pandas as pd
from io import StringIO

# Data as a multi-line string
data = """Jersey|MatchGamesPlayed|TotalServes|ServingAces|ServingErrors|ServingPoints|AttacksAttempts|AttacksKills|AttacksErrors|ServingReceivedSuccess|ServingReceivedErrors|BlocksSolo|BlocksAssists|BlocksErrors|BallHandlingAttempt|Assists|AssistsErrors|Digs|DigsErrors
3|5|18|1|3|8|0|0|0|28|0|0|0|0|6|0|0|13|0
4|3|0|0|0|0|5|1|2|0|0|0|2|0|0|0|0|1|0
5|2|0|0|0|0|3|1|2|0|0|0|0|0|1|0|1|0|0
7|5|19|2|2|8|32|11|4|26|1|0|0|0|2|1|1|9|0
8|5|21|2|1|10|70|22|6|31|0|0|0|0|14|7|0|22|0
9|5|10|0|1|2|28|11|6|0|0|0|0|0|0|0|0|2|0
10|4|0|0|0|0|11|1|2|1|0|1|4|0|0|0|0|3|0
11|5|15|1|4|4|30|13|6|4|0|1|6|0|111|41|0|12|0
12|5|24|2|0|15|0|0|0|0|0|0|0|0|3|1|0|8|0
13|5|4|0|0|3|0|0|0|1|0|0|0|0|37|10|1|5|0"""

df = pd.read_csv(StringIO(data), delimiter='|')

print(df)

# (1) MatchGamesPlayed -> GP
# (2) TotalServes -> Serving ATT
# (3) ServingErrors -> Serving ERR
# (4) ServingPoints -> Serving PTS
# (5) ServingAces -> Serving ACE
# (6) AttacksAttempts -> Attack Att
# (7) AttacksKills -> Attack KLS
# (8) AttacksErrors -> Attack ERR
# (9) ServingReceivedSuccess -> Srv Rec TOT
# (10) ServingReceivedErrors -> Srv Rec ERR
# (11) BlocksSolo -> Block SLO
# (12) BlocksAssists -> Block AST
# (13) Assists -> Assists
# (14) Digs -> Digs TOT

# BlocksErrors #This is a null field
# BallHandlingAttempt #This is a null field 
# AssistsErrors #This is a null field
# DigsErrors -> Digs E #This is a null field

df.to_csv('cleaned_volleyball_stats.csv', index=False)
