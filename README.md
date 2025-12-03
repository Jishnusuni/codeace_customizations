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

   1. Manage several legal entities within a single ERPNext instance.
  
   2. Support for multiple operational units under each entity.
    
   3. Every unit can operate with its own warehouse, stock, and accounting records.
    
   4. Ensures that pricing, valuation, and transaction data stay isolated for each entity.

2. Item Control & Stock Handling

    1. Create beverage SKUs with batch and expiry monitoring.
    
    2. Monitor stock availability across all warehouses and locations.
    
    3. Prevent sales of expired or soon-to-expire lots.
    
    4. Simulated reorder suggestions based on inventory thresholds.
    
    5. Batch-level tracking for every product variant.

3. Procurement & Sales Operations
    
    1. Multi-currency support using ERPNext’s built-in financial tools.
    
    2. Track pending quantities, partially received shipments, and open deliveries.
    
    3. Movement of goods tracked using the Shipment doctype and Delivery modules.

4. Regulatory & Document Compliance

    1. Store permits and certificates required for beverage trade.
    
    2. Automated expiry reminders before critical documents lapse.
    
    3. Validation checks ensure all mandatory permits are valid before a transaction can proceed.
    
    4. Custom fields added to Company for simple document management.

5. Shipment Lifecycle & Container Movement

    1. Framework to track shipments from origin to destination.
    
    2. Predefined states:
      Packed → On Route → Reached Port → Released → Delivered
    
    3. Shipments can be tagged to specific locations and warehouses.
    
    4. Workflow actions exported through fixtures for easy reuse.
    
    5. Overview dashboards to monitor logistics progress.

6. Fleet & Delivery Tracking

    Assign drivers and vehicles to outgoing deliveries.
    
    Uses Delivery Trip, Vehicle, and Driver doctypes for operation flow.

7. Insights & Operational Dashboards

Visual overviews for:

    Stock by company and location
    
    Shipment movement
    
    Delivery progress

🖼️ Visual References

✔ Overview Dashboard

<img width="1557" height="848" alt="image" src="https://github.com/user-attachments/assets/45ea1501-2319-479b-82b7-1cf3df492ef9" />

✔ Company & Warehouse Configuration

<img width="1557" height="365" alt="image" src="https://github.com/user-attachments/assets/8a981ac2-d9eb-42d2-b13d-c0dc603b9d35" />
<img width="1557" height="365" alt="image" src="https://github.com/user-attachments/assets/4b147020-dc3a-4fb5-8094-c5fb0396ddbf" />
<img width="1557" height="365" alt="image" src="https://github.com/user-attachments/assets/cd560143-0a14-4a05-aab0-242a7c0ee546" />
<img width="1557" height="365" alt="image" src="https://github.com/user-attachments/assets/9d0dba89-b122-4307-b8ad-1cf17771aa16" />
<img width="1559" height="438" alt="image" src="https://github.com/user-attachments/assets/1a4de960-be8e-41f3-a5f7-c268a7a3065e" />


✔ Batch & Expiry Tracking

<img width="1461" height="714" alt="image" src="https://github.com/user-attachments/assets/0a1dad58-11af-4b27-92de-00c3b5817066" />


✔ Shipment Flow
<img width="1512" height="781" alt="image" src="https://github.com/user-attachments/assets/8dcb4cae-e0e3-4534-b3d9-25052e126713" />
<img width="1512" height="781" alt="image" src="https://github.com/user-attachments/assets/7553cd45-6a6a-4352-b52d-4d7b2fbeb4d0" />

✔ Vehicle & Delivery Progress
<img width="1518" height="841" alt="image" src="https://github.com/user-attachments/assets/8f01544a-268c-45f8-8205-0dc315c57f6a" />
<img width="1547" height="558" alt="image" src="https://github.com/user-attachments/assets/10d51a76-f2bc-4738-866d-029e8e9476fa" />
<img width="1529" height="545" alt="image" src="https://github.com/user-attachments/assets/25ec79c6-ef45-4908-81a4-5c3a0e7c01ab" />




