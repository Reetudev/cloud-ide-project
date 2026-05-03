import streamlit as st
import subprocess
import os

st.title("Cloud IDE")

code = st.text_area("Enter your Python code:", height=300)

if st.button("Run Code"):
    try:
        with open("temp.py", "w") as f:
            f.write(code)

        result = subprocess.getoutput("python3 temp.py")
        st.text_area("Output:", result, height=200)

        os.remove("temp.py")

    except Exception as e:
        st.error(str(e))
