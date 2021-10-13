from django.db import models


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
        "DateTime when the record has been added",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Collected Statistics"
        ordering = ("data", "views", "clicks", "cost")

    def __str__(self):
        return f"{self.date}"

    def __repr__(self):
        return f"Statistics({self.date}, {self.views}, {self.clicks}, {self.cost})"
