import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name='googlesearch',  
	version='0.1.0',
	scripts=['googlesearch'] ,
	author="sithsiri",
	description="allows access to some Google Search features which may not be easily accessible using the official Google APIs",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/sithsiri/googlesearch.py",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
 )