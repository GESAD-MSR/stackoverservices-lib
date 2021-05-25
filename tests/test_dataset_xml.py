import xml.sax
#  import os

from src.stackoverservices.dataset.xml.sos_handler import SOSHandler


def test_sos_handler(capsys):
    #  current_dir = os.path.abspath('.')
    #  test_file = current_dir + "/sample.xml"
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
         "stackoverservices-lib/tests/sample.xml")
    )

    #  print(type(test_file))

    captured = capsys.readouterr()
    assert (captured.out == "posts\n" or captured.out == "row\n")
