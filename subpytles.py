#!/usr/bin/env python

import argparse
import os

from subpytles import SrtEditor


parser = argparse.ArgumentParser(description="Edit a \".srt\" file")
parser.add_argument('--delay', metavar='-d', default=0, type=int, help="Delay in milliseconds, positive or negative")
parser.add_argument('--start', metavar='-s', default=None, type=str, help="Treat subtitles from this time")
parser.add_argument('--end', metavar='-e', default=None, type=str, help="Treat subtitles until this time")
parser.add_argument('filepath', type=str, help="Path of srt file")
args = parser.parse_args()

filepath = os.path.realpath(args.filepath)

content = file(filepath).read()
editor = SrtEditor(content)
if args.delay:
    editor.delay(args.delay)
if args.start or args.end:
    editor.slice(start_time=args.start, end_time=args.end)

print editor.content
