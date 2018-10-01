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

    def delete_comment(self, author, comment_id):
        role = get_user(author)['role']
        if role == 'admin' or role == 'moderator':
            for comment in self.comments:
                id = comment.get('id')
                if id == comment_id:
                    self.comments.remove(comment)
        else:
            return 'you are not authorized to perform this task'

    def admin_edit_comment(self, author, edited_at, comment_id, content):

    		for comment in comments:
    			if comment['comment_id']==comment_id:
    				if comment['author'] !='admin':
    					comment['content'] == content
  						return self.comments
  					return "Unauthirised"
    			return "Couldn't find comment id"

    def other_user_edit(self, author, edited_at, comment_id, content):

    		for comment in comments:
    			if comment['comment_id']==comment_id:
    					comment['content'] == content
  						return self.comments
    			return "Couldn't find comment id"
