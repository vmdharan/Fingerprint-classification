# RunTests.py
# Run the Fingerprint program on the test cases.

import Fingerprint
import csv

f = Fingerprint.Fingerprint()

# Open the test file
with open('../tests/testfile1.csv', 'r') as tf:
    reader = csv.reader(tf)
    fp_data = list(reader)

# Process the input and identify the grouping.
print(fp_data[0])
print(fp_data[1])

exp_result = [int(x) for x in fp_data[1]]

test_result = f.Henry(fp_data[0])
print(test_result)
print(exp_result)

# Determine whether the application passes or fails testing.
if (test_result != exp_result):
    print('Test failed.')
else:
    print('Test passed.')
