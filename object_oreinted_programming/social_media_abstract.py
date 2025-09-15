
from abc import ABC,abstractmethod

class SocialMedia(ABC):

    @abstractmethod
    def add_post(self):
        pass

    @abstractmethod
    def follow(self):
        pass

    @abstractmethod
    def share(self):
        pass

class Facebook(SocialMedia):

    def add_post(self):
        print("fb add post method")

    def follow(self):
        print("follow req in fb")

    def share(self):
        print("share reels and posts")

fb_instance = Facebook()

fb_instance.add_post()