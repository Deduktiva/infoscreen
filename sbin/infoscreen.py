#!/usr/bin/env python3
from selenium import webdriver
import os, time, zipfile

class Infoscreen:
    def __init__(self, defaultpage, sourcedir, destdir):
        self.defaultpage = defaultpage
        self.sourcedir   = sourcedir
        self.destdir     = destdir
        self.driver      = None

    def start(self):
        '''set up the webdriver environment'''

        # set the display
        os.environ['DISPLAY'] = ":0"

        # initialize Firefox via Webdriver
        self.driver = webdriver.Firefox()

        # display default page
        self.driver.get('file://' + self.defaultpage)

        # XXX(azet): maximize_window does not properly work

    def stop(self):
        self.driver.quit()

    def scan_for_incoming(self):
        '''scan the incoming folder for recently uploaded ZIP files'''
        files = []
        # XXX(azet): zipfile.is_zipfile(k) always returns False?
        [files.append(self.sourcedir + k) for k in os.listdir(self.sourcedir) if k.endswith('.zip')]
        return files

    def extract_zip_files(self):
        '''
        extracts zip files and places them into the active
        working directory for display in the browser. the
        extracted zip file is then deleted.
        '''
        for zips in self.scan_for_incoming():
            f = zipfile.ZipFile(zips)
            f.extractall(self.destdir)
            os.remove(zips)

    def display_time(self, directory):
        ''' returns the display time for a given directory '''
        try:
            with open(directory + '/time') as f:
                return int(f.read())
        except FileNotFoundError:
            return 150000

    def serve(self):
        ''' display the website content '''
        while True:
            self.extract_zip_files()

            for root, dirs, files in os.walk(self.destdir):
                if 'index.html' in files:
                    t = self.display_time(root)
                    self.driver.get('file://' + root + '/index.html')
                    time.sleep(t/1000)

