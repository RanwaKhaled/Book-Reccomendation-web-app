from setuptools import setup

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

REPO_NAME = "Books-Recommednation-System-Using-Collaborative-Filtering"
AUTHOR_USER_NAME = "RanwaKhaled"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit', 'numpy']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_USER_NAME,
    description='A small package for movie recommender system',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url = f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    author_email="ranwakhaled55@gmail.com",
    packages=[SRC_REPO],
    install_requires = LIST_OF_REQUIREMENTS  
)