#!/usr/bin/env python3

from infoscreen import Infoscreen

def main():
    nfoscr = Infoscreen(
                defaultpage='/opt/infoscreen/content/active/blank.html',
                sourcedir='/opt/infoscreen/content/new/',
                destdir='/opt/infoscreen/content/active/'
             )
             
    try:
        nfoscr.start()
        nfoscr.serve()
    finally:
        nfoscr.stop()

if __name__ == '__main__':
    main()
