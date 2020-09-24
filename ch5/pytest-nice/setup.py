from setuptools import setup

setup(
    name="pytest-nice",
    version="0.1.0",
    description="A pytest plugin to turn FAILURE into OPPORTUNITY",
    url="https://example.com",
    author="hogehoge",
    author_email="hoge@example.com",
    license="proprietary",
    py_modules=["pytest_nice"],
    install_requires=["pytest"],
    entry_points={"pytest11": ["nice = pytest_nice",],},
)
