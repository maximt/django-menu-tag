from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse
import json


class Menu(models.Model):
    name = models.CharField(max_length=128,
                            null=False, blank=False, unique=True)
    title = models.CharField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    title = models.CharField(max_length=256, null=False, blank=False)

    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True, related_name='items')

    depth = models.IntegerField(default=0)
    mpath = models.CharField(max_length=512, null=True, blank=True, default='')

    url = models.URLField(max_length=2048, null=True, blank=True)
    named_url = models.CharField(max_length=256, null=True, blank=True)
    named_url_kwargs = models.CharField(max_length=256, null=True, blank=True)

    def get_url(self):
        if self.named_url:
            url_kwargs = {}
            if self.named_url_kwargs:
                try:
                    url_kwargs = json.loads(self.named_url_kwargs)
                except json.JSONDecodeError:
                    url_kwargs = {}
            return reverse(
                self.named_url,
                kwargs=url_kwargs
            )

        if self.url:
            return self.url

        return None

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['mpath']

    def save(self, *args, **kwargs, ):
        if not self.pk:
            super().save(*args, **kwargs)  # we need pk for path

        if self.parent:
            self.mpath = "{}/{}".format(self.parent.mpath, self.pk)
            self.depth = self.parent.depth + 1
        else:
            self.mpath = self.pk
            self.depth = 0

        super().save()


@receiver(post_save, sender=MenuItem)
def update_mpath_children(sender, instance, **kwargs):
    for child in instance.items.all():
        child.save()
