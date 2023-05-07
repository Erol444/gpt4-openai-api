from setuptools import setup

setup(
    name="gpt4-openai-api",
    version="1.0.0",
    description="",
    author="Erol444",
    author_email="erol123444@gmail.com",
    url="https://github.com/Erol444/gpt4-openai-api",
    packages=["gpt4_openai"],
    install_requires=[
        "undetected-chromedriver>=3.4.6",
        "markdownify>=0.11.6",
        "langchain",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10"
    ],
    python_requires=">=3.6",
)
