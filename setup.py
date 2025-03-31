from setuptools import setup, find_packages

setup(
    name="edapro",
    version="0.1.0",
    license_file='LICENSE'
    description="A Python library for easy exploratory data analysis",
    author="aitechman",
    author_email="aitechman@gmail.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "seaborn",
        "matplotlib",
        "scipy",
        "statsmodels",
        "scikit-learn",
        "wordcloud",
        "ipython"
    ],
    python_requires=">=3.8",
)
