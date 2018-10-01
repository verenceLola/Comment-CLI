"""define the comments model"""
from datetime import datetime
from users import get_user


class Comments():
    """define and configure the comments model"""

    def __init__(self, author, created_at, comment_id, content):
        self.author = author
        self.created_at = created_at
        self.comment_id = comment_id
        self.content = content
        self.comments = []  # comment item

    def add_comment(self, author, content):
        if len(author) == 0 or author.isspace():  
            return "Empty author"
        elif len(content) == 0 or content.isspace():
            return "Empty comment content"
        role = get_user(author)['role']
        if role == 'Admin':
            return "Admin cannot add comment"
        self.author = author
        self.content = content
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.comment_id = len(self.comments) + 1
        self.comments.append(
            {
                "author": self.author,
                "created_at": self.created_at,
                "content": self.content,
                "comment_id": self.comment_id
            }
        )
        return "Comment Added Successfully"