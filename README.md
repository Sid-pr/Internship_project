# 📄 PDF Generator API

A flexible Flask-based API to generate professional Invoices, Report Cards, and Certificates in PDF format.
The API accepts JSON input and returns either a downloadable PDF or a Base64 string, making it suitable for integration into modern applications.
---

## 🎯 Features

- 📑 Generate Invoices, Report Cards, and Certificates

- 📝 Accepts custom JSON input for dynamic PDF creation

- 🔄 Option to return PDF as Base64 (API friendly) or as a direct file download

- 📂 Uses separate HTML templates for easy customization

- ⚡ Lightweight & Fast – built on Flask + WeasyPrint
---


## 🛠️ Technologies Used

- **Python** (Pandas, Flask)
- **Weasyprint**(HTML ->PDF)
- **Jinja2 Templates**

---

## 📁 Project Structure
```bash
  .
  ├── app.py                  # Main Flask app
  ├── templates/              # HTML templates for PDFs
  │   ├── invoice.html
  │   ├── report_card.html
  │   └── certificate.html
  ├── requirements.txt        # Python dependencies
  ├── README.md               # Project documentation
  └── screenshots/            # Example output PDFs as images
```


## 📊 Sample Visuals

- 📈 Accidents by Hour of Day  
- ☁️ Weather Conditions vs. Severity  
- 🌍 Heatmap of Accident Locations (Folium)  
- 📅 Monthly Trend of Accidents  

<img width="1231" height="855" alt="Confusion_Matrix" src="https://github.com/user-attachments/assets/6436ba40-6dbc-4087-a080-fb62abd68a85" />


---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Sid-pr/Internship_project.git
   cd pdf-generator-api

2. Create Virtual Environment
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows

3. Install Dependencies
   ```bash
   pip install -r requirements.txt

4. API will be live at:
   http://127.0.0.1:5000/generate-pdf
