#!/usr/bin/env python3
""" Module for logging messages"""
import logging
import re
from typing import List
import os
import mysql.connector


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


# Personally Identifiable Information
PII_FIELDS = ('name', 'phone', 'ssn', 'password', 'ip')


def get_logger() -> logging.Logger:
    """CReates Logger"""
    # initialize logger as user_data
    logger = logging.getLogger('user_data')
    # set logging level
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # set stream handler to display message
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))

    # add stream to logger user_data
    logger.addHandler(stream_handler)

    return logger


# Connect to secure database
def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to the database"""

    name = os.getenv("PERSONAL_DATA_DB_NAME")
    username = os.getenv("PERSONAL_DATA_DB_USERNAME")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD")
    host = os.getenv("PERSONAL_DATA_DB_HOST")

    db = mysql.connector.connect(
        database=name if name else 'my_db',
        host=host if host else 'localhost',
        user=username if username else 'root',
        password=password if password else 'root'
    )

    return db
