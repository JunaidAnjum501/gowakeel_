from django.shortcuts import render

# Create your views here.


def index(request):
    services = [
        {"name": "NTN Registration", "price": "500 PKR", "image": "wakeelapp/Img/ntnregis.jpg"},
        {"name": "Annual Income Tax Return (Salary)", "price": "3000 PKR", "image": "images/tax-salary.jpg"},
        {"name": "Annual Income Tax Return (Business)", "price": "5000 PKR", "image": "images/tax-business.jpg"},
        {"name": "GST Registration", "price": "Contact for Price", "image": "images/gst.jpg"},
        {"name": "Monthly Sales Tax Return Filing", "price": "Contact for Price", "image": "static/wakeelapp/Img/blogs.png"},
        {"name": "Company Registration", "price": "Starting 15000 PKR", "image": "images/company.jpg"},
        {"name": "Trade Marks & Partnership", "price": "Starting 15000 PKR", "image": "images/trademark.jpg"},
    ]

    
    context = {'services': services}

    return render(request, 'wakeelapp/index.html', context)


def calculator(request):
    return render(request, 'wakeelapp/cal.html')


def atl(request):
    return render(request, 'wakeelapp/active_tax_list.html')

def ntn(request):
    return render(request, 'wakeelapp/ntn.html')

def faq(request):
    return render(request, 'wakeelapp/faq.html')

def contact(request):
    return render(request, 'wakeelapp/contact.html')

def service_card(request):
    return render(request, 'wakeelapp/service_card.html')

def blogs(request):
    return render(request, 'wakeelapp/blogs.html')

def video(request):
    return render(request, 'wakeelapp/video.html')

def about(request):
    return render(request, 'wakeelapp/about.html')

from django.shortcuts import render

def service_detail(request, service_name):
    services = {
        "NTN Registration": {
            "description": "Get your Individual NTN in just 3 simple steps.",
            "price": "Rs:500/-",
            "requirements": [
            "Color copy of CNIC",
            "Latest paid electricity bill",
            "Phone Number",
            "Email address",
          ],
            
        },
        "Annual Income Tax Return (Salary)": {
            "description": "File your tax returns without any hassle.",
            "price": "Rs:3000/-",
            "requirements": [
            "Color copy of CNIC",
            "Annual Salary certificate",
            "Other Income sources if any",
            "Annual personal expense",
            "Details of all owned assets",
            "Investments during the year",
            "Disposals during the year",
            "Other inflows/outflows during the year",
            "Other information as required",
          ],
            
        },
        "Annual Income Tax Return (Business)": {
            "description": "Start your business legally with ease.",
            "price": "Rs:5000/-",
            "requirements": [
            "Color copy of CNIC",
            "Annual Accounts",
            "Other Income sources if any",
            "Annual personal expense",
            "Details of all owned assets",
            "Investments during the year",
            "Disposals during the year",
            "Other inflows/outflows during the year",
            "Other information as required",
          ],
            
        },
        "GST Registration": {
            "description": "Start your business legally with ease.",
            "price": "$150",
            "requirements": [
            "Color copy of CNIC's of Partners",
            "Bank Account Certificate",
            "Acquisition Date, Capacity and Business Activity",
            "Particulars of all branches (if any)",
            "Authorization of principal Officer",
            "GPS-tagged photographs of the business premises",
            "Consumer number with the gas and electricity supplier along with pictures of utilities meter",
            "GPS-tagged photographs of machinery and industrial electricity or gas meter installed",
            "Rent agreement/ownership docs of Office premises",
            "Latest paid electricity bill",
            "Biometric Verification",
            "Post Verification",
          ],
            
        },
        "Monthly Sales Tax Return Filing": {
            "description": "Start your business legally with ease.",
            "price": "$150",
            "requirements": ["Business Name", "CNIC Copy", "Bank Account", "Office Address"],
            
        },
        "Company Registration": {
            "description": "Start your business legally with ease.",
            "price": "Starting From Rs:15000/-",
            "requirements": [
            "Incorporation Certificate",
            "Memorandum of Association",
            "Articles of Association",
            "Incorporation Form/ Form A & 29",
            "Color copy of CNIC",
            "Rent agreement/ownership docs of Office premises",
            "Letterhead",
            "Latest paid electricity bill",
            "Phone Number",
            "Email address",
            "Bank Account Certificate",
            "Acquisition Date, Capacity and Business Activity",
            "Particulars of all branches (if any)",
            "Authorization of principal Officer",
            "Signed Application Form",
          ],
            
        },
        "Trade Marks & Partnership": {
            "description": "Start your business legally with ease.",
            "price": "Starting From Rs:7500/-",
            "requirements": ["Business Name", "CNIC Copy", "Bank Account", "Office Address"],
            
        },
    }

    service = services.get(service_name, None)
    print("Data Validation", service)
    if service is None:
        return render(request, "404.html", status=404)

    return render(request, "wakeelapp/service_detail.html", {"service": service, "service_name": service_name})



