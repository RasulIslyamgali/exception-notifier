from setuptools import find_packages, setup

project_urls = {
    'Homepage': 'https://github.com/RasulIslyamgali/exception-notifier',
}

with open('Readme.md') as f:
    long_description = f.read()


setup(
    name='pyexception-notifier',
    packages=find_packages(),
    version='0.0.3',
    description='Exception notifier',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='r.islyamgali',
    license='MIT',
    install_requires=[
        "pydantic",
        "uvicorn",
        "requests(>=2.27,<3.0)",
        "python-dotenv",
        "gunicorn[standard]",
    ],
    python_requires=">=3.8"
)
