from setuptools import find_packages,setup

setup(
    name="MCQGenerator",
    version="0.0.1",
    author="AnandKumar Sivalanka",
    author_email="anandkumrs016@gmail.com",
    install_requires=["openai","langchain","langchain_community","python-dotenv","PyPDF2"],
    packages=find_packages(),
    
)