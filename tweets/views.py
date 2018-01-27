# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, get_object_or_404

from django.urls import reverse

from django.views.generic import (
	CreateView,
	DetailView,
	DeleteView,
	ListView,
	UpdateView
	)

from .forms import TweetModelForm

from .models import Tweet

from .mixins import FormUserNeededMixin, UserOwnerMixin

# Create your views here.

class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
	form_class = TweetModelForm
	template_name = 'tweets/create_view.html'
	# success_url = reverse_lazy("tweet:detail")
	login_url = "/admin/login/"

class TweetUpdateView(UserOwnerMixin, LoginRequiredMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = 'tweets/update_view.html'
	# success_url = '/tweet/'

class TweetDeleteView(LoginRequiredMixin, DeleteView):
	model = Tweet
	success_url = reverse("tweet:list")
	template_name = 'tweets/delete_confirm.html'
	

class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()

class TweetListView(ListView):
	queryset = Tweet.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		return context