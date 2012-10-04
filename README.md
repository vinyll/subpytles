Subpytles allows you to edit your ".srt" subtitles file to delay all of it.

The purpose of this project is to delay the subtitles of a srt file that does not exactly match the movie timing.

As of now you can :

- delay subtitles appearance for the whole file


# How to use

just run :

    ./subpytles.py --delay 6000 /path/to/your/file.srt > my-output-file.srt

and you'll have a new "my-output-file.srt" with subtitles delayed of 6 seconds (6000 milliseconds).


# FAQ

### How to know how much time to delay ?

Use the great VLC player and press "h" and "j" keys to delay subtitles. VLC will display the delay in milliseconds. That's the information you need for this script.

### What systems are supported ?

Mac OS and Linux (actually all Unix based system with python)
