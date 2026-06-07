from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. Define the names of your public URLs (namespaces included if applicable)
        # Use reverse() or clean string matching to ensure Django recognizes them
        exempt_urls = [
            reverse('login'),
            reverse('register'),
            # add any other public URLs here, like a home page
        ]

        # 2. Check if the current URL path matches any exempt paths
        if request.path in exempt_urls:
            return self.get_response(request)

        # 3. CRITICAL CHECK: If the user is NOT logged in, hijack the request
        if not request.user.is_authenticated:
            # You MUST explicitly return a redirect response here to stop the cycle
            return redirect('login') 

        # 4. If they are logged in, let them move on to the view normally
        response = self.get_response(request)
        return response