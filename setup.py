from setuptools import setup, find_packages


setup(
    name="route-permission-manager",
    version="1.0.0",
    author="Ali Bahrampour",
    description="Bulk Route Permission Assignment Tool",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "route-permission-manager=src.main:main"
        ]
    },
)