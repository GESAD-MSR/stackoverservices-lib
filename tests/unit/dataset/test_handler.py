import xml.sax

from src.stackoverservices.dataset.xml.sos_handler import SOSHandler


def test_sos_handler(capsys, xml_input):
    """TODO: Docstring for test_model.

    :function: TODO
    :returns: TODO

    """

    handler = SOSHandler()

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    parser.setContentHandler(handler)
    parser.parse(xml_input)

    print(xml_input)
    captured = capsys.readouterr()
    assert (captured.out.strip() ==str(xml_input))
    # assert 1 is 1
