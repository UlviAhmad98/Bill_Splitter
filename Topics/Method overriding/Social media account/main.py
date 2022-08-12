class Account:
    def __init__(self, media, username, n_followers):
        self.media = media
        self.username = username
        self.n_followers = n_followers
        print("Account")


class InstagramAccount(Account):
    def __init__(self, username, n_followers, n_following):
        super().__init__(username=None, n_followers=None, media="Instagram")
        self.n_following = n_following
        self.username = username
        self.n_followers = n_followers
# create the class here