from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
import os

import subprocess

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from datetime import date

def generate_receipt(pdf_file:str, receipt_id:str, customer, data:list, raw_total:str, auto_open=False, c_date=None):
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)
    # Create a list to hold the content of the receipt
    story = []

    path = os.path.join(os.path.join(os.getcwd(),'logic'), 'logo.jpg')
    # Logo
    logo = Image(path, 200, 100)
    story.append(logo)
    txt_style_center = getSampleStyleSheet()["Normal"]
    txt_style_center.alignment = TA_CENTER
    story.append(Paragraph(f"Address: Pul-e-Charkhi Industrial Parks, Kabul, Afghanistan", txt_style_center))
    story.append(Paragraph(f"Ph: 0777919119", txt_style_center))
    story.append(Spacer(1, 10))  # Add some space


    # Header
    header_style = getSampleStyleSheet()["Title"]
    header_style.alignment = TA_CENTER
    header_text = Paragraph("<b>Receipt</b>", header_style)
    story.append(header_text)
    story.append(Spacer(1, 20))  # Add some space

    # Receipt id
    txt_style_left = getSampleStyleSheet()["BodyText"]
    txt_style_left.alignment = TA_LEFT
    receipt_txt = Paragraph(f"<b>Receipt ID:</b> {receipt_id}", txt_style_left)
    story.append(receipt_txt)
    story.append(Spacer(1, 10))  # Add some space

    # Customer name
    customer_text = Paragraph(f"<b>Name:</b> {customer.name}", txt_style_left)
    story.append(customer_text)
    story.append(Spacer(1, 10))  # Add some space

    # Customer address
    customer_text = Paragraph(f"<b>Address:</b> {customer.address}", txt_style_left)
    story.append(customer_text)
    story.append(Spacer(1, 10))  # Add some space

    # Customer Ph#
    customer_ph_text = Paragraph(f"<b>Phone Number:</b> {customer.ph}", txt_style_left)
    story.append(customer_ph_text)
    story.append(Spacer(1, 10))  # Add some space

    # Date
    if c_date is None:
        today = date.today().strftime("%b-%d-%Y")
    else:
        today = c_date
    story.append(Paragraph(f"<b>Date: </b> {today}", txt_style_left))
    story.append(Spacer(1, 20))  # Add some space

    # Table for item details
    item_details = [
        ['Product ID', 'Product Name', 'Unit Price', 'Quantity', 'Discount%', 'Discounted Unit Price', 'Total Price']]
    for item in data:
        item_details.append(item)  # Replace '$10.00' with the actual price

    table_style = TableStyle([

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),

    ])

    table = Table(item_details)
    table.setStyle(table_style)
    story.append(table)
    story.append(Spacer(1, 5))  # Add some space

    # Draw a horizontal line below the table
    line = HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.black)
    story.append(line)
    story.append(Spacer(1, 20))  # Add some space

    # Total Amount
    story.append(Paragraph(f"<b>Total:</b> {raw_total}", txt_style_left))
    story.append(Spacer(1, 10))  # Add some space

    # Build the receipt and save to the PDF file
    doc.build(story)

    if auto_open:
        try:
            subprocess.Popen(["xdg-open", pdf_file])  # For Linux (Ubuntu)
        except:
            try:
                subprocess.Popen(["open", pdf_file])  # For macOS
            except:
                try:
                    subprocess.Popen(["start", "", pdf_file], shell=True)  # For Windows
                except:
                    print("Unable to open PDF automatically. Please open the PDF manually.")
