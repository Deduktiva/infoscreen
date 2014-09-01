#!/usr/bin/env python3

from infoscreen import Infoscreen

def main():
    nfoscr = Infoscreen(
                defaultpage='/home/azet/dev/infoscreen/content/active/blank.html',
                sourcedir='/home/azet/dev/infoscreen/content/new/',
                destdir='/home/azet/dev/infoscreen/content/active/'

             )
    try:
        nfoscr.start()
        nfoscr.serve()
    finally:
        nfoscr.stop()

if __name__ == '__main__':
    main()
