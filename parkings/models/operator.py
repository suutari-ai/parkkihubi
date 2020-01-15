from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _

from parkings.models.mixins import TimestampedModelMixin, UUIDPrimaryKeyMixin

from .enforcement_domain import EnforcementDomain


class Operator(TimestampedModelMixin, UUIDPrimaryKeyMixin):
    name = models.CharField(verbose_name=_("name"), max_length=80)
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name=_("user"))
    owned_domain = models.ForeignKey(
        EnforcementDomain, null=True, blank=True,
        verbose_name=_("owned enforcement domain"), help_text=_(
            "An enforcement domain than is owned by this operator, if any."))

    class Meta:
        verbose_name = _("operator")
        verbose_name_plural = _("operators")

    def __str__(self):
        return self.name
