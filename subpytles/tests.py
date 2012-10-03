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
        self.assertEqual(self.editor.content, "1\r\n00:01:34,680 --> 00:01:35,874\r\nTu veux un ballon ?\r\n\r\n2\r\n00:01:36,080 --> 00:01:38,036\r\n- Maman, tu me l'ach\xe8tes ?\r\n\r\n")

    def test_delay(self):
        self.editor.delay(1000)
        self.assertEqual(self.editor.content, "1\r\n0:01:35,680 --> 0:01:36,874\r\nTu veux un ballon ?\r\n\r\n2\r\n0:01:37,080 --> 0:01:39,036\r\n- Maman, tu me l'ach\xe8tes ?\r\n\r\n")
        self.editor.delay(-1000)
        self.assertEqual(self.editor.content, "1\r\n0:01:34,680 --> 0:01:35,874\r\nTu veux un ballon ?\r\n\r\n2\r\n0:01:36,080 --> 0:01:38,036\r\n- Maman, tu me l'ach\xe8tes ?\r\n\r\n")

if __name__ == "__main__":
    unittest.main()
