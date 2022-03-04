#!/usr/bin/env python
"""Creates an 80%/10%/10% split, assuming each line is an example."""

import argparse


def main(args: argparse.Namespace) -> None:
    # It's usually bad to slurp up a single file at once. But the alternative
    # here is rather complicated.
    lines: list[str] = []
    with open(args.input, "r") as source:
        for line in source:
            lines.append(line.rstrip())
    decile = len(lines) // 10
    with open(args.train, "w") as sink:
        for line in lines[:8 * decile]:
            print(line, file=sink)
    with open(args.dev, "w") as sink:
      for line in lines[8 * decile:9 * decile]:
            print(line, file=sink)
    with open(args.test, "w") as sink:
      for line in lines[9 * decile:]:
            print(line, file=sink)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="path to input file")
    parser.add_argument("train", help="path to output training set file")
    parser.add_argument("dev", help="path to output development set file")
    parser.add_argument("test", help="path to output testing set file")
    main(parser.parse_args())
