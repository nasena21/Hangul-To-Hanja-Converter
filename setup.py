from setuptools import setup, find_packages

__version__ = "0.1"

setup(
    name="hanja-tagger",
    version=__version__,
    license="MIT",
    description="Online Hanja tagger (powered by Hanjaro)",
    author="Kang Min Yoo",
    author_email="kaniblurous@gmail.com",
    url="https://github.com/kaniblu/hanja-tagger",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="Hanja, Tagger, Natural Language Processing",
    entry_points={
        'console_scripts': [
            'hangul-to-hanja=Hangul_To_Hanja.my_script:main',  # Update based on your script
        ],
    },
    package_data={
        '': ['Hangul_To_Hanja/*.bat'],  # Include .bat files in the package
    },
)
