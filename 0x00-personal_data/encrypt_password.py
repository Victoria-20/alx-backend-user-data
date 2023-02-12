#!/usr/bin/env python3
"""Encrypting passwords"""
import bcrypt


def hash_password(password):
    """returns a salted, hashed password, which is a byte string."""
    # Hash a password for the first time, with a randomly-generated salt
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    return hashed
