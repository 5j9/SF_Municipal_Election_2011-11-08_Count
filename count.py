from collections import defaultdict
from itertools import count
from pprint import pprint as pp

voter_to_votes = defaultdict(list)
# Downloaded from http://www.sfelections.org/results/20111108/data/Mayor.zip
with open('Mayor-BallotImage.txt') as file:
    for line in file:
        voter_id = int(line[7:16])
        vote = int(line[33:36])
        cand = int(line[37:43])
        # overvote = line[43]
        undervote = int(line[44])
        votes = voter_to_votes[voter_id]
        if not undervote and vote not in votes:
            votes.append(cand)

for r in count(1):
    counts = defaultdict(int)
    for votes in voter_to_votes.values():
        if votes:
            counts[votes[0]] += 1
    counts.pop(0)
    minimum = min(counts.values())
    for votes in voter_to_votes.values():
        for vote in votes.copy():
            if counts[vote] <= minimum and vote != 0:
                votes.remove(vote)
    print('Round', r)
    pp(dict(counts))
    if len(counts) == 2:
        break
