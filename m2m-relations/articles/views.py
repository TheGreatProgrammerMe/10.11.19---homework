from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article, Membership


def articles_list(request):
	# используйте этот параметр для упорядочивания результатов
	# https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by

	template = 'articles/news.html'
	ordering = '-published_at'
	object_list = Article.objects.all().filter().order_by(ordering)

	Membership_objects = Membership.objects.all()
	all_article_name_set = set()
	all_scopes_dict = {}
	one_article_scope_arr = [] #список с тегом для конкретной статьи
	previous_title = None

	for membership in Membership_objects:
		if (membership.article.title not in all_article_name_set) and (previous_title != None):
			all_article_name_set.add(membership.article.title)
			previous_title = membership.article.title

		elif previous_title == None:
			previous_title = membership.article.title
			all_article_name_set.add(membership.article.title)
		
		if membership.is_main:
			if previous_title in all_scopes_dict:
				one_article_scope_arr = [all_scopes_dict[previous_title], [membership.scope.title, True]]
			else:
				one_article_scope_arr.append([membership.scope.title, True])

		else:
			if previous_title in all_scopes_dict:
				one_article_scope_arr = [all_scopes_dict[previous_title], [membership.scope.title, True]]
			else:
				one_article_scope_arr.append([membership.scope.title, False])
		print(one_article_scope_arr)
		all_scopes_dict.update({previous_title : one_article_scope_arr})
		print()
		print(all_scopes_dict)
		print()
		print()
		del one_article_scope_arr[:]

	# all_scopes_dict.update({previous_title : one_article_scope_arr})

	print(all_scopes_dict)


	context = {
	'object_list': object_list,
	}

	return render(request, template, context)
