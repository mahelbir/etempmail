import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

pkg_name = "etempmail"
setuptools.setup(
    name=pkg_name,
    version="2.0.0.0",
    author="Mahmuthan Elbir",
    author_email="me@mahmuthanelbir.com.tr",
    description="A simple Python module to get free disposable temporary email address",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['temp mail', 'temporary mail', 'disposable mail', 'temp email', 'etempmail', 'etempmail.com'],
    license="MIT",
    url="https://github.com/mahelbir/etempmail",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=[pkg_name],
    include_package_data=True,
    install_requires=[
        "requests~=2.28.1"
    ],
    python_requires=">=3.6"
)
