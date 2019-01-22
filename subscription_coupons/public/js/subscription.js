frappe.ui.form.on('Subscription', {
	coupon_code: function(frm){
		console.log("ssssss")
		frappe.call({
			method:"subscription_coupons.subscription_coupons.doctype.subscription_coupon_code.subscription_coupon_code.coupon_code_details",
			args: {
				coupon_code: frm.doc.coupon_code,
				customer: frm.doc.customer,
				plans: frm.doc.plans
			},
			freeze: true,
			callback: function(r) {
				frm.set_value("apply_additional_discount", r.message.apply_discount_on)
				frm.toggle_enable("apply_additional_discount", frm.doc.coupon_code == undefined)
				frm.toggle_enable("additional_discount_percentage", frm.doc.coupon_code == undefined)
				frm.toggle_enable("additional_discount_amount", frm.doc.coupon_code == undefined)

				frm.set_value("additional_discount_percentage", r.message.discount_percentage)
				frm.set_value("additional_discount_amount", r.message.discount_amount)
			}
		});
	}
})