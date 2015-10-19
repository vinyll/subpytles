# Subpytles – python subtitles time editing

Subpytles allows you to edit your ".srt" subtitles file to delay all of them directly from the terminal.

The purpose of this project is to delay the subtitles of a srt file that does not exactly match the movie timing.

Test status: [![Travis tests](https://travis-ci.org/vinyll/subpytles.svg)](https://travis-ci.org/vinyll/subpytles)

> This version is for python3.
> If you are using python2 checkout the [python2 branch](https://github.com/vinyll/subpytles/tree/python2).

## Features

- delay subtitles appearance for the whole file
- slice out a part of a file and optionnaly apply a delay on it.


## Usage

    positional arguments:
      filepath    Path of srt file

    optional arguments:
      -h, --help  show this help message and exit
      --delay -d  Delay in milliseconds, positive or negative
      --start -s  Treat subtitles from this time
      --end -e    Treat subtitles until this time


## Examples

Output subtitles and forward them of 6 seconds

    ./subpytles.py --delay 6000 /path/to/your/file.srt

Output subtitles and backward them of 8 seconds. Save it into a new file called _updated_subtitles.srt_

    ./subpytles.py --delay -8000 /path/to/your/file.srt > updated_subtitles.srt

Extract subtitles after time 0:01:41

    ./subpytles.py --start=0:01:41 fixtures/subtitles.srt

Extract subtitles between time 0:01:41 and 0:01:43,400

    ./subpytles.py --start=0:01:41 --end=0:01:43,400 fixtures/subtitles.srt

Extract subtitles between time 0:01:41 and 0:01:43,400 and apply a delay onto it

    ./subpytles.py --delay=5000 --start=0:01:41 --end=0:01:43,400 fixtures/subtitles.srt

Extract subtitles between time 0:01:41 and 0:01:43,400. Apply a delay onto it. Save it into _updated_subtitles.srt_

    ./subpytles.py --delay=5000 --start=0:01:41 --end=0:01:43,400 fixtures/subtitles.srt > updated_subtitles.srt


## FAQ

### How to know how much time to delay?

Use the great VLC player and press "h" and "j" keys to delay subtitles. VLC will display the delay in milliseconds. That's the information you need for this script.

### What systems are supported?

Mac OS and Linux (actually all Unix based system with python).
