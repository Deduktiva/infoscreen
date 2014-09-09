## Infoscreen Design Specification
### Conceptual Overview
An embedded system will be attached to a public display screen (TFT or LCD).
The embedded system dynamically serves HTML pages via X and a Browser.
The browser is automated using the Webdriver Framework [0]
implementation of Selenium [1].
New content MUST be pushed onto the device via `rsync(1)` using
the SSH protocol with pre-shared keys. Pulling content from a central
infrastructure onto the device is OPTIONAL and not intended nor to be
implemented in the current design.


### Content

Structure of the content directory:
```
config.csv
01.html
02.html
...
01.jpg
02.jpg
...
```

Only the filename `config.csv` is mandatory, all other filenames are
suggested to be named in ascending order, but this is NOT REQUIRED.

The presence or use of images is OPTIONAL.

It is suggested to use one image per HTML file, and the image SHOULD
match the configured display resolution.

#### Config
```
01.html;displaytime1
02.html;displaytime2
...
```

Each line in the `config.csv` specifies a filename that MUST be a
valid HTML file that will be displayed for a given time in seconds.

After all files have been displayed, the rotation starts again with
the first file.


#### Updating and removing active content on the device

The current assets are expected in the directory called `content/active`.
To replace the content, create a new folder `content/new` with the new content,
then touch a state file called `content/do-update`. When the update state file
is found by the infoscreen software, it SHALL, in the specified order:

1. pause the rotation,
2. recursively remove `content/old`,
3. rename `content/active` to `content/old`,
4. rename `content/new` to `content/active`,
5. unlink the `content/do-update` file,
6. recursively remove `content/old`,
7. restart the rotation by rereading the configuration file and starting at the first entry.


#### Considerations for central updates

The following section is OPTIONAL.

The server pushing the updates SHALL follow this procedure:

1. Copy `content/active` to `content/new` using hard links
2. Update `content/new` with the new content
3. Touch the file `content/do-update`


------
[0] - [W3C: WebDriver](http://www.w3.org/TR/webdriver)    
[1] - [Selenium2 - WebDriver](http://docs.seleniumhq.org/projects/webdriver)    
