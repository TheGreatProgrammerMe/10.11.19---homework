from django.db import models

class Scope(models.Model):
	title = models.CharField(max_length=256, verbose_name='Раздел')

	
	class Meta:
		verbose_name = 'Раздел'
		verbose_name_plural = 'Разделы'

	def __str__(self):
		return self.title

class Article(models.Model):

	title = models.CharField(max_length=256, verbose_name='Название')
	text = models.TextField(verbose_name='Текст')
	published_at = models.DateTimeField(verbose_name='Дата публикации')
	image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
	scopes = models.ManyToManyField(
		Scope, 
		through='Membership',
		related_name='scopes', 
		verbose_name='Раздел',
		)

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

	def __str__(self):
		return self.title

class Membership(models.Model):
	scope = models.ForeignKey(
		Scope,
		on_delete=models.CASCADE,
		verbose_name='Раздел'
		)
	article = models.ForeignKey(
		Article,
		on_delete=models.CASCADE,
		verbose_name='Статья'
		)
	is_main = models.BooleanField(default = False, verbose_name='Основной')


	
	
	class Meta:
		verbose_name = 'Тематика статьи'
		verbose_name_plural = 'Тематика статьи'
		
	def __str__(self):
		return self.article.title