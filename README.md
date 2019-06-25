# gsearch.py
This tiny module allows access to some Google Search features which may not be easily accessible using the official Google APIs. Only the beautifulsoup4 and requests modules are required.
Please note that Google may change how the Google Search websites work at any moment, or even ban those who are overusing/abusing their features, which this module will happily allow one to do. Use this module carefully at your own risk.
## Documentation
### Google Search
#### `gsearch.get_autocomplete_entry(query : str)`
*returns a list of strings, or None*
Takes a query and returns Google's autocompletes.
### Google Images
#### `gsearch.reverse_gimage(imagelink : str)`
*returns string*
Takes the link to an image and returns what Google thinks the image is.
#### `gsearch.reverse_gimage_link(imagelink : str)`
*returns string*
Takes the link to an image and returns a link to a Google Search of that image.
### Exceptions
#### `gsearch.Error(Exception)`
This is the base class for exceptions in the gsearch module.
#### `gsearch.NetworkError(Error)`
This exception is raised when the data gsearch is trying to access on the Internet can't be reached.
#### `gsearch.DecodeError(Error)`
This exception is raised when gsearch doesn't understand the data it got from the Internet. This may indicate that Google has blocked or ratelimited due to overuse/abuse. This can sometimes be fixed by accessing a Google webpage, upon which Google will try to see if you're a robot, and you can lie through your teeth. This error could also indicate that the webpage structure has changed and the module doesn't know what to do. If updating gsearch doesn't fix this problem, see if there is an issue is open, and if not, submit your own.
