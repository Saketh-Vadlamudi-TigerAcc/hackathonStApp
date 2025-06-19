'''import streamlit as st

st.set_page_config(layout="wide")
st.title("Hello from Streamlit on Databricks!")
st.write("This is a basic Streamlit app deployed via Databricks Apps.")

name = st.text_input("What's your name?", "World")
st.write(f"Hello, {name}!")

if st.button("Click Me!"):
    st.write("You clicked the button!") '''
import os
os.environ["PYSPARK_USE_SPARK_CONNECT"] = "0"  # Disable Spark Connect before importing PySpark

from pyspark.sql import SparkSession
# /editor/files/779215961203655?o=1806740992728685
# spark = SparkSession.builder.getOrCreate()
spark = SparkSession.builder.remote("sc://adb-1806740992728685.5.azuredatabricks.net:443").getOrCreate()

df = spark.range(10)
df.show()
