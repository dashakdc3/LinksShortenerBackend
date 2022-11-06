from django.views.generic.base import RedirectView
from rest_framework.viewsets import mixins, GenericViewSet
from .models import Link
from .serializers import LinkSerializer

class LinkViewSet(mixins.CreateModelMixin,
                   GenericViewSet):

    def get_queryset(self):
        return Link.objects.filter(user = self.request.user)

    def get_serializer_context(self):
        return {'user_id': self.request.user.id,
                'request': self.request}

    serializer_class = LinkSerializer


class MyLinksViewSet(mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):

    def get_queryset(self):
        return Link.objects.filter(user = self.request.user)

    def get_serializer_context(self):
        return {'user_id': self.request.user.id,
                'request': self.request}

    serializer_class = LinkSerializer


class LinkRedirect(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            new_url = 'https://vfls.herokuapp.com/' + str(pk)
            object = Link.objects.get(new_url=new_url)
            url = object.initial_url   
            return url
        except Link.DoesNotExist:
            pass