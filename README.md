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


## Sample Visuals
1. Certificate:
   <img width="884" height="937" alt="image" src="https://github.com/user-attachments/assets/26badfc1-ff8e-459a-962a-b00254451f76" />

2. Invoice:
    <img width="1049" height="646" alt="image" src="https://github.com/user-attachments/assets/a88c7000-5749-4de8-9b51-8873a5736fdd" />


3. Report Card:
   <img width="1055" height="822" alt="image" src="https://github.com/user-attachments/assets/5b0c2f90-df40-413b-a2a3-7fd595effd40" />



---

## Sample Input
1. Certificate
   ```bash
       {
      "type": "certificate",
      "output":"file",
      "data": {
        "name": "Sample name",
        "course": "Full Stack Web Development",
        "date": "2025-09-15",
        "issuer": "XYZ Institute"
      }
    }

2. Invoice
   ```bash
     {
    "type": "invoice",
    "output": "file",
    "data": {
      "company": "Tech Corp",
      "customer": {"name": "Alice"},
      "items": [{"name": "Laptop", "qty": 1, "price": 120000},
      {"name": "Phone", "qty": 2, "price": 12000}],
      "total": 140000
    }
    }

   
3. Report Card
   ```bash
    {
      "type": "report_card",
      "output":"file",
      "data": {
        "student": {
          "name": "Sample name",
          "roll": "56",
          "class": "6th sem"
        },
        "subjects": [
          { "name": "Data Structures", "marks": 85 },
          { "name": "Operating Systems", "marks": 78 },
          { "name": "DBMS", "marks": 92 },
          { "name": "Computer Networks", "marks": 88 }
        ],
        "total": 343,
        "grade": "A",
        "remarks": "Excellent performance! Keep up the good work."
      }
    }

---
NOTE:- If you want the result in base 64 format just remove the "output:file" from the input.
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
