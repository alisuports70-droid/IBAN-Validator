# test_iban.py
import pytest
from iban_validator import validate_iban



def test_valid_iban_pakistan():
    iban = "PK36SCBL0000001123456702"
    assert validate_iban(iban) == "IBAN is valid for PK."


def test_valid_iban_germany():
    iban = "DE44500105175407324931"
    assert validate_iban(iban) == "IBAN is valid for DE."

def test_valid_iban_uk():
    iban = "GB82WEST12345698765432"
    assert validate_iban(iban) == "IBAN is valid for GB."

def test_invalid_length():
    iban = "DE4450010517540732493"  # too short
    result = validate_iban(iban)
    assert "Invalid length for DE" in result

def test_invalid_chars():
    iban = "DE44$00105175407324931"
    assert validate_iban(iban) == "Invalid characters found."

def test_unknown_country():
    iban = "ZZ44500105175407324931"
    assert validate_iban(iban) == "Unknown country code: ZZ"

def test_invalid_checksum():
    iban = "DE44500105175407324932"  # one digit changed
    assert validate_iban(iban) == "IBAN is invalid for DE."

