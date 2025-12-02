import frappe 
import datetime
from frappe.utils import getdate


def validate_document_expiry(doc, method):
    fda_expiry_date = frappe.db.get_value("Company", doc.company, "custom_fda_expiry_date")
    alcohol_permit_expiry_date = frappe.db.get_value("Company", doc.company, "custom_alcohol_permit")
    export_certificate_expiry_date = frappe.db.get_value("Company", doc.company, "custom_export_certificate_expiry")
    if doc.posting_date:
        if getdate(fda_expiry_date) and getdate(doc.posting_date) > getdate(fda_expiry_date):
            frappe.throw(f"Cannot save Sales Invoice as FDC Expiry Date ({fda_expiry_date}) has passed.")
        if getdate(alcohol_permit_expiry_date) and getdate(doc.posting_date) > getdate(alcohol_permit_expiry_date):
            frappe.throw(f"Cannot save Sales Invoice as Alcohol Permit Expiry Date ({alcohol_permit_expiry_date}) has passed.")
        if getdate(export_certificate_expiry_date) and getdate(doc.posting_date) > getdate(export_certificate_expiry_date):
            frappe.throw(f"Cannot save Sales Invoice as Export Certificate Expiry Date ({export_certificate_expiry_date}) has passed.")