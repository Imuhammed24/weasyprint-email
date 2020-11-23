import weasyprint
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

product_model = {
    '1': {
        'name': 'BLUE OX',
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
        'assortment_benchmark': 12},

    '2': {
        'name': 'BLUE OX',
        'atlas_number': '1271-8',
        'vendorNum': '1',
        'vendorId': '1',
        'productId': '1',
        'product': '1',
        'storeId': '1',
        'status': '1',
        'regularPrice': '749.00',
        'specialPrice': '539.00',
        'description': '1',
        'assortment_benchmark': 12},

    '3': {
        'name': 'CANADIAN RV MATS',
        'atlas_number': '1626-2',
        'vendorNum': '1',
        'vendorId': '1',
        'productId': '1',
        'product': '1',
        'storeId': '1',
        'status': '1',
        'regularPrice': '29.90',
        'specialPrice': '19.95',
        'description': '1',
        'assortment_benchmark': 12},

    '4': {
        'name': 'CANADIAN RV MATS',
        'atlas_number': '1626-5',
        'vendorNum': '1',
        'vendorId': '1',
        'productId': '1',
        'product': '1',
        'storeId': '1',
        'status': '1',
        'regularPrice': '39.90',
        'specialPrice': '28.95',
        'description': '1',
        'assortment_benchmark': 10},

    '5': {
        'name': 'CANADIAN RV MATS',
        'atlas_number': '1626-6',
        'vendorNum': '1',
        'vendorId': '1',
        'productId': '1',
        'product': '1',
        'storeId': '1',
        'status': '1',
        'regularPrice': '39.90',
        'specialPrice': '28.95',
        'description': '1',
        'assortment_benchmark': 10},

    '6': {
        'name': 'CANADIAN RV MATS',
        'atlas_number': '1629-1',
        'vendorNum': '1',
        'vendorId': '1',
        'productId': '1',
        'product': '1',
        'storeId': '1',
        'status': '1',
        'regularPrice': '59.90',
        'specialPrice': '46.95',
        'description': '1',
        'assortment_benchmark': 24},

    '7': {
        'name': 'CREATIVE PRODUCTS',
        'atlas_number': '203-8',
        'vendorNum': '1',
        'vendorId': '1',
        'productId': '1',
        'product': '1',
        'storeId': '1',
        'status': '1',
        'regularPrice': '37.50',
        'specialPrice': '24.95',
        'description': '1',
        'assortment_benchmark': 24},

    '8': {
        'name': 'GCI OUTDOOR',
        'atlas_number': '1625-6',
        'vendorNum': '1',
        'vendorId': '1',
        'productId': '1',
        'product': '1',
        'storeId': '1',
        'status': '1',
        'regularPrice': '79.50',
        'specialPrice': '59.95',
        'description': '1',
        'assortment_benchmark': 4},

    '9': {
        'name': 'GCI OUTDOOR',
        'atlas_number': '1625-22',
        'vendorNum': '1',
        'vendorId': '1',
        'productId': '1',
        'product': '1',
        'storeId': '1',
        'status': '1',
        'regularPrice': '54.50',
        'specialPrice': '39.95',
        'description': '1',
        'assortment_benchmark': 4},

    '10': {
        'name': 'GCI OUTDOOR',
        'atlas_number': '1625-23',
        'vendorNum': '1',
        'vendorId': '1',
        'productId': '1',
        'product': '1',
        'storeId': '1',
        'status': '1',
        'regularPrice': '49.50',
        'specialPrice': '34.95',
        'description': '1',
        'assortment_benchmark': 4},
}


def index_view(request):
    return render(request, 'index.html', {'products': product_model})


def email_pdf(request):
    queryset = product_model
    html = render_to_string('pdf.html', {'products': queryset})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = "filename='order_{}.pdf'".format('file_name')
    weasyprint.HTML(string=html).write_pdf(response,
                                           stylesheets=[weasyprint.CSS('static/css/pdf.css')])
    return response
