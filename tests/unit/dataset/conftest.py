import os
import pytest

from pathlib import Path


@pytest.fixture
def xml_input(test_root) -> str:
    """Fixture for configuring the input data for testing handlers


    :returns: The path to the xml test input.
    """

    #TODO: SET TEST PATHS IN A FIXTURE IN ROOT CONFTEST
    #TODO: TRY TO PASS FIXTURE TO ANOTHER FIXTURE


    # test_folder_path = os.path.abspath(".")

    # test_folder = Path(test_folder_path)

    # return test_folder / "resources/sample.xml"
    return test_root / "resources/sample.xml"


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
