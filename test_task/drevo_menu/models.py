from django.db import models


class MenuDrevo(models.Model):
    menu_title = models.CharField(max_length=50, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.menu_title
