#!/usr/bin/env python3
"""
Filtered Logger Module
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscate specified fields in the log message.

    Args:
        fields (List[str]): List of fields to obfuscate.
        redaction (str): String to replace obfuscated fields with.
        message (str): The log message to process.
        separator (str): The character separating fields in the log message.

    Returns:
        str: The log message with specified fields obfuscated.
    """
    pattern = re.compile(fr'(?<={separator})(' + '|'.join(fields) + r')=[^;]+')
    return pattern.sub(f'{separator}\\1={redaction}', message)

# Example usage
if __name__ == "__main__":
    fields = ["password", "date_of_birth"]
    messages = [
        "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
        "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;",
    ]

    for message in messages:
        print(filter_datum(fields, 'xxx', message, ';'))
