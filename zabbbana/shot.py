class Shot():

    def __init__(self, client, shot_id):
        self.client  = client
        self.shot_id = shot_id

    def list_attachments(self, shot_id=None):

        """
            List attachments for a shot
            http://developer.dribbble.com/v1/shots/attachments/#list-attachments-for-a-shot
        """

        shot_id             = shot_id if shot_id is not None else self.shot_id
        attachments         = self.client.get("/shots/{}/attachments".format(shot_id))
        return attachments.json()

    def get_attachment(self, attachment_id, shot_id=None):

        """
            get a single attachment for shot
            http://developer.dribbble.com/v1/shots/attachments/#get-a-single-attachment
        """
        shot_id             = shot_id if shot_id is not None else self.shot_id
        attachment          = self.client.get("/shots/{}/attachments/{}".format(shot_id, attachment_id))
        return attachment.json()

    def list_buckets(self, shot_id=None):

        """
            List all buckets a shot is part of
            http://developer.dribbble.com/v1/shots/buckets/
        """

        shot_id             = shot_id if shot_id is not None else self.shot_id
        buckets             = self.client.get("/shots/{}/buckets".format(shot_id))
        return buckets.json()

    def list_comments(self, shot_id=None):
        """
            List all the comments for a shot
            http://developer.dribbble.com/v1/shots/comments/#list-comments-for-a-shot
        """
        shot_id             = shot_id if shot_id is not None else self.shot_id
        comments            = self.client.get("/shots/{}/comments".format(shot_id))
        return comments.json()

    def list_comment_likes(self, comment_id, shot_id=None):

        """
            List all likes for a single comment in a single shot
            http://developer.dribbble.com/v1/shots/comments/#list-likes-for-a-comment
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        comment_likes           = self.client.get("/shots/{}/comments/{}/likes".format(shot_id, comment_id))
        return comment_likes.json()

    def get_comment(self, comment_id, shot_id=None):

        """
            Get a single comment for a single shot
            http://developer.dribbble.com/v1/shots/comments/#get-a-single-comment
        """
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        comment                 = self.client.get("/shots/{}/comments/{}".format(shot_id, comment_id))
        return comment.json()

    def check_user_likes_comment(self, comment_id, shot_id=None):

        """
            Check if the authenticated user likes a comment
            http://developer.dribbble.com/v1/shots/comments/#check-if-you-like-a-comment
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        result                  = self.client.get("/shots/{}/comments/{}/like".format(shot_id, comment_id))
        return result

    def like_comment(self, comment_id, shot_id=None):


        """
            Add like to a single comment
            http://developer.dribbble.com/v1/shots/comments/#like-a-comment
        """
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        like                    = self.client.post("/shots/{}/comments/{}/like".format(shot_id, comment_id))
        return like.json()

    def unlike_comment(self, comment_id, shot_id=None):

        """
            Unlikes a previously liked comment
            http://developer.dribbble.com/v1/shots/comments/#unlike-a-comment
        """
        shot_id                 = shot_id if shot_id is not None else self.shot_id
        unlike                  = self.client.delete("/shots/{}/comments/{}/like".format(shot_id, comment_id))
        return unlike

    def list_likes(self, shot_id=None):

        """
            List all the likes for a shot
            http://developer.dribbble.com/v1/shots/likes/#list-the-likes-for-a-shot
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        shot_likes              = self.client.get("/shots/{}/likes".format(shot_id))
        return shot_likes.json()

    def like(self, shot_id=None):

        """
            Like a single shot
            http://developer.dribbble.com/v1/shots/likes/#like-a-shot
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        like                    = self.client.post("/shots/{}/like".format(shot_id))
        return like.json()

    def unlike(self, shot_id=None):

        """
            Unlike a single shot
            http://developer.dribbble.com/v1/shots/likes/#unlike-a-shot
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        unlike                  = self.client.delete("/shots/{}/like".format(shot_id))
        return unlike

    def list_projects(self, shot_id=None):

        """
            List all the projects for a shot
            http://developer.dribbble.com/v1/shots/projects/#list-projects-for-a-shot
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        projects                = self.client.get("/shots/{}/projects".format(shot_id))
        return projects.json()

    def list_rebounds(self, shot_id=None):

        """
            List all the rebounds for a shot
            http://developer.dribbble.com/v1/shots/rebounds/
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        projects                = self.client.get("/shots/{}/rebounds".format(shot_id))
        return projects.json()

    def check_user_likes_shot(self, shot_id=None):

        """
            Checks if the authenticated user likes a single shot
            http://developer.dribbble.com/v1/shots/likes/#check-if-you-like-a-shot
        """

        shot_id                 = shot_id if shot_id is not None else self.shot_id
        like_shot               = self.client.get("/shots/{}/like".format(shot_id))
        return like_shot
