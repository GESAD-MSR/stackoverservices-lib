from src.stackoverservices.models.post_model import PostModel


def test_model_for_question_post(so_post):
    """TODO: Docstring for test_model.

    :function: TODO
    :returns: TODO

    """

    post = PostModel(**so_post)
    assert post != {}
