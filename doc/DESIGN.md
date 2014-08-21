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
#### Format
Content to be pushed onto devices SHALL be packaged and compressed as ZIP
format [1]. The implementation MUST support multiple ZIP files to be
pushed onto devices concurrently.

#### ZIP File Directory Structure
A ZIP file SHALL contain one (1) or more subdirectories in accending
number sequence (e.g. 01..99). Each subdirectory contains the
contents of one (1) website to be displayed. An example tree structure
might look like this:
```
contentupdate-2014-08-19.zip:
  /01
     index.html
     graphics/
              ad.jpeg
              header.jpeg
              [...]
     time
  /02
    index.html
    gif/
        ani01.gif
        ani02.gif
        [...]
    time
  [...]
```

#### Display Time
Each subdirectory contained in a ZIP file MUST contain a file `time`.
This file will be used to define display time periods (i.e. how low a
certain website will be displayed until rotation continues).

The `time` files only content is a duration specified in milliseconds.

An example may look like this:
```
  08/time:
    150000
```
(The only content of the file `time` in the subdirectory `08` is `150000`.
Which specifies two and a half minutes of display time)


[0] - [W3C: WebDriver](http://www.w3.org/TR/webdriver)    
[1] - [Selenium2 - WebDriver](http://docs.seleniumhq.org/projects/webdriver)    
[2] - [.ZIP File Format Specification](http://www.pkware.com/documents/casestudies/APPNOTE.TXT)    
