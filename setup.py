from setuptools import find_packages, setup

with open("README.md", "r+") as fh:
    long_description = fh.read()

setup(
        name='S17',
        package_dir={'': 'src'},
        version='1.0.0',
        long_description=long_description,
        long_description_content_type="text/markdown",
        description='The S17 framework',
        url='git@github.com:bblue/bblue-SDK.git',
        author='Aleksander Lanes',
        author_email='aleksander.lanes@gmail.com',
        license='unlicensed',
        packages=find_packages(where='src'),
        zip_safe=False,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python :: 3.9',
            'Environment :: X11 Applications :: Qt',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'License :: Other/Proprietary License',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        install_requires=[
            'bblue-SDK @ git+ssh://git@github.com/bblue/bblue-SDK.git',
        ],
)
