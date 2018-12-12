#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess


class TestEcho(unittest.TestCase):

    def setUp(self):
        self.parser = echo.create_parser()

    def test_help(self):
        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        self.assertEquals(stdout, usage)

    def test_upper_short(self):
        arg_list = ["-u", "hello"]
        namespace = self.parser.parse_args(arg_list)
        # W as the '-u' attr
        self.assertTrue(namespace.upper)
        # Did the program transform our text to uppercase?
        self.assertEquals(echo.main(arg_list), "HELLO")

    def test_upper_long(self):
        arg_list = ["--upper", "hello"]
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.upper)
        self.assertEquals(echo.main(arg_list), "HELLO")

    def test_lower_short(self):
        arg_list = ["-l", "HELLO"]
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.lower)
        self.assertEquals(echo.main(arg_list), 'hello')

    def test_lower_long(self):
        arg_list = ["--lower", "HELLO"]
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.lower)
        self.assertEquals(echo.main(arg_list), 'hello')

    def test_title_short(self):
        arg_list = ["-t", "hello"]
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.title)
        self.assertEquals(echo.main(arg_list), 'Hello')

    def test_title_long(self):
        arg_list = ["--title", "hello"]
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(namespace.title)
        self.assertEquals(echo.main(arg_list), 'Hello')

    def test_all_options(self):
        arg_list = ["-tul", 'hElLo']
        namespace = self.parser.parse_args(arg_list)
        self.assertTrue(all([namespace.lower,
                             namespace.upper, namespace.title]))
        self.assertEquals(echo.main(arg_list), 'Hello')


if __name__ == '__main__':
    unittest.main()
