# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Restouran(models.Model):
    owner = models.ForeignKey('auth.User', related_name='restourant', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=150)
    image = models.ImageField(blank=True, upload_to='static/images/', help_text='150x150px',
                              verbose_name='Ссылка картинки')

    def save(self, *args, **kwargs):
        super(Restouran, self).save(*args, **kwargs)


class Dish(models.Model):
    owner = models.ForeignKey('auth.User', related_name='dish', on_delete=models.CASCADE)
    restourant = models.ForeignKey(Restouran)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.TextField(max_length=150)
    image = models.ImageField(blank=True, upload_to='static/images/', help_text='150x150px',
                              verbose_name='Ссылка картинки')

    def save(self, *args, **kwargs):
        super(Dish, self).save(*args, **kwargs)


class Comment(models.Model):
    owner = models.ForeignKey('auth.User', related_name='comment', on_delete=models.CASCADE)
    restourant = models.ForeignKey(Restouran)
    username = models.CharField(max_length=20)
    text = models.TextField(max_length=150)
    date = models.DateField()

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)



