# iban_validator.py

iban_lengths = {
    "PK": 92,  #Pakistan
    "DE": 22,  # Germany
    "FR": 27,  # France
    "GB": 22,  # United Kingdom
    "PK": 24,  # Pakistan
    "ES": 24,  # Spain
    "IT": 27,  # Italy
    "NL": 18,  # Netherlands
    "BE": 16,  # Belgium
    # (you can add more later)
}

def validate_iban(iban: str) -> str:
    """
    Validate an IBAN (International Bank Account Number).
    Returns a message about validity.
    """
    iban = iban.replace(' ', '').replace('-', '')   # remove spaces & dashes

    if not iban.isalnum():
        return "Invalid characters found."

    if len(iban) < 15:
        return "IBAN is too short."
    elif len(iban) > 31:
        return "IBAN is too long."

    # Country code check
    country_code = iban[:2].upper()
    if country_code in iban_lengths:
        expected = iban_lengths[country_code]
        if len(iban) != expected:
            return f"Invalid length for {country_code}. Expected {expected}, got {len(iban)}."
    else:
        return f"Unknown country code: {country_code}"

    # Rearrange & convert
    iban = (iban[4:] + iban[0:4].upper())
    iban2 = ''

    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))

    iban = int(iban2)

    if iban % 97 == 1:
        return f"IBAN is valid for {country_code}."
    else:
        return f"IBAN is invalid for {country_code}."

if __name__ == "__main__":
    user_iban = input("Enter IBAN: ")
    print(validate_iban(user_iban))
