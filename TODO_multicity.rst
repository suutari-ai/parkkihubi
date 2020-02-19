Multicity TODO
==============

* Make domain not required and update the migrations to run faster

* Enforcement API PermitSeries activate endpoint is pruning too much

  - Line ``prunable_series = PermitSeries.objects.prunable()`` is
    incorrect in api/enforcement/permit.py.  It should be limited to the
    owned PermitSeries only.
  
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
