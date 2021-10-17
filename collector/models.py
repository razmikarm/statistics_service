from django.db import models

from collector.utils import handle_zero_div


class Statistics(models.Model):
    date = models.DateField(
        "Date of collected statistics"
    )

    views = models.IntegerField(
        "Count of views in statistics",
        default=0
    )

    clicks = models.IntegerField(
        "Count of clicks in statistics",
        default=0
    )

    cost = models.IntegerField(
        "Amount of cost of clicks in statistics",
        default=0
    )

    created_at = models.DateTimeField(
        "Record adding datetime",
        auto_now_add=True,
    )

    updated_at = models.DateField(
        "Record last updated",
        auto_now=True,
    )

    class Meta:
        verbose_name = "Collected Statistics"
        ordering = ("date", "views", "clicks", "cost")

    def __str__(self):
        return f"{self.date}"

    def __repr__(self):
        return f"Statistics({self.date}, {self.views}, {self.clicks}, {self.cost})"

    @handle_zero_div
    def cpc(self):
        return f"{(self.cost / self.clicks):.2f}"

    @handle_zero_div
    def cpm(self):
        return f"{(self.cost / self.views):.2f}"
