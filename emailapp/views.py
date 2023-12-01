# emailapp/views.py

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Email
from django.views.decorators.http import require_POST


@require_POST
def delete_email(request):
    try:
        email_id = request.POST.get('email_id')
        email = Email.objects.get(pk=email_id)
        email.delete()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})


def index(request):
    return render(request, 'emailapp/index.html')


def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        recipient = request.POST.get('recipient', '')

        try:
            # Send the email
            send_mail(subject, message, 'your_email@example.com', [recipient])

            # Save the email to the database
            Email.objects.create(
                subject=subject,
                message=message,
                recipient=recipient
            )

            response_data = {'success': True,
                             'message': 'Email sent and saved successfully!'}
        except Exception as e:
            response_data = {'success': False,
                             'message': f'Error sending email: {str(e)}'}

        return JsonResponse(response_data)

    return render(request, 'emailapp/send_email.html')


def view_emails(request):
    emails = Email.objects.all()
    return render(request, 'emailapp/view_emails.html', {'emails': emails})
