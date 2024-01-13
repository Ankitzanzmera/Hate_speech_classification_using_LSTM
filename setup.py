from setuptools import setup, find_packages


project_name = "hate_speech_classification"

setup(
    name= project_name,
    version = "0.0.1",
    author= "Ankit Zanzmera",
    author_email = "22msrds052@jainuniversity.ac.in",
    url= "https://github.com/Ankitzanzmera/Hate_speech_classification_using_LSTM",
    packages= find_packages(where="src"),
    package_dir = {"":"src"}
)