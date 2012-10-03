#!/usr/bin/env python

import argparse
import os

from subpytles import SrtEditor


parser = argparse.ArgumentParser(description="Edit a \".srt\" file")
parser.add_argument('--delay', metavar='-d', default=0, type=int, help="Delay in milliseconds, positive or negative")
parser.add_argument('filepath', type=str, help="Path of srt file")
args = parser.parse_args()

delay = args.delay
filepath = os.path.realpath(args.filepath)


content = file(filepath).read()
editor = SrtEditor(content)
if delay:
    editor.delay(delay)
print editor.content
