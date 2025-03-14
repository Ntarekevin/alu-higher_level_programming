#!/usr/bin/python3

"""Module that defines the read_file function."""


def read_file(filename=""):
    """Read a UTF-8 encoded file and print its contents."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
