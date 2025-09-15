from flask import Flask, request, jsonify, render_template, send_file
from weasyprint import HTML
import io
import base64
from datetime import datetime

app = Flask(__name__, template_folder="templates")

# Helper: Generate PDF

def generate_pdf_from_html(template_name, context):
    html_str = render_template(template_name, **context)
    pdf_bytes = HTML(string=html_str).write_pdf()
    return pdf_bytes

# API Endpoint
@app.route("/generate-pdf", methods=["POST"])
def generate_pdf():
    try:
        payload = request.get_json(force=True) 
        pdf_type = payload.get("type")
        data = payload.get("data")
        output_format = payload.get("output", "base64") 

        if not pdf_type or not data:
            return jsonify({"error": "Missing 'type' or 'data'"}), 400

        context = {}

        # Invoice -->
        if pdf_type == "invoice":
            items = data.get("items", [])

            for item in items:
                item["total"] = item.get("qty", 0) * item.get("price", 0)

            grand_total = sum(item["total"] for item in items)

            context = {
                "company": data.get("company", "My Company"),
                "customer": data.get("customer", {}),
                "items": items,
                "invoice_id": data.get("invoice_id", "INV-001"),
                "date": data.get("date", "2025-09-15"),
                "total": grand_total,
            }
            pdf_bytes = generate_pdf_from_html("invoice.html", context)

        # Report Card -->
        elif pdf_type == "report_card":
            context = {
                "student": data.get("student", {}),
                "subjects": data.get("subjects", []),
                "total": data.get("total", 0),
                "grade": data.get("grade", "N/A"),
                "remarks": data.get("remarks", "Keep it up!"),
            }
            pdf_bytes = generate_pdf_from_html("report_card.html", context)

        # Certificate -->
        elif pdf_type == "certificate":
            context = {
                "name": data.get("name", "John Doe"),
                "course": data.get("course", "Python Development"),
                "date": datetime.now().strftime("%d-%m-%Y"),
                "issuer": data.get("issuer", "My Academy"),
            }
            pdf_bytes = generate_pdf_from_html("certificate.html", context)

        else:
            return jsonify({"error": "Invalid type. Use 'invoice', 'report_card', or 'certificate'"}), 400

        # Output handling -->
        if output_format == "base64":
            pdf_base64 = base64.b64encode(pdf_bytes).decode("utf-8")
            return jsonify({"pdf_base64": pdf_base64}), 200
        elif output_format == "file":
            return send_file(
                io.BytesIO(pdf_bytes),
                as_attachment=True,
                download_name=f"{pdf_type}.pdf",
                mimetype="application/pdf"
            )
        else:
            return jsonify({"error": "Invalid output format. Use 'base64' or 'file'"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
