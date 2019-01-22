// Copyright (c) 2019, Zerodha and contributors
// For license information, please see license.txt

frappe.ui.form.on('Subscription Coupon Code', {
	refresh: function(frm) {

	},
	validate: function(frm) {
		frm.toggle_reqd("discount_percentage", frm.doc.discount_type == "Percentage");
		frm.toggle_reqd("discount_amount", frm.doc.discount_type == "Amount");
	},
});