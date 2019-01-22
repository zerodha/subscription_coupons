# -*- coding: utf-8 -*-
# Copyright (c) 2019, Zerodha and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import ast


class SubscriptionCouponCode(Document):
    pass


@frappe.whitelist()
def coupon_code_details(coupon_code, customer, plans):
    """
    return coupon code details
    """
    if isinstance(plans, unicode):
        plans = ast.literal_eval(plans)
    coupon_code = frappe.get_doc("Subscription Coupon Code", coupon_code)
    if coupon_code.customer and coupon_code.customer != customer:
        frappe.throw(
            "Coupon code not applicable to customer {}".format(customer)
        )

    for plan in plans:
        if coupon_code.plan and plan['plan'] != coupon_code.plan:
            frappe.throw(
                "Coupon code not applicable to plan {}".format(plan['plan'])
            )
    return {
        "apply_discount_on": coupon_code.apply_discount_on,
        "discount_percentage": coupon_code.discount_percentage,
        "discount_amount": coupon_code.discount_amount
    }


def validate(subscription, method):
    """
    validate coupon code and apply appropriate discount
    """
    if subscription.coupon_code:
        meta = coupon_code_details(
            subscription.coupon_code,
            subscription.customer,
            subscription.plans
        )
        subscription.apply_discount_on = meta['apply_discount_on']
        subscription.discount_percentage = meta['discount_percentage']
        subscription.discount_amount = meta['discount_amount']
