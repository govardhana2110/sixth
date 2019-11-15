from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import csv
data="""<tabel border="2"><tr><th>eid</th><th>ename</th><th>esal</th></tr><tr><td>1001</td><td>govardhan</td><td>2000</td></tr><tr><td>2001</td><td>ramesh</td><td>1500</td></tr><tr><td>1003</td><td>harinath</td><td>2500</td></tr></table>"""
def csvview(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;' \
                                    'filename="myfile.csv"'
    writer=csv.writer(response)
    writer.writerow(['first row','Foo','Bar','Bar','Baz'])
    writer.writerow(['second row','A','B','C','"testing"',"here's a quote"])
    return response
def pdfview(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']= \
        'favattachment; filename="myfile.pdf"'
    p=canvas.Canvas(response)
    p.drawString(100,100,"hello world")
    p.showPage()
    p.save()
    return response
def htmlview(request):
    return HttpResponse(data,content_type="text/html")
def xmlview(request):
    return HttpResponse(data,content_type="application/xml")

