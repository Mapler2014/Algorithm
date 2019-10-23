import random
# from itertools import count, groupby
from itertools import islice
import  sys
import time
import gzip

def next_n_lines(file_opened, N):
    return [x.strip() for x in islice(file_opened, N)]

SAMPLE_COUNT = 1000000
# Force the value of the seed so the results are repeatable
random.seed(145)
sample_data = []
index = 0
start_time=time.time()

# for index, line in enumerate(open("scratch_1.csv")):
with gzip.open(sys.argv[1], 'r') as sampleR1:
# Generate the reservoir
    while True:
        buffer = next_n_lines(sampleR1, 4)
        if not buffer:
            break
        if index < SAMPLE_COUNT:
            sample_data.append(buffer)
        else:
        # Randomly replace elements in the reservoir
        # with a decreasing probability.
        # Choose an integer between 0 and index (inclusive)
            r = random.randint(0, index)
            if r < SAMPLE_COUNT:
                sample_data[r] = buffer
        index += 1

print(sample_data)
print "running time %s sec" %(time.time() - start_time)
