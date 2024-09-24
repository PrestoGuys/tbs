import sys
import comp1
from os.path import exists

operation = sys.argv[1]

if operation == '-c':
    print("Beginning Compiling..")
    start_file = sys.argv[2]
    file_exists = exists(start_file)
    if file_exists:
        comp1.begin_comp(start_file)
    elif not file_exists:
        print('ERROR: No file')
        sys.exit()

elif operation == '-v':
    print("TBS (Text Based Scratch) v0.0.1")
    print("Type tbs -h for help.")
