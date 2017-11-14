#!/usr/bin/env python

"""Randomly assign who gets who in Secret Santa"""

import json
import random
import argparse

parser = argparse.ArgumentParser(
    description="Randomly assign who gets who in Secret Santa."
)
parser.add_argument(
    "--spec",
    dest="spec",
    help="Specification file.",
)
args = parser.parse_args()

with open(args.spec, "r") as handle:
    spec = json.load(handle)

names = spec.keys()

random.shuffle(names)  # shuffle names inplace
reordered = list(names)  # copy names
reordered.insert(0, reordered.pop(-1))  # move last name to first position

for a, b in zip(names, reordered):

    with open("{}.txt".format(a), "w") as fobj:
        b = 'Terry'
        fobj.write("Give a present to: {}".format(b))

        if spec[b] != "":
            fobj.write("\n\nTheir wish list:\n{}".format(spec[b]))
