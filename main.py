from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Frame, Image
from reportlab.lib.units import cm,mm,inch
from reportlab.rl_config import defaultPageSize
from reportlab.lib import utils

PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()
styles = getSampleStyleSheet()
styleN = styles['Normal']
styleH = styles['Heading1']

def get_image(path, width=1*cm):
    img = utils.ImageReader(path)
    iw, ih = img.getSize()
    aspect = ih / float(iw)
    width=width
    height=(width * aspect)
    return Image(path, width, height),width,height

def user_invoice_generator(canvas,data):
    canvas.saveState()

    #comapny_details
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-38, 'Comapny Name')
    canvas.setFont('Times-Roman',10)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-50, 'Comapny Collony , Khan Para , South 24 PGS')
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-60, 'Pin-908756, West Bengal')
    #calling details
    image_link,width,height=get_image('call_icon.png', width=0.5*cm)
    story_call_icon = []
    story_call_icon.append(image_link)
    frame_call_icon = Frame(PAGE_WIDTH/1.56, PAGE_HEIGHT-32 ,width+0.5*cm,height+0.5*cm)
    frame_call_icon.addFromList(story_call_icon, canvas)
    canvas.drawCentredString(PAGE_WIDTH/1.24, PAGE_HEIGHT-20, ' +91-7045893672 / +91-894379087')
    canvas.setFont('Times-Roman',9)

    #page details
    canvas.drawString(0.3*inch, 0.3 * inch, "First Page / %s" % 'Invoice')
    canvas.restoreState()

    #comapny_icon
    image_link,width,height=get_image('comp_icon.png', width=2.5*cm)
    story_company_icon = []
    story_company_icon.append(image_link)
    frame_company_icon = Frame(1*cm, PAGE_HEIGHT-88 ,width+0.5*cm,height+0.5*cm)
    frame_company_icon.addFromList(story_company_icon, canvas)

    #user_details
    canvas.setFont('Times-Roman',9)
    if 'user_name' in data.keys():
        canvas.drawString(PAGE_WIDTH/1.3, PAGE_HEIGHT-35, 'Name : '+data['user_name'])
    if 'mobile_no' in data.keys():
        canvas.drawString(PAGE_WIDTH/1.3, PAGE_HEIGHT-45, 'Mob No. : +91-'+data['mobile_no'])
    if 'shop_name' in data.keys():
        canvas.drawString(PAGE_WIDTH/1.3, PAGE_HEIGHT-55, 'Shop Name. : '+data['shop_name'])
    if 'user_no' in data.keys():
        canvas.drawString(PAGE_WIDTH/1.3, PAGE_HEIGHT-65, 'User No. : '+str(data['user_no']))
  

    #payment_details
    canvas.setFont('Times-Roman',9)
    canvas.setLineWidth(.3)
    canvas.line(10,PAGE_HEIGHT-75, (PAGE_WIDTH/2.0)-15, PAGE_HEIGHT-75)
    canvas.drawString(10,PAGE_HEIGHT-85,'SL NO.')
    canvas.drawString(1.8*cm,PAGE_HEIGHT-85,'Date')
    canvas.drawString(3*cm,PAGE_HEIGHT-85,'Rate')
    canvas.drawString(4.2*cm,PAGE_HEIGHT-85,'AD.')
    canvas.drawString(5.6*cm,PAGE_HEIGHT-85,'Amount')
    canvas.drawString(7.5*cm,PAGE_HEIGHT-85,'Collected By')
    canvas.line(10,PAGE_HEIGHT-90, (PAGE_WIDTH/2.0)-15, PAGE_HEIGHT-90)

    canvas.line((PAGE_WIDTH/2.0)+10,PAGE_HEIGHT-75,PAGE_WIDTH-15, PAGE_HEIGHT-75)
    canvas.drawString((PAGE_WIDTH/2.0)+10,PAGE_HEIGHT-85,'SL NO.')
    canvas.drawString((PAGE_WIDTH/2.0)+1.8*cm,PAGE_HEIGHT-85,'Date')
    canvas.drawString((PAGE_WIDTH/2.0)+3*cm,PAGE_HEIGHT-85,'Rate')
    canvas.drawString((PAGE_WIDTH/2.0)+4.2*cm,PAGE_HEIGHT-85,'AD.')
    canvas.drawString((PAGE_WIDTH/2.0)+5.6*cm,PAGE_HEIGHT-85,'Amount')
    canvas.drawString((PAGE_WIDTH/2.0)+7.5*cm,PAGE_HEIGHT-85,'Collected By')
    canvas.line((PAGE_WIDTH/2.0)+10,PAGE_HEIGHT-90,PAGE_WIDTH-15, PAGE_HEIGHT-90)

    if "payment" in data.keys():
        sl_no=1
        total_rate=0
        total_amount=0
        leng_of_payment_data=len(data['payment'])
        for payment_data in data['payment']:
            if(sl_no < 51):
                canvas.drawString(18,PAGE_HEIGHT-(88+(14*sl_no)),str(sl_no))
                if 'date' in payment_data.keys():
                    canvas.drawString(1.3*cm,PAGE_HEIGHT-(88+(14*sl_no)),payment_data['date'])
                if 'rate' in payment_data.keys():
                    canvas.drawString(3*cm,PAGE_HEIGHT-(88+(14*sl_no)),str(payment_data['rate']))
                    total_rate+=payment_data['rate']
                if 'ad' in payment_data.keys():
                    canvas.drawString(4.2*cm,PAGE_HEIGHT-(88+(14*sl_no)),str(payment_data['ad']))
                if 'amount' in payment_data.keys():
                    canvas.drawString(5.6*cm,PAGE_HEIGHT-(88+(14*sl_no)),str(payment_data['amount']))
                    total_amount+=payment_data['amount']
                if 'collected_by' in payment_data.keys():
                    canvas.drawString(7.6*cm,PAGE_HEIGHT-(88+(14*sl_no)),payment_data['collected_by'])
                canvas.line(10,PAGE_HEIGHT-(90+(14*sl_no)), (PAGE_WIDTH/2.0)-15, PAGE_HEIGHT-(90+(14*sl_no)))
                if(sl_no==leng_of_payment_data):
                    canvas.drawString(18,PAGE_HEIGHT-(88+(14*sl_no)),'Total Rate')
                    canvas.drawString(3*cm,PAGE_HEIGHT-(88+(14*sl_no)),str(total_rate))
                    canvas.drawString(5.6*cm,PAGE_HEIGHT-(88+(14*sl_no)),'Total Amount')
                    canvas.drawString(7.6*cm,PAGE_HEIGHT-(88+(14*sl_no)),str(total_amount))
            else:
                canvas.drawString((PAGE_WIDTH/2.0)+18,PAGE_HEIGHT-(88+(14*(sl_no-50))),str(sl_no))
                if 'date' in payment_data.keys():
                    canvas.drawString((PAGE_WIDTH/2.0)+1.3*cm,PAGE_HEIGHT-(88+(14*(sl_no-50))),payment_data['date'])
                if 'rate' in payment_data.keys():
                    canvas.drawString((PAGE_WIDTH/2.0)+3*cm,PAGE_HEIGHT-(88+(14*(sl_no-50))),str(payment_data['rate']))
                    total_rate+=payment_data['rate']
                if 'ad' in payment_data.keys():
                    canvas.drawString((PAGE_WIDTH/2.0)+4.2*cm,PAGE_HEIGHT-(88+(14*(sl_no-50))),str(payment_data['ad']))
                if 'amount' in payment_data.keys():
                    canvas.drawString((PAGE_WIDTH/2.0)+5.6*cm,PAGE_HEIGHT-(88+(14*(sl_no-50))),str(payment_data['amount']))
                    total_amount+=payment_data['amount']
                if 'collected_by' in payment_data.keys():
                    canvas.drawString((PAGE_WIDTH/2.0)+7.6*cm,PAGE_HEIGHT-(88+(14*(sl_no-50))),payment_data['collected_by'])
                canvas.line((PAGE_WIDTH/2.0)+10,PAGE_HEIGHT-(90+(14*(sl_no-50))), PAGE_WIDTH-15, PAGE_HEIGHT-(90+(14*(sl_no-50))))
                if(sl_no==leng_of_payment_data):
                    sl_no+=1
                    canvas.setFont('Times-Bold',10)
                    canvas.drawString((PAGE_WIDTH/2.0)+18,PAGE_HEIGHT-(88+(14*(sl_no-50))),'Total Rate :')
                    canvas.drawString((PAGE_WIDTH/2.0)+5.2*cm,PAGE_HEIGHT-(88+(14*(sl_no-50))),'Total Amount :')
                    canvas.setFillColorRGB(255,0,0)
                    canvas.drawString((PAGE_WIDTH/2.0)+7.8*cm,PAGE_HEIGHT-(88+(14*(sl_no-50))),str(total_amount))
                    canvas.drawString((PAGE_WIDTH/2.0)+3*cm,PAGE_HEIGHT-(88+(14*(sl_no-50))),str(total_rate))
            sl_no+=1


def invoice_generator(invoice_name,data):
    c = canvas.Canvas(invoice_name+".pdf")
    user_invoice_generator(c,data)
    c.showPage()
    c.save()