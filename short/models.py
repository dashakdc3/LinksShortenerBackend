from django.db import models
from string import ascii_letters, digits
import random
from linkShorter.settings import dev

class LinkFunc(models.Manager):

    def get_all_initiall_links(self, user_id):
        objects = Link.objects.filter(user_id = user_id)
    # def get_all_initiall_links(self):
    #     objects = Link.objects.all()
        list_initial_url = []
        for object in objects:
            list_initial_url.append(object.initial_url)
        return list_initial_url

    def get_all_new_links(self, user_id):
        objects = Link.objects.filter(user_id = user_id)
    # def get_all_new_links(self):
    #     objects = Link.objects.all()
        list_new_url = []
        for object in objects:
            list_new_url.append(object.new_url)
        return list_new_url

    def create_random_url(self):
        chars = ascii_letters + digits
        result= 'https://vfls.herokuapp.com/' + ''.join(random.choice(chars) for n in range(3))
        return result

    def check_new_url(self, list_new_url):
        new_url = self.create_random_url()
        if random in list_new_url:
            return self.check_new_url(list_new_url)
        return new_url
        

class Link(models.Model):
    initial_url = models.URLField()
    new_url = models.CharField(max_length=50, unique=True, blank=True)
    user = models.ForeignKey(
        dev.AUTH_USER_MODEL, related_name="link_user",
        on_delete=models.CASCADE
    )
    time_created = models.DateTimeField(auto_now_add=True)
    objects = LinkFunc()
    class Meta:
        ordering = ["time_created"]