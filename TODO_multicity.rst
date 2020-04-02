Multicity TODO
==============

* Make domain not required and update the migrations to run faster

* Is Enforcement API PermitSeries activate endpoint pruning too much?

  - First thought that pruning should be limited to the permit series of
    the current user, but maybe it's OK to prune *all* inactive permit
    series after the three days, but that just have to be documented.

* Make PermitLookupItem.area a FK instead of char field

  - Change the PermitArea.id field to be integer rather than UUID

    - This would be good because db will work faster with integers

* Endpoints for payment zone and permit area listing

* operator/permit.py:13: Check if Meta fields is needed for the
  serializer or not

* PaymentZone referencing by code instead of number:

  - test cases for payment zone by non-int code

* Make sure that permit series activation in Enforcement API does not
  deactivate operator series

  - test cases for permit series deactivation

* Make sure that default domain is not used for PermitAreas and other
  such objects (only for Parkings)

* What to do with dashboard regarding multicity?

* What to do with public API regarding multicity?

* Are enforcer limitations even implemented yet? (Can Helsinki see Espoo
  or vice versa?)
