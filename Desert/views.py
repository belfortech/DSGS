from django.shortcuts import render
from .models import ContactMessage, NewsletterSubscriber,Service



def home(request):
    return render (request,"index.html",{'active': 'home'})

def about_us(request):
    return render(request, 'about_us.html', {'active': 'about'})

def our_services(request):
    return render(request, 'our_services.html', {'active': 'services'})

def portfolio(request):
    return render(request, 'portfolio.html', {'active': 'portfolio'})

def blog(request):
    return render(request, 'blog.html', {'active': 'blog'})

def contact_us(request):
    return render(request, 'contact_us.html', {'active': 'contact'})
    

def success(request):
    return render(request, 'success.html')

def our_services(request):
    services = Service.objects.all()
    return render(request, 'our_services.html', {
        'services': services,
        'active': 'services'  
    })


def audit_assurance(request):
    return render(request, 'services/audit-assurance.html')

def quantification_budgeting(request):
    return render(request, 'services/quantification-budgeting.html')

def global_financing(request):
    return render(request, 'services/global-financing.html')

def procurement_audit(request):
    return render(request, 'services/procurement-audit.html')

def psm_planning(request):
    return render(request, 'services/psm-planning.html')

def capacity_building(request):
    return render(request, 'services/capacity-building.html')

def procurement_strategy(request):
    return render(request, 'services/procurement-strategy.html')

def procurement_transformation(request):
    return render(request, 'services/procurement-transformation.html')

def international_business(request):
    return render(request, 'services/international-business.html')










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

