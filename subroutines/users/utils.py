import jwt
from datetime import timedelta

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils import timezone


def gen_verification_token(user):
    """Create JWT to allow user verify his email account."""
    exp_date = timezone.now() + timedelta(days=5)
    payload = {
        "user": user.username,
        "exp": int(exp_date.timestamp()),
        "type": "account_verification",
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    return token.decode()


def send_verification_email(user):
    """Send link to user account verification."""
    verification_token = gen_verification_token(user)
    subject = f"Welcome {user.first_name}"
    from_email = "Dejavu <noreply@dejavuhq.xyz>"
    content = render_to_string(
        "emails/users/account_verification.html",
        {"token": verification_token, "user": user,},
    )
    message = EmailMultiAlternatives(subject, content, from_email, [user.email])
    message.attach_alternative(content, "text/html")
    message.send()
