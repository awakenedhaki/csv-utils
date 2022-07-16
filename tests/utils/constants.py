import os

def traverse_parents(path, nupwards):
    if nupwards == 0:
        return path
    return traverse_parents(os.path.split(path)[0], nupwards - 1)

CONSTANTS_SCRIPT = os.path.realpath(__file__)
TEST_DIR = traverse_parents(CONSTANTS_SCRIPT, 2)

DATA_DIR = os.path.join(TEST_DIR, 'data')