⚙️ Installation Guide

Follow these steps inside your bench environment.

1. Create a New Site (If not already created)
bench new-site yoursite.com

2. Install ERPNext on the Site
bench --site yoursite.com install-app erpnext

3. Download the Custom App
bench get-app https://github.com/<your-repo>/codeace_customizations.git

4. Install the App on the Same Site
bench --site yoursite.com install-app codeace_customizations

5. Apply System Updates
bench build
bench migrate
bench clear-cache
