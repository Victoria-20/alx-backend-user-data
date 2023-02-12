#!/usr/bin/env python3
""" Module for logging messages"""
import logging
import re


def filter_datum(fields: list[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns the log message obfuscated
        uses re.sub to perform the substitution with a single regex."""
    holder = message
    for field in fields:
        holder = re.sub(field + "=.*?" + separator,
                        field + "=" + redaction + separator, holder)
    return holder
