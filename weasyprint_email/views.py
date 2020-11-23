import weasyprint
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from emails.models import Email

product_model = [
    {'name': 'BLUE OX',
     'atlas_number': '1271-7',
     'vendorNum': '1',
     'vendorId': '1',
     'productId': '1',
     'product': '1',
     'storeId': '1',
     'status': '1',
     'regularPrice': '749.00',
     'specialPrice': '539.00',
     'description': '1',
     'assortment_benchmark': 12}
]


def index_view(request):
    return render(request, 'index.html', {'products': product_model})


def email_pdf(request):
    queryset = product_model
    html = render_to_string('pdf.html', {'products': queryset})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = "filename='order_{}.pdf'".format('file_name')
    weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS('static/css/pdf.css')])

    # obj = Email.objects.get(id=instance_id)
    # context = {'instance': obj}
    # pdf = render_to_pdf('your/pdf/template.html', context)
    # filename = "YourPDF_Order{}.pdf" % (obj.slug)
    # obj.pdf.save(filename, File(BytesIO(pdf.content)))

    # print(html)

    # pdf = response['Content-Disposition']
    # to_emails = ['ishaq@gmail.com']
    # subject = "EMAIL FROM ATLAS"
    # email = EmailMessage(subject, body=pdf, from_email='attaazd@gmail.com', to=to_emails)
    # email.attach('Ishaq Muhammed' + '.pdf', pdf, "application/pdf")
    # email.content_subtype = "pdf"
    # email.encoding = 'us-ascii'
    # email.send()

    # Write PDF to file
    # document_html = HTML(string=html, base_url=request.build_absolute_uri())
    # document = document_html.render()
    # if len(document.pages) > 1:
    #     for page in document.pages[1:]:
    #         str(page)
    #     pdf = document.write_pdf()
    # else:
    #     pdf = document.write_pdf()
    # # response = HttpResponse(html)
    # response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'filename="Invoice {0} | Invoice {0}.pdf"'.format(self.id)


    return response
