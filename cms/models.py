from django.db import models


class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/')
    cms_title = models.CharField(max_length=200, verbose_name='Title')
    cms_text = models.CharField(max_length=200, verbose_name='Text')
    # cms_css = models.Choices(label="CSS class", value=[' ', 'active'])
    cms_css = models.BooleanField(verbose_name="Main image", default=False)

    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = "Slide"
        verbose_name_plural = "Slides"
