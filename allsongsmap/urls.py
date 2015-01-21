from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from musicmapper.models import Artist, Story, Song
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class StorySerializer(serializers.HyperlinkedModelSerializer):
		class Meta:
				model = Story
				fields = ('storyId', 'title', 'description', 'date', 'thumbnail')

# ViewSets define the view behavior.
class StoryViewSet(viewsets.ModelViewSet):
		queryset = Story.objects.all()
		serializer_class = StorySerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'stories', StoryViewSet)



urlpatterns = patterns('',
		# Examples:
		# url(r'^$', 'allsongsmap.views.home', name='home'),
		# url(r'^blog/', include('blog.urls')),

		url(r'^admin/', include(admin.site.urls)),
		url(r'^', include('musicmapper.urls')),
		url(r'^', include(router.urls)),
		url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
