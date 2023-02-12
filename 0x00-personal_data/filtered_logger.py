#!/usr/bin/env python3
""" Module for logging messages"""
import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Returns the log message obfuscated """
    holder = message
    for field in fields:
        holder = re.sub(field + "=.*?" + separator,
                        field + "=" + redaction + separator, holder)
    return holder
