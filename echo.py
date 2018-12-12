#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "davidstewy"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    # Create and define your parser engine here, but DONT PARSE.
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument("text", help="text to be manipulated")
    parser.add_argument(
        "-u", "--upper", action="store_true", help="convert text to uppercase")
    parser.add_argument(
        "-l", "--lower", action="store_true", help="convert text to lowercase")
    parser.add_argument(
        "-t", "--title", action="store_true", help="convert text to titlecase")
    return parser


def main(args):
    parser = create_parser()
    namespace = parser.parse_args(args)
    text = namespace.text
    if namespace.upper:
        text = text.upper()
    if namespace.lower:
        text = text.lower()
    if namespace.title:
        text = text.title()
    return text


if __name__ == '__main__':
    print main(sys.argv[1:])
