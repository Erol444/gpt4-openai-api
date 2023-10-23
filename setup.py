from setuptools import setup
from pathlib import Path

root = Path(__file__).parent.resolve()
readme_file = root / 'readme.md'
long_description = readme_file.read_text(encoding='utf-8')

setup(
    name="gpt4-openai-api",
    version="0.8.1",
    description="Python package for unofficial GPT-4 API access via chat.openai.com using Chrome browser via Selenium",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Erol444",
    author_email="erol123444@gmail.com",
    url="https://github.com/Erol444/gpt4-openai-api",
    packages=["gpt4_openai"],
    install_requires=[
        "undetected-chromedriver>=3.5.3",
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
