⚙️ Installation Guide

Follow these steps inside your bench environment.

1. Create a New Site (If not already created)
```
bench new-site yoursite.com
```
2. Install ERPNext on the Site
```
bench --site yoursite.com install-app erpnext
```
4. Download the Custom App
```
bench get-app https://github.com/Jishnusuni/codeace_customizations.git
```
6. Install the App on the Same Site
```
bench --site yoursite.com install-app codeace_customizations
```
8. Apply System Updates
```
bench build
bench migrate
bench clear-cache
```


Codeace Customizations
ERPNext Extension for Beverage Distribution & International Trade

Codeace Customizations is an ERPNext add-on designed for businesses involved in beverage distribution, import operations, and multi-location management. The app introduces structured workflows, automated checks, and practical tools that simplify daily operations across companies, branches, and warehouses.

🌐 Core Capabilities
1. Organization & Location Management

Manage several legal entities within a single ERPNext instance.

Support for multiple operational units under each entity.

Every unit can operate with its own warehouse, stock, and accounting records.

Ensures that pricing, valuation, and transaction data stay isolated for each entity.

2. Item Control & Stock Handling

Create beverage SKUs with batch and expiry monitoring.

Monitor stock availability across all warehouses and locations.

Prevent sales of expired or soon-to-expire lots.

Simulated reorder suggestions based on inventory thresholds.

Batch-level tracking for every product variant.

3. Procurement & Sales Operations

Seamless handling of local and international orders.

Multi-currency support using ERPNext’s built-in financial tools.

Bills and commercial documents are added automatically as attachments.

Track pending quantities, partially received shipments, and open deliveries.

Movement of goods tracked using the Shipment doctype and Delivery modules.

4. Regulatory & Document Compliance

Store permits and certificates required for beverage trade.

Automated expiry reminders before critical documents lapse.

Validation checks ensure all mandatory permits are valid before a transaction can proceed.

Custom fields added to Company for simple document management.

5. Shipment Lifecycle & Container Movement

Framework to track shipments from origin to destination.

Predefined states:
Packed → On Route → Reached Port → Released → Delivered

Shipments can be tagged to specific locations and warehouses.

Workflow actions exported through fixtures for easy reuse.

Overview dashboards to monitor logistics progress.

6. Fleet & Delivery Tracking

Assign drivers and vehicles to outgoing deliveries.

Simulated tracking coordinates for demonstration.

Delivery status updates applied automatically based on trip activity.

Uses Delivery Trip, Vehicle, and Driver doctypes for operation flow.

7. Insights & Operational Dashboards

Visual overviews for:

Stock by company and location

Shipment movement

Delivery progress

Helps management quickly evaluate supply chain and inventory health.
