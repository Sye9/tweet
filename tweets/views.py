# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import DetailView, ListView

from .models import Tweet

# Create your views here.

class TweetDetailView(DetailView):
	template_name = "tweets/detail_view.html"
	queryset = Tweet.objects.all()

	def get_object(self):
		return Tweet.object.get(id=1)

class TweetListView(ListView):
	template_name = "tweets/list_view.html"
	queryset = Tweet.objects.all()

# def tweet_detail_view(request, id=1):
# 	queryset = Tweet.objects.get(id=id)
# 	print(queryset)
# 	context = {
# 		'object': queryset
# 	}
# 	return render(request, "tweets/detail_view.html", context)

# def tweet_list_view(request):
# 	queryset = Tweet.objects.all()
# 	print(queryset)
# 	for obj in queryset:
# 		print(obj)
# 	context = {
# 		'object_list': queryset
# 	}
# 	return render(request, "tweets/list_view.html", context)