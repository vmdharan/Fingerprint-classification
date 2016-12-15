# RunTests.py
# Run the Fingerprint program on the test cases.

import os
import csv
import Fingerprint

# Instantiate the Fingerprint class.
f = Fingerprint.Fingerprint()

# Loop over all the test cases in the test directory.
test_directory = '../tests'
for test_file in os.listdir(test_directory):
    if (test_file.endswith('.tst')):
        print (test_file)

        # Evaluate the full path to the file.
        test_file_path = test_directory + '/' + test_file
        print(test_file_path)
        
        # Open the test file
        with open(test_file_path, 'r') as tf:
            reader = csv.reader(tf)
            fp_data = list(reader)

            # Process the input and identify the grouping.
            print(fp_data[0])
            print(fp_data[1])

            # Get the expected result.
            exp_result = [int(x) for x in fp_data[1]]

            # Get the actual test result.
            test_result = f.Henry(fp_data[0])

            # Display results.
            print(test_result)
            print(exp_result)

            # Determine whether the application passes or fails testing.
            if (test_result != exp_result):
                print('Test failed.')
            else:
                print('Test passed.')

    # Display an error if the test case could not be accessed.
    else:
        print ('Unspecified error')
