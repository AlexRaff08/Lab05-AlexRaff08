# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("filename", help="the file to search")

    args = parser.parse_args()

    with open(args.filename) as file:
        for line_number, line in enumerate(file, start=1):
            text = line.rstrip("\n")

            if args.ignore_case:
                match = args.pattern.lower() in text.lower()
            else:
                match = args.pattern in text

            if match:
                print(f"{line_number}: {text}")


if __name__ == "__main__":
    main()
    
    args = parser.parse_args()
    # TODO: open args.filename and read its lines. For each line, numbered starting
    #   at 1, print "<number>: <line>" when the line contains args.pattern.
    #   If the --ignore-case flag was given, match without caring about upper/lower
    #   case (hint: compare the lowercased versions of both).


if __name__ == "__main__":
    main()
