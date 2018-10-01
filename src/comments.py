"""define the comments model"""


class Comments():
    """define and configure the comments model"""

    comments = []  # comments list
    def __init__(self, author, created_at, comment_id, content):
        self.author = author
        self.created_at = created_at
        self.comment_id = comment_id
        self.content = content
        self.comment = {}  # comment item
