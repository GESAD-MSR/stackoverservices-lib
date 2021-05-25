#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This module presents a class for handling stackoverflow XML dataset

"""


# ============================= IMPORT SECTION ============================= #


# Standart libs
#
import xml.sax
from xml.sax import ContentHandler
#  from xml.parsers.expat import ExpatError
#  from xml.sax._exceptions import SAXParseException

# External libs
#

# Local libs
#


__author__ = "Alan Bandeira"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Alan Bandeira"
__email__ = "alan.p.bandeira@gmail.com"
__status__ = "Development"


# ============================== CODE SECTION ============================== #


class SOSHandler(ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.id = None
        self.parent_id = None
        self.title = ""
        self.tags = []
        self.body = ""
        self.comment_count = None
        self.view_count = None
        self.answer_count = None
        self.favorite_count = None
        self.score = None

    def startElement(self, tag, attributes):
        print(str(dict(attributes)))

    def endElement(self, tag):
        pass

    def characters(self, content):
        pass
        #  try:
        #      print(content)
        #  except ExpatError:
        #      print('aaaahhhhhh', content)

    def endDocument(self):
        pass


if __name__ == "__main__":

    handler = SOSHandler()

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    parser.setContentHandler(handler)

    #  parser.parse(
    #      ("/mnt/c/Users/alanp/Devspace/GESAD/"
    #       "stackoverservices-lib/tests/data-mock.xml")
    #  )
    #  parser.parse(test_file)
    parser.parse(
        ("/mnt/c/Users/alanp/Devspace/GESAD/"
         "stackoverservices-lib/tests/data-mock.xml")
    )
