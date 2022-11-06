from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Link

class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = ['id', 'initial_url','new_url', 'user']
        read_only_fields = ['id','user','new_url']
        permission_classes = (IsAuthenticatedOrReadOnly)

    def create(self, validated_data):
        user_id = self.context['user_id']
        if validated_data['new_url'] != 1:
            return Link.objects.create(user_id=user_id, **validated_data)
        else:
            return Link.objects.get(user_id = user_id, initial_url = validated_data['initial_url'] )
            # return Link.objects.get(initial_url = validated_data['initial_url'] )

    def validate(self, data):
        user_id = self.context['user_id']
        list_initial_url = Link.objects.get_all_initiall_links(user_id)
        list_new_links = Link.objects.get_all_new_links(user_id)
        # list_initial_url = Link.objects.get_all_initiall_links()
        # list_new_links = Link.objects.get_all_new_links()
        initial_url = data['initial_url'].strip()
        if initial_url != '' and initial_url not in list_initial_url:
            list_initial_url.append(initial_url)
            new_url = Link.objects.check_new_url(list_new_links)
            data['new_url'] = new_url
            return data
        else:
            data['new_url'] = 1
            return data
