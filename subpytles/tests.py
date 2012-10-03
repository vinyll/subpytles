# -*- coding: utf-8 -*-

import unittest
import os

from editor import SrtEditor


filepath = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'subtitles.srt'))

class SrtEditorTest(unittest.TestCase):
    def setUp(self):
        content = file(filepath).read()
        self.editor = SrtEditor(content)

    def test_read_file(self):
        self.assertEqual(self.editor.content, "1\r\n00:01:34,680 --> 00:01:35,874\r\nTu veux un ballon ?\r\n\r\n3\r\n00:01:38,440 --> 00:01:39,793\r\n5 euros\r\n\r\n4\r\n00:01:41,680 --> 00:01:42,635\r\nLe re\xe7u ?\r\n\r\n")

    def test_delay(self):
        self.editor.delay(1000)
        self.assertEqual(self.editor.content, "1\r\n0:01:35,680 --> 0:01:36,874\r\nTu veux un ballon ?\r\n\r\n3\r\n0:01:39,440 --> 0:01:40,793\r\n5 euros\r\n\r\n4\r\n0:01:42,680 --> 0:01:43,635\r\nLe re\xe7u ?\r\n\r\n")


if __name__ == "__main__":
    unittest.main()
