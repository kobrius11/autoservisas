from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.
class CarModel(models.Model):
    make = models.CharField(_("make"), max_length=250)
    model = models.CharField(_("model"), max_length=250)
    year = models.PositiveIntegerField(_("year"), default=2000)
    engine = models.CharField(_("engine"), max_length=250)

    class Meta:
        verbose_name = _("car model")
        verbose_name_plural = _("car models")

    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.engine}"

    def get_absolute_url(self):
        return reverse("carmodel_detail", kwargs={"pk": self.pk})


class Car(models.Model):
    plate_nr = models.CharField(_("Valstybinis NR"), max_length=50)
    vin = models.CharField(_("VIN"), max_length=50)
    client = models.CharField(_("client"), max_length=250)
    car_model = models.ForeignKey(
        CarModel, 
        verbose_name=_("car model"), 
        on_delete=models.CASCADE,
        related_name='cars'
    )


    class Meta:
        verbose_name = _("car")
        verbose_name_plural = _("cars")

    def __str__(self):
        return f"{self.plate_nr} {self.vin} {self.client} {self.car_model}"

    def get_absolute_url(self):
        return reverse("car_detail", kwargs={"pk": self.pk})
    

class Order(models.Model):
    date = models.DateField(_("date"), auto_now=False, auto_now_add=True)
    cost = models.FloatField(_("cost"))
    car = models.ForeignKey(
        Car, 
        verbose_name=_("car"), 
        on_delete=models.CASCADE,
        related_name='cars'    
    )
    

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return f"{self.date} {self.cost} {self.car}"

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})


class Service(models.Model):
    name = models.CharField(_("name"), max_length=250)
    cost = models.FloatField(_("cost"))
    

    class Meta:
        verbose_name = _("service")
        verbose_name_plural = _("services")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("service_detail", kwargs={"pk": self.pk})


class OrderField(models.Model):
    cost = models.FloatField(_("cost"))
    quantity = models.PositiveIntegerField(_("quantity"))
    service = models.ForeignKey(
        Service, 
        verbose_name=_("service"), 
        on_delete=models.CASCADE,
        related_name='services'
    )
    order = models.ForeignKey(
        Order, 
        verbose_name=_("order"), 
        on_delete=models.CASCADE,
        related_name='orders'
    )

    class Meta:
        verbose_name = _("order field")
        verbose_name_plural = _("order fields")

    def __str__(self):
        return f"{self.cost} {self.quantity} {self.service}"

    def get_absolute_url(self):
        return reverse("order_field_detail", kwargs={"pk": self.pk})


