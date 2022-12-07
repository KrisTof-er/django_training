from django.db import models


class StatusCRM(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Status Name')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True, verbose_name='Date')
    order_name = models.CharField(max_length=200, verbose_name='Name')
    order_phone = models.CharField(max_length=200, verbose_name='Phone')
    order_status = models.ForeignKey(
        to=StatusCRM, on_delete=models.PROTECT,
        null=True, blank=True,
        verbose_name='Status'
    )

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class CommentCRM(models.Model):
    comment_binding = models.ForeignKey(
        to=Order, on_delete=models.CASCADE,
        verbose_name='Order'
    )
    comment_text = models.TextField(verbose_name='Comment Text', max_length=300)
    comment_date = models.DateTimeField(auto_now=True, verbose_name='Creation Date')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
