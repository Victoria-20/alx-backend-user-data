#!/usr/bin/env python3
""" 4. Hash password"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """returns a salted, hashed password, which is a byte string"""

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
