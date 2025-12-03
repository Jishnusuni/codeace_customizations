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
