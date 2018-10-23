# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def about_view(request):

	context = {
		"Burak Ede"
		"Website: burakede.com.tr"
	}

	return render(request, 'about.html', context)
