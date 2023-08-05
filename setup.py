import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "ANN-implementation"
USER_NAME = "sureshs96"

setuptools.setup(
    name=f"src",
    version="0.0.1",
    author=USER_NAME,
    author_email="sunny.c17hawke@gmail.com",
    description="its an ANN implimentation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "pandas",
        "tensorflow",
        "matplotlib",
        "seaborn"
    ]
)