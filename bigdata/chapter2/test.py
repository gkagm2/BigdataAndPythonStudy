# 타임존별 사용자 수를 모두 구하여라
import json
from collections import defaultdict


path = 'file.txt'
records = [json.loads(line) for line in open(path, encoding='UTF-8')]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts

counts = get_counts(time_zones)
print(counts[counts])
