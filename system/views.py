from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.


class LandingPageView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "landing.html"
        self.args = {

        }
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, self.args)


class AboutPageView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "about.html"
        self.args = {

        }
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, self.args)


class ContactPageView(View):
    def dispatch(self, request, *args, **kwargs):
        self.template_name = "contact.html"
        self.args = {

        }
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, self.args)

    def post(self, request):

        try:
            data = request.POST.dict()
            user_email = data['email']
            user_name = data['full_name']
            message = f'''
Message From User
Name: {user_name},
Email Address: {user_email}

Message:
{data['message']}
            '''
            subject = "Message from user at aarchrealestate.com.au"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["sunil.mainali@aarchrealestate.com.au",]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, "Message sent successfully")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        except Exception as e:
            messages.error(
                request, "Sorry! Error sending message, please try again")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
