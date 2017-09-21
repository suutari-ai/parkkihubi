from django.contrib.gis.db import models
from django.contrib.gis.db.models.functions import Distance
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import localtime, now
from django.utils.translation import ugettext_lazy as _

from parkings.models.mixins import TimestampedModelMixin, UUIDPrimaryKeyMixin
from parkings.models.operator import Operator
from parkings.models.parking_area import ParkingArea

from .parking_terminal import ParkingTerminal


class Parking(TimestampedModelMixin, UUIDPrimaryKeyMixin):
    VALID = 'valid'
    NOT_VALID = 'not_valid'

    parking_area = models.ForeignKey(
        ParkingArea, on_delete=models.SET_NULL, verbose_name=_("parking area"), related_name='parkings', null=True,
        blank=True,
    )
    terminal_number = models.CharField(
        max_length=50,  blank=True,
        verbose_name=_("terminal number"),
    )
    terminal = models.ForeignKey(
        ParkingTerminal, null=True, blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_("terminal"),
    )
    location = models.PointField(verbose_name=_("location"), null=True, blank=True)
    operator = models.ForeignKey(
        Operator, on_delete=models.PROTECT, verbose_name=_("operator"), related_name="parkings"
    )
    registration_number = models.CharField(max_length=20, db_index=True, verbose_name=_("registration number"))
    time_start = models.DateTimeField(
        verbose_name=_("parking start time"), db_index=True,
    )
    time_end = models.DateTimeField(
        verbose_name=_("parking end time"), db_index=True, null=True, blank=True,
    )
    zone = models.IntegerField(verbose_name=_("zone number"), validators=[
        MinValueValidator(1), MaxValueValidator(3),
    ])

    class Meta:
        verbose_name = _("parking")
        verbose_name_plural = _("parkings")

    def __str__(self):
        start = localtime(self.time_start).replace(tzinfo=None)

        if self.time_end is None:
            return "%s -> (%s)" % (start, 'ABC-123')

        if self.time_start.date() == self.time_end.date():
            end = localtime(self.time_end).time().replace(tzinfo=None)
        else:
            end = localtime(self.time_end).replace(tzinfo=None)

        return "%s -> %s (%s)" % (start, end, 'ABC-123')

    def get_state(self):
        current_timestamp = now()

        if self.time_start > current_timestamp:
            return Parking.NOT_VALID

        if self.time_end and self.time_end < current_timestamp:
            return Parking.NOT_VALID

        return Parking.VALID

    def get_closest_area(self, max_distance=50):
        if self.location:
            location = self.location
        else:
            return None

        closest_area = ParkingArea.objects.annotate(
            distance=Distance('geom', location),
        ).filter(distance__lte=max_distance).order_by('distance').first()
        return closest_area

    def save(self, *args, **kwargs):
        if not self.terminal and self.terminal_number:
            self.terminal = ParkingTerminal.objects.filter(
                number=_try_cast_int(self.terminal_number)).first()

        if self.terminal and not self.location:
            self.location = self.terminal.location

        self.parking_area = self.get_closest_area()

        super(Parking, self).save(*args, **kwargs)


def _try_cast_int(value):
    try:
        return int(value)
    except ValueError:
        return None
