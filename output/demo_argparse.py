import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('alpha', type=int, default=1, nargs='?', help='first term')
parser.add_argument('-b', '--beta', type=int, default=2, nargs='?')
parser.add_argument('-g', '--gamma', type=int, default=3, nargs='?')
parser.add_argument('delta', type=int, default=4, nargs='?')
args = parser.parse_args()

print(f'alpha={args.alpha}, beta={args.beta}, gamma={args.gamma}, delta={args.delta}')
