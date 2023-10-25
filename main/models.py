from django.db import models


class InformationBox(models.Model):
    title = models.CharField(blank=False, max_length=60)
    main_text = models.TextField(blank=False, max_length=5000)
    box_img = models.ImageField(blank=False)

    def __str__(self):
        return f'{self.title}'

    @staticmethod
    def get_all_products():
        return InformationBox.objects.all()