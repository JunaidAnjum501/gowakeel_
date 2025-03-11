from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Blogs, BlogCategory, VideoCategory, Videos


def index(request):
    services = [
        {"slug":"NTN-Registration", "name": "NTN Registration", "price": "500 PKR", "image": "wakeelapp/Img/NTNRegistraion.png"},
        {"slug":"Annual-Income-Tax-Return-(Salary)", "name": "Annual Income Tax Return (Salary)", "price": "3000 PKR", "image": "wakeelapp/Img/annualtaxsalary.png"},
        {"slug":"Annual-Income-Tax-Return-(Business)", "name": "Annual Income Tax Return (Business)", "price": "5000 PKR", "image": "wakeelapp/Img/annualtaxbus.png"},
        {"slug":"GST-Registration", "name": "GST Registration", "price": "5000 PKR", "image": "wakeelapp/Img/gst.png"},
        {"slug":"Monthly-Sales-Tax-Return-Filing", "name": "Monthly Sales Tax Return Filing", "price": "5000 PKR", "image": "wakeelapp/Img/monthly.png"},
        {"slug":"Company-Registration", "name": "Company Registration", "price": "Starting 15000 PKR", "image": "wakeelapp/Img/companyregistration.png"},
        {"slug":"Trade-Marks-&-Partnership", "name": "Trade Marks & Partnership", "price": "Starting 15000 PKR", "image": "wakeelapp/Img/Trademarks.png"},
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

def about(request):
    return render(request, 'wakeelapp/about.html')

def usaservice(request):
    return render(request, 'wakeelapp/usaservices.html')

def login(request):
    return render(request, 'wakeelapp/login.html')

def zakatcalculator(request):
    return render(request, 'wakeelapp/zakatcalculator.html')

def currencyconvert(request):
    return render(request, 'wakeelapp/currencyconvert.html')


def blogdetail(request, blogs_slug):
    try:
        blog = Blogs.objects.get(slug=blogs_slug)
        from icecream import ic
        ic(blogs)
        blogs = Blogs.objects.all().order_by('-created_at')[:3]
    
    except:
        blog = None
        blogs = None

    context = {
        'blog': blog,
        'blogs': blogs,
    }


    return render(request, 'wakeelapp/blogdetail.html', context)

def blogs(request):
    # Fetch all blogs and order by 'created_at'
    blogs_list = Blogs.objects.all().order_by("-created_at")
    categories = BlogCategory.objects.values("name")

    paginator = Paginator(blogs_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "blogs": page_obj,
        "categories": categories
    }

    return render(request, 'wakeelapp/blogs.html', context)


def video(request):
     # Fetch all blogs and order by 'created_at'
    video_list = Videos.objects.all().order_by("-created_at")
    categories = VideoCategory.objects.values("name")

    paginator = Paginator(video_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "videos": page_obj,
        "categories": categories
    }
    return render(request, 'wakeelapp/video.html', context)



def service_detail(request, service_name):
    services = {
        "NTN-Registration": {
            "description": "Get your Individual NTN in just 3 simple steps.",
            "price": "Rs:500/-",
            "requirements": [
            "Color copy of CNIC",
            "Latest paid electricity bill",
            "Phone Number",
            "Email address",
          ],
            
        },
        "Annual-Income-Tax-Return-(Salary)": {
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
        "Annual-Income-Tax-Return-(Business)": {
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
        "GST-Registration": {
            "description": "Start your business legally with ease.",
            "price": "Rs:5000/-",
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
        "Monthly-Sales-Tax-Return-Filing": {
            "description": "Start your business legally with ease.",
            "price": "Rs:5000/-",
            "requirements": ["Business Name", "CNIC Copy", "Bank Account", "Office Address"],
            
        },
        "Company-Registration": {
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
        "Trade-Marks-&-Partnership": {
            "description": "Start your business legally with ease.",
            "price": "Starting From Rs:15000/-",
            "requirements": ["Business Name", "CNIC Copy", "Bank Account", "Office Address"],
            
        },
    }

    service = services.get(service_name, None)
    
    if service is None:
        return render(request, "404.html", status=404)

    return render(request, "wakeelapp/service_detail.html", {"service": service, "service_name": service_name})



