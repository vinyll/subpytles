# -*- coding: utf-8 -*-

import re
from datetime import timedelta


row_format = "%(id)s\r\n%(start)s --> %(end)s\r\n%(text)s\r\n\r\n"

class SrtEditor(object):

    def __init__(self, content, *args, **kwargs):
        time_format="\d+:\d+:\d+,\d+"
        rows = re.findall(
            r'(\d+)\r\n(%(time_format)s) --> (%(time_format)s)\r\n(.+)\r\n\r\n' % locals(),
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
            start = str(start_time + timedelta(milliseconds=time)).replace('.', ',')[:-3]
            t = re.findall(time_pattern, end)[0]
            end_time = timedelta(hours=int(t[0]), minutes=int(t[1]), seconds=int(t[2]), milliseconds=int(t[3]))
            end = str(end_time + timedelta(milliseconds=time)).replace('.', ',')[:-3]
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
