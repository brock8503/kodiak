from typing import Any

import pytest

from web_api.models import StripeCustomerInformation


@pytest.mark.django_db
def test_expired(mocker: Any) -> None:
    """
    The subscription should be expired if past the period end. We give a grace
    period of two days, so to be expired we need to be three days pass the
    expiration period.
    """
    ONE_DAY_SEC = 60 * 60 * 24
    period_start = 1650581784
    period_end = 1655765784 + ONE_DAY_SEC * 30  # start plus one month.
    mocker.patch("web_api.models.time.time", return_value=period_end + ONE_DAY_SEC * 3)
    stripe_customer_info = StripeCustomerInformation.objects.create(
        customer_id="cus_Ged32s2xnx12",
        subscription_id="sub_Gu1xedsfo1",
        plan_id="plan_G2df31A4G5JzQ",
        customer_email="accounting@acme-corp.com",
        customer_balance=0,
        customer_created=1585781308,
        plan_amount=499,
        upcoming_invoice_subtotal=3 * 499,
        upcoming_invoice_total=3 * 499,
        subscription_quantity=3,
        subscription_start_date=1585781784,
        subscription_current_period_start=period_start,
        subscription_current_period_end=period_end,
    )

    assert stripe_customer_info.expired is True


@pytest.mark.django_db
def test_expired_inside_grace_period(mocker: Any) -> None:
    """
    Inside the grace period (two days) we will not show the subscription as
    expired.
    """
    ONE_DAY_SEC = 60 * 60 * 24
    period_start = 1650581784
    period_end = 1655765784 + 30 * ONE_DAY_SEC  # start plus one month.
    mocker.patch("web_api.models.time.time", return_value=period_end + ONE_DAY_SEC)
    stripe_customer_info = StripeCustomerInformation.objects.create(
        customer_id="cus_Ged32s2xnx12",
        subscription_id="sub_Gu1xedsfo1",
        plan_id="plan_G2df31A4G5JzQ",
        customer_email="accounting@acme-corp.com",
        customer_balance=0,
        customer_created=1585781308,
        plan_amount=499,
        subscription_quantity=3,
        upcoming_invoice_subtotal=3 * 499,
        upcoming_invoice_total=3 * 499,
        subscription_start_date=1585781784,
        subscription_current_period_start=period_start,
        subscription_current_period_end=period_end,
    )

    assert stripe_customer_info.expired is False
