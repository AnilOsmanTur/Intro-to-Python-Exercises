import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', default='example', help='example argument')
parser.add_argument('--value', default=0, type=int, help='example int value argument')
args, unknown = parser.parse_known_args()

print(sys.argv)
print(args)
print(unknown)
