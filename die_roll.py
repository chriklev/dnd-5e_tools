#!/usr/bin/env python3

import argparse
import numpy as np
import re

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tool for rolling die.')
    parser.add_argument('dies', nargs='+', type=str,
                        help='give dies to roll in format nds+x where n is numbers of dies, s is size of the dies, and x is added to the sum. Eksample: 2d10+3')
    args = parser.parse_args()

    for s in args.dies:
        print(s)
        m = re.match("(\d+)d(\d+)", s)
        if m:
            rolls = np.random.randint(1, int(m.group(2))+1, int(m.group(1)))
        else:
            print("Wrong syntax! Run \'die_roll.py -h\' for help")

        summ = rolls.sum()
        bonus = re.match("\d+d\d+\+(\d+)", s)
        if bonus:
            summ += int(bonus.group(1))

        print(rolls, summ)
