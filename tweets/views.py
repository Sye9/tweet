# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from django.views.generic import (
	DetailView,
	ListView,
	CreateView
	)

from .forms import TweetModelForm

from .models import Tweet

# Create your views here.

class TweetCreateView(CreateView):
	form_class = TweetModelForm
	template_name = 'tweets/create_view.html'
	success_url = "/tweet/create/"

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(TweetCreateView, self).form_valid(form)

class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()

	# def get_object(self):
	# 	print(self.kwargs)
	# 	pk = self.kwargs.get("pk")
	# 	obj = get_object_or_404(Tweet, pk=pk)
	# 	return obj

class TweetListView(ListView):
	queryset = Tweet.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		# context["another_list"] = Tweet.objects.all()
		# print(context)
		return context