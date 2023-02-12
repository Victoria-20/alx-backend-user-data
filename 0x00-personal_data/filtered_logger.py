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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """initialize attributes"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filters values in incoming log records using filter_datum"""
        log = super().format(record)
        return filter_datum(self.fields, self.REDACTION, log, self.SEPARATOR)
