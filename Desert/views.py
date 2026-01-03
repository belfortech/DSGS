from django.shortcuts import render, get_object_or_404
from .models import ContactMessage, NewsletterSubscriber



def home(request):
    return render (request,"index.html",{'active': 'home'})

def about_us(request):
    return render(request, 'about_us.html', {'active': 'about'})

def portfolio(request):
    return render(request, 'portfolio.html', {'active': 'portfolio'})

def blog(request):
    return render(request, 'blog.html', {'active': 'blog'})

def contact_us(request):
    return render(request, 'contact_us.html', {'active': 'contact'})


def success(request):
    return render(request, 'success.html')

# Hardcoded services data
SERVICES = [
    {
        'title': 'Public Procurement Strategy and Advisory',
        'slug': 'public-procurement-strategy-and-advisory',
        'description': 'Comprehensive advisory services for public procurement, including strategy development, policy formulation, and implementation guidance to ensure compliance, efficiency, and value-for-money in procurement processes.',
        'image': 'img/public_procurement.jpg',
        'category': 'Advisory'
    },
    {
        'title': 'Procurement Capacity Building And Training',
        'slug': 'procurement-capacity-building-and-training',
        'description': 'Training programs designed to build procurement capacity, enhance skills, and improve knowledge among procurement professionals, stakeholders, and organizations.',
        'image': 'img/investment.jpg',
        'category': 'Capacity'
    },
    {
        'title': 'PSM Planning',
        'slug': 'psm-planning',
        'description': 'Strategic planning for Procurement and Supply Management (PSM), including forecasting, budgeting, and resource allocation to optimize procurement operations.',
        'image': 'img/psm.jpg',
        'category': 'PSM'
    },
    {
        'title': 'Procurement Transformation',
        'slug': 'procurement-transformation',
        'description': 'Transforming procurement processes through digitalization, process re-engineering, and organizational change management to achieve operational excellence.',
        'image': 'img/procurement_transformation.jpg',
        'category': 'Transformation'
    },
    {
        'title': 'Audit and Assurance',
        'slug': 'audit-and-assurance',
        'description': 'Independent, compliance-first audits that add strategic value, including financial audits, operational audits, and risk assessments.',
        'image': 'img/audit_assurance.jpg',
        'category': 'Assurance'
    },
    {
        'title': 'Quantification and Budgeting',
        'slug': 'quantification-and-budgeting',
        'description': 'Quantification of procurement needs and budgeting services to ensure accurate forecasting, resource planning, and financial management.',
        'image': 'img/quantification_2.jpg',
        'category': 'Planning'
    },
    {
        'title': 'Global Financing, Sourcing and Negotiation Consultancy',
        'slug': 'global-financing-sourcing-and-negotiation-consultancy',
        'description': 'Global consultancy services for financing, sourcing, and negotiation to secure favorable terms, optimize costs, and expand market reach.',
        'image': 'img/african_finance_consulting.jpg',
        'category': 'Financing'
    },
    {
        'title': 'Procurement Audit and Compliance Reviews',
        'slug': 'procurement-audit-and-compliance-reviews',
        'description': 'Comprehensive audits and compliance reviews of procurement processes to ensure adherence to regulations, policies, and best practices.',
        'image': 'img/procurement_2.jpg',
        'category': 'Compliance'
    },
    {
        'title': 'International Business Opportunities',
        'slug': 'international-business-opportunities',
        'description': 'Exploring and facilitating international business opportunities, including market entry strategies, partnerships, and expansion planning.',
        'image': 'img/international_business_opportunities.jpg',
        'category': 'Markets'
    }
]

def our_services(request):
    return render(request, 'our_services.html', {
        'services': SERVICES,
        'active': 'services'
    })

def service_detail(request, slug):
    service = next((s for s in SERVICES if s['slug'] == slug), None)
    if not service:
        from django.http import Http404
        raise Http404("Service not found")
    return render(request, 'service_detail.html', {
        'service': service,
        'active': 'services'
    })










def newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        print("Newsletter subscription:", email)

        if email:
            subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)


        messages.success(request, "Thank you for subscribing!")
        return redirect('contact_us')  # corrected here!
    return redirect('contact_us')






from django.shortcuts import render, redirect
from django.contrib import messages  # very important!

from .models import ContactMessage
from django.core.mail import send_mail

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print("Form received:", name, email, subject, message)

        if name and email and subject and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            full_message = f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}"
            send_mail(
                subject=f"New Contact Message from {name}",
                message=full_message,
                from_email=email,  # who sent the email (user)
                recipient_list=['charitymuthoka2019@gmail.com'],  # 🔥 your own email to receive the notification
                fail_silently=False,
            )



        messages.success(request, "Thanks for contacting us! We will get back to you soon.")
        return redirect('contact_us')  # redirect, not render

    return render(request, 'contact_us.html')

