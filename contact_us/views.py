from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.urls import reverse


class ContactFormView(FormView):
    template_name = "contact/contact_us.html"
    form_class = ContactForm
    success_url = reverse_lazy("thank_you")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def thank_you(request):
    messages.success(request, "Thank you for your message!")
    return redirect(reverse("contact_form"))
