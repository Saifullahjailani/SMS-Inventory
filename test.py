import io
import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, HRFlowable, PageTemplate, Frame
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

def generate_receipt(customer_name, items_purchased, total_amount, logo_path):
    # Create a BytesIO buffer to store the PDF content in memory
    pdf_buffer = io.BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)

    # Create a list to hold the content of the receipt
    story = []

    # Create a frame for the header
    header_frame = Frame(doc.leftMargin, doc.height - 50, doc.width, 50, showBoundary=0)

    # Logo
    logo = Image(logo_path, 200, 100)
    story.append(logo)
    story.append(Spacer(1, 10))  # Add some space

    # ... (rest of the receipt content as before)

    # Table for item details
    item_details = [['Item', 'Price']]
    for item in items_purchased.split(','):
        item_details.append([item.strip(), '$10.00'])  # Replace '$10.00' with the actual price

    table_style = TableStyle([
        # Table styles as before
    ])

    table = Table(item_details)
    table.setStyle(table_style)
    story.append(table)
    story.append(Spacer(1, 20))  # Add some space

    # Draw a horizontal line below the table
    line = HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.black)
    story.append(line)
    story.append(Spacer(1, 20))  # Add some space

    # Total Amount
    total_style = getSampleStyleSheet()["Heading3"]
    total_style.alignment = TA_RIGHT
    total_text = Paragraph(f"<b>Total Amount: ${total_amount}</b>", total_style)
    story.append(total_text)

    # Add the header to each page
    doc.addPageTemplates([PageTemplate(frames=[header_frame], onPage=header)])

    # Build the receipt and save to the PDF buffer
    doc.build(story)

    # Reset the buffer position to the beginning
    pdf_buffer.seek(0)

    # Open the PDF content using the system's default PDF viewer
    try:
        subprocess.Popen(["xdg-open", "-", pdf_buffer.read()], stdin=subprocess.PIPE)  # For Linux (Ubuntu)
    except:
        try:
            subprocess.Popen(["open", "-f", "-a", "Preview", "-"], stdin=subprocess.PIPE, shell=True)  # For macOS
        except:
            try:
                subprocess.Popen(["start", "", pdf_buffer.read()], stdin=subprocess.PIPE, shell=True)  # For Windows
            except:
                print("Unable to open PDF automatically. Please open the PDF manually.")

def header(canvas, doc):
    # Header content
    customer_name = "John Doe"  # Replace with the actual customer name
    header_text = f"Customer Name: {customer_name}"

    # Draw the header text
    canvas.saveState()
    canvas.setFont("Helvetica", 12)
    canvas.drawRightString(doc.width - doc.rightMargin, doc.height - doc.topMargin + 30, header_text)
    canvas.restoreState()

if __name__ == "__main__":
    customer_name = "John Doe"
    items_purchased = "Item 1, Item 2, Item 3"
    total_amount = 30.00
    logo_path = "path/to/your/logo.png"  # Replace with the actual path to your logo image

    generate_receipt(customer_name, items_purchased, total_amount, logo_path)
