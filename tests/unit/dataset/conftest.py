import pytest


@pytest.fixture
def xml_input() -> str:
    """Fixture for configuring the input data for testing handlers


    :returns: The path to the xml test input.
    """

    return ("/mnt/c/Users/alanp/Devspace/GESAD/stackoverservices-lib/tests/"
            "resources/sample.xml")


@pytest.fixture
def so_post():
    """Fixture with dict data for easy input manipulation

    :returns: A dict with data to simulate a StackOverflow Post
    """

    return {
        "Id": 1,
        "PostTypeId": 1,
        'AcceptedAnswerId': 1,
        'ParentId': 1,
        "CreationDate": "2008-08-01T00:42:38.903",
        'DeletionDate': "2008-08-01T00:42:38.903",
        'Score': 1,
        'ViewCount': 1,
        'Body': '',
        'OwnerUserId': 1,
        'OwnerDisplayName': 'Alan',
        'LastEditorUserId': 1,
        'LastEditorDisplayName': 'Alan',
        'LastEditDate': "2008-08-01T00:42:38.903",
        'LastActivityDate': "2008-08-01T00:42:38.903",
        'Title': 'A post',
        'Tags': '<python><microservices>',
        'AnswerCount': 1,
        'CommentCount': 1,
        'FavoriteCount': 1,
        'ClosedDate': None,
        'CommunityOwnedDate': None
    }
