# -*- coding: utf-8 -*-

import re
from datetime import timedelta


row_format = "%(id)s\r\n%(start)s --> %(end)s\r\n%(text)s\r\n\r\n"


def format_timedelta(td):
    # Get total seconds from timedelta
    total_seconds = int(td.total_seconds())
    
    # Calculate hours, minutes, seconds, and milliseconds
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = int((td.total_seconds() - total_seconds) * 1000)

    # Format the time string
    formatted_time = f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"
    return formatted_time


class SrtEditor(object):

    def __init__(self, content, *args, **kwargs):
        content = content.replace('\r', '')
        time_format="\d+:\d+:\d+,\d+"
        rows = re.findall(
            r'(\d+)\n(%(time_format)s) --> (%(time_format)s)\n(.+)\n\n' % locals(),
            content)
        self.time_format = time_format
        self.contents = rows

    def delay(self, time):
        time_format = self.time_format
        time_pattern = time_format.replace('\d+', '(\d+)')
        output = []
        for (id, start, end, text) in self.contents:
            text = text
            t = re.findall(time_pattern, start)[0]
            start_time = timedelta(hours=int(t[0]), minutes=int(t[1]), seconds=int(t[2]), milliseconds=int(t[3]))
            start_delta = start_time + timedelta(milliseconds=time)
            start = format_timedelta(start_delta)
            t = re.findall(time_pattern, end)[0]
            end_time = timedelta(hours=int(t[0]), minutes=int(t[1]), seconds=int(t[2]), milliseconds=int(t[3]))
            end_delta = end_time + timedelta(milliseconds=time)
            end = format_timedelta(end_delta)
            output.append((id, start, end, text))
        self.contents = output

    def slice(self, start_time=None, end_time=None):
        output = []
        for (id, start, end, text) in self.contents:
            if (not start_time or start_time <= start) and (not end_time or end_time >= end):
                output.append((id, start, end, text))
        self.contents = output

    @property
    def content(self):
        output = ""
        for (id, start, end, text) in self.contents:
            output += row_format % locals()
        return output
