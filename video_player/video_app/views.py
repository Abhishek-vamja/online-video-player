from django.shortcuts import render, redirect, get_object_or_404
from video_app.models import *
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login, authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from user.models import User


class ARVideoPlayer(LoginRequiredMixin):
    """
    The ARVideoPlayer class encapsulates views related to the AR Video Player application,
    providing functionality for rendering various pages and handling video-related operations. 
    Here's a breakdown of its responsibilities:
    """

    def home_view(request):
        """
        Renders the home page of the AR Video Player application, 
        displaying categories of videos with pagination.
        """
        prod_obj = Category.objects.all()

        items_per_page = 12

        # Paginate the product data
        paginator = Paginator(prod_obj, items_per_page)
        page = request.GET.get('page', 1)

        try:
            product_data = paginator.page(page)
        except PageNotAnInteger:
            product_data = paginator.page(1)
        except EmptyPage:
            product_data = paginator.page(paginator.num_pages)

        context = {
            'product': product_data,
        }
        return render(request, 'index.html', context)

    def about_view(request):
        """
        Renders the about page providing information about 
        the AR Video Player application.
        """
        return render(request, 'about.html')

    def contact_view(request):
        """
        Renders the contact page for the AR Video Player application.
        """
        return render(request, 'contact.html')

    def search(request):
        """
        Handles the search functionality, allowing users to search for videos based on category title,
        category slug, or video slug. Displays paginated search results.
        """
        query = request.GET.get('q', '')  # Get the search query from the URL parameter
        results = Product.objects.filter(
            Q(category__title__icontains=query) | Q(category__slug__icontains=query) | Q(slug__icontains=query)
        )

        items_per_page = 8

        # Paginate the product data
        paginator = Paginator(results, items_per_page)
        page = request.GET.get('page', 1)

        try:
            product_data = paginator.page(page)
        except PageNotAnInteger:
            product_data = paginator.page(1)
        except EmptyPage:
            product_data = paginator.page(paginator.num_pages)

        context = {
            'query': query,
            'results': product_data,
        }
        return render(request, 'search.html', context)

    def show_video(request, category_slug):
        """
        Displays a list of videos belonging to a specific category, 
        with pagination for a better user experience.
        """
        cat_obj = get_object_or_404(Category, slug=category_slug)
    
        pro_obj = Product.objects.filter(category=cat_obj)

        items_per_page = 8

        # Paginate the product data
        paginator = Paginator(pro_obj, items_per_page)
        page = request.GET.get('page', 1)

        try:
            product_data = paginator.page(page)
        except PageNotAnInteger:
            product_data = paginator.page(1)
        except EmptyPage:
            product_data = paginator.page(paginator.num_pages)
        
        context = {
            'product': product_data,
            'category': cat_obj.title,
        }
        
        return render(request, 'videos.html', context)

    def show_single_video(request, category_slug, product_slug):
        """
        Displays detailed information about a single video, 
        including its category and other relevant details.
        """
        prod_obj = Product.objects.get(slug=product_slug,category__slug=category_slug)

        context = {
            'product': prod_obj
        }
        return render(request, 'video-detail.html',context)


class UserAuth:
    """
    The UserAuth class manages user authentication operations within the AR Video Player application, 
    including login, registration, and logout. Here's an overview of its functions:
    """

    def user_login(request):
        """
        Handles user authentication for login, allowing users to log in using their email and password.
        Redirects authenticated users to the home page.
        """
        if request.user.is_authenticated:
            return redirect('index')

        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request,user)
                return redirect('index')

            else:
                return render(request, 'login.html')

        return render(request, 'login.html')
    
    def user_register(request):
        """
        Handles user registration, creating a new user with provided email, name, and password. 
        Logs in the newly registered user and redirects them to the home page.
        """
        if request.method == 'POST':
            email = request.POST.get('email')
            name = request.POST.get('name')
            password = request.POST.get('password')

            user = User.objects.create_user(
                email=email,name=name,password=password
            )
            user.save()

            if user:
                login(request,user)
                return redirect('index') 

            return redirect('index')
        
        return render(request, 'register.html')

    def user_logout(request):
        """
        Logs out the currently authenticated user and redirects them to the home page.
        """
        logout(request)
        return redirect('index')