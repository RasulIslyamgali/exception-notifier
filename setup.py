from setuptools import find_packages, setup

setup(
    name='exception-notifier',
    packages=find_packages(),
    version='0.0.1',
    description='Exception notifier',
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
