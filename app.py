import streamlit as st
from iban_validator import validate_iban

st.title("IBAN Validator")

iban_list = st.text_area("Enter one or more IBANs (one per line):")
if st.button("Validate IBANs"):
    ibans = iban_list.strip().splitlines()
    results = []

    for ib in ibans:
        results.append({
            "IBAN": ib,
            "Result": validate_iban(ib)
        })

    st.write("### Validation Results")
    st.dataframe(results)
