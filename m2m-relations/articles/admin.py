from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Membership

class RelationshipInlineFormset(BaseInlineFormSet):
	def clean(self):
		one_true = False
		for form in self.forms:
			# В form.cleaned_data будет словарь с данными
			# каждой отдельной формы, которые вы можете проверить
			form.cleaned_data
			# вызовом исключения ValidationError можно указать админке о наличие ошибки
			# таким образом объект не будет сохранен,
			# а пользователю выведется соответствующее сообщение об ошибке

			if form.cleaned_data['is_main'] == True:
				if one_true:
					raise ValidationError('Может быть только один основной раздел')
					return super().clean()
				else:
					one_true = True

		if one_true == False:
			raise ValidationError('Укажите основной раздел')
			return super().clean()





class MembershipInline(admin.TabularInline):
	model = Membership
	formset = RelationshipInlineFormset
	extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	inlines = (MembershipInline,)

@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
	pass