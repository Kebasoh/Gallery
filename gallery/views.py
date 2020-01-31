from django.shortcuts import render
import datetime as dt
# from django.http  import HttpResponse
from django.http  import HttpResponse,Http404

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def gallery_of_day(request):
    date = dt.date.today()

    return render(request, 'gallery/today-gallery.html', {"date": date,})

def past_days_gallery(request, past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(gallery_of_day)

    return render(request, 'gallery/past-gallery.html', {"date": date})
