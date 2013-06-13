from django.conf import settings

class PayPalSettingsError(Exception):
    """Raised when settings be bad."""
    

TEST = getattr(settings, "PAYPAL_TEST", True) # is this even used?


RECEIVER_EMAIL = settings.PAYPAL_RECEIVER_EMAIL


# API Endpoints.
POSTBACK_ENDPOINT = "https://www.paypal.com/cgi-bin/webscr"
SANDBOX_POSTBACK_ENDPOINT = "https://www.sandbox.paypal.com/cgi-bin/webscr"

# Images
DONT_USE_IMAGE = getattr(settings, "PAYPAL_DONT_USE_IMAGE", False)
IMAGE = getattr(settings, "PAYPAL_IMAGE", "http://images.paypal.com/images/x-click-but01.gif")
SUBSCRIPTION_IMAGE = getattr(settings, "PAYPAL_SUBSCRIPTION_IMAGE", "https://www.paypal.com/en_US/i/btn/btn_subscribeCC_LG.gif")
DONATION_IMAGE = getattr(settings, "PAYPAL_DONATION_IMAGE", "https://www.paypal.com/en_US/i/btn/btn_donateCC_LG.gif")
SANDBOX_IMAGE = getattr(settings, "PAYPAL_SANDBOX_IMAGE", "https://www.sandbox.paypal.com/en_US/i/btn/btn_buynowCC_LG.gif")
SUBSCRIPTION_SANDBOX_IMAGE = getattr(settings, "PAYPAL_SUBSCRIPTION_SANDBOX_IMAGE", "https://www.sandbox.paypal.com/en_US/i/btn/btn_subscribeCC_LG.gif")
DONATION_SANDBOX_IMAGE = getattr(settings, "PAYPAL_DONATION_SANDBOX_IMAGE", "https://www.sandbox.paypal.com/en_US/i/btn/btn_donateCC_LG.gif")

# Also used in a form
BUY = 'buy'
SUBSCRIBE = 'subscribe'
DONATE = 'donate'

# Submit text
SUBMIT_TEXT = {
    BUY: getattr(settings, "PAYPAL_BUY_TEXT", "Buy it Now"),
    DONATE: getattr(settings, "PAYPAL_DONATE_TEXT", "Donate Now"),
    SUBSCRIBE: getattr(settings, "PAYPAL_SUBSCIRBE_TEXT", "Subscribe Now"),
}
