from django.shortcuts import render
from .models import InformationBox, Feedback, DailyQuote


def index(request):
    information_boxs = InformationBox.get_all_information_box()
    feedback = Feedback.get_all_feedback()
    daily_quote = DailyQuote.get_today_daily_quote()
    data = {'InformationBox': information_boxs, 'Feedback': feedback, 'DailyQuote': daily_quote}
    return render(request, 'main/index.html', data)


def contact_us(request):
    return render(request, 'main/contact_us.html')
