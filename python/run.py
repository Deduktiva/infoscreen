#!/usr/bin/env python3

from infoscreen import Infoscreen

def main():
    nfoscr = Infoscreen(
                defaultpage='/home/azet/dev/infoscreen/content/active/blank.html',
                sourcedir='/home/azet/dev/infoscreen/content/new',
                destdir='/home/azet/dev/infoscreen/content/active'
             )

    nfoscr.start()
    nfoscr.serve_content()

if __name__ == '__main__':
    main()
