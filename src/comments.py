"""define the comments model"""
from users import get_user

class Comments():
    """define and configure the comments model"""

    def __init__(self, author, created_at, comment_id, content):
        self.author = author
        self.created_at = created_at
        self.comment_id = comment_id
        self.content = content
        self.comments = []

    def delete_comment(self, author, comment_id):
        role = get_user(author)['role']
        if role == 'admin' or role == 'moderator':
            for comment in self.comments:
                id = comment.get('id')
                if id == comment_id:
                    self.comments.remove(comment)
        elif author == self.author:
            for comment in self.comments:
                id = comment.get('id')
                if id == comment_id:
                    self.comments.remove(comment)
        else:
            return 'you are not authorized to perform this task'
