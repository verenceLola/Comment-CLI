"""define the comments model"""


class Comments():
    """define and configure the comments model"""

    def __init__(self, author, created_at, comment_id, content):
        self.author = author
        self.created_at = created_at
        self.comment_id = comment_id
        self.content = content
        self.comment = []  # comment item

    def admin_edit_comment(self, author, edited_at, comment_id, content):

    		for comment in self.comments:
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



