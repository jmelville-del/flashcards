from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

card_length = 5*inch
card_height = 3*inch
card = (card_length,card_height)

c = canvas.Canvas('cards.pdf', pagesize=card)
page_number = 0
with open('words.txt', "r") as f:
    for word in f:
        page_number+=1
        c.setFont('Helvetica', card_height/3)
        c.drawCentredString(card_length/2, ((card_height/2)-(card_height/12)), word.strip())
        c.setFont('Helvetica', card_height/10)
        c.drawRightString(card_length*0.95, card_length*0.05, str(page_number))
        c.showPage()
    c.save()