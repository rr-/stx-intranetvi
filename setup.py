from setuptools import find_packages, setup

setup(
    name="intranetvi",
    version="0.1.0",
    description="editing stxnext intranet timesheets with vim",
    author="Marcin Kurczewski",
    author_email="rr-@sakuya.pl",
    url="https://github.com/rr-/intranetvi",
    packages=find_packages(),
    install_requires=["requests", "configargparse", "python-dateutil", "pytimeparse"],
    entry_points={"console_scripts": ["intranetvi = intranetvi.__main__:main"]},
)
