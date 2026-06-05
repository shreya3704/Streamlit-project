import streamlit as st
import pandas as pd

st.title("CSV Transformation Tool")

# Upload File
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Preview")
    st.dataframe(df.head(100))

    st.subheader("Column Mapping")

    amount_col = st.selectbox("Select Amount Column", df.columns)
    date_col = st.selectbox("Select Date Column", df.columns)

    # Validation
    st.subheader("Validation")

    invalid_amounts = pd.to_numeric(
        df[amount_col],
        errors="coerce"
    ).isna().sum()

    if invalid_amounts > 0:
        st.error(f"{invalid_amounts} invalid amount values found")
    else:
        st.success("Amount column is valid")

    try:
        pd.to_datetime(df[date_col])
        st.success("Date column is valid")
    except:
        st.error("Invalid date format")

    # Transformations
    st.subheader("Transformations")

    remove_duplicates = st.checkbox("Remove Duplicates")

    fill_nulls = st.checkbox("Fill Null Values")

    fill_value = st.text_input(
        "Fill Value",
        "0"
    )

    multiplier = st.number_input(
        "Tax Multiplier",
        value=1.18
    )

    if st.button("Apply Transformations"):

        new_df = df.copy()

        if remove_duplicates:
            new_df = new_df.drop_duplicates()

        if fill_nulls:
            new_df = new_df.fillna(fill_value)

        new_df["Adjusted_Amount"] = (
            pd.to_numeric(
                new_df[amount_col],
                errors="coerce"
            ) * multiplier
        )

        st.success("Transformation Complete")

        st.dataframe(new_df.head())

        csv = new_df.to_csv(index=False)

        st.download_button(
            "Download CSV",
            csv,
            "processed_file.csv",
            "text/csv"
        )