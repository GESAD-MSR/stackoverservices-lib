#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This module presents a class for handling stackoverflow XML dataset

"""


# ============================= IMPORT SECTION ============================= #


# Standart libs
#
import xml.sax
#  import pprint as printer

from xml.sax.handler import ContentHandler

# External libs
#
from pandas import DataFrame

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
    # def __init__(self, output_file: str):
    def __init__(self):
        self.posts_count = 0
        self.header = True
        self.posts = DataFrame()
        # self.output_file = output_file

    def startElement(self, tag: str, attributes: dict):
        """docstring"""

        if attributes:
            new_post = dict(attributes)
            self.posts = self.posts.append(new_post, ignore_index=True)
            self.posts_count += 1

            if self.posts_count % 10 == 0:
                if self.header:
                    self.posts.columns = list(attributes.keys())
                # self.write_posts_chunk()
                self.header = False

    # def write_posts_chunk(self):
    #     """docstring"""
    #     self.posts.to_csv(
    #         self.output_file,
    #         header=self.header,
    #         mode='a'
    #     )


if __name__ == "__main__":
    # TODO Test with SO sample

    handler = SOSHandler('')

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
         "stackoverservices-lib/tests/so-sample.xml")
    )
