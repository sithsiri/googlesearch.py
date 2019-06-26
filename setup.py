import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name='googlesearch',  
	version='0.1.0',
	author="sithsiri",
	description="allows access to some Google Search features which may not be easily accessible using the official Google APIs",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/sithsiri/googlesearch.py",
	py_modules=['googlesearch'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent",
	],
 )