# -*- coding: utf-8 -*-

import unittest
import os
import copy
from io import open

from editor import SrtEditor


filepath = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'subtitles.srt'))

content = "1\r\n00:01:34,680 --> 00:01:35,874\r\nTu veux un ballon ?\r\n\r\n2\r\n00:01:36,080 --> 00:01:38,036\r\n- Maman, tu me l'achètes ?\r\n\r\n3\r\n0:01:38,440 --> 0:01:42,793\r\n5 euros\r\n\r\n"

class SrtEditorTest(unittest.TestCase):
    def setUp(self):
        content = open(filepath, encoding='iso-8859-1').read()
        self.editor = SrtEditor(content)

    def test_read_file(self):
        self.assertEqual(self.editor.content, content)

    def test_delay(self):
        editor = copy.deepcopy(self.editor)
        editor.delay(1000)
        self.assertEqual(editor.content, "1\r\n0:01:35,680 --> 0:01:36,874\r\nTu veux un ballon ?\r\n\r\n2\r\n0:01:37,080 --> 0:01:39,036\r\n- Maman, tu me l'achètes ?\r\n\r\n3\r\n0:01:39,440 --> 0:01:43,793\r\n5 euros\r\n\r\n")
        editor = copy.deepcopy(self.editor)
        editor.delay(-1000)
        self.assertEqual(editor.content, "1\r\n0:01:33,680 --> 0:01:34,874\r\nTu veux un ballon ?\r\n\r\n2\r\n0:01:35,080 --> 0:01:37,036\r\n- Maman, tu me l'achètes ?\r\n\r\n3\r\n0:01:37,440 --> 0:01:41,793\r\n5 euros\r\n\r\n")

    def test_slice(self):
        editor = copy.deepcopy(self.editor)
        editor.slice("0:01:38")
        self.assertEqual(editor.content, "3\r\n0:01:38,440 --> 0:01:42,793\r\n5 euros\r\n\r\n")
        editor = copy.deepcopy(self.editor)
        editor.slice(end_time="0:01:38")
        self.assertEqual(editor.content, "1\r\n00:01:34,680 --> 00:01:35,874\r\nTu veux un ballon ?\r\n\r\n2\r\n00:01:36,080 --> 00:01:38,036\r\n- Maman, tu me l'achètes ?\r\n\r\n")

if __name__ == "__main__":
    unittest.main()
