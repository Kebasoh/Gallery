from django.shortcuts import render
import datetime as dt
from .models import Images
# from django.http  import HttpResponse
from django.http  import HttpResponse,Http404

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def gallery_of_day(request):
    date = dt.date.today()
    # gallery = images.todays_gallery()

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
    
    # gallery = images.days_gallery(date)

    return render(request, 'gallery/past-gallery.html', {"date": date,})


def search_results(request):
    
    if 'Images' in request.GET and request.GET["Images"]:
        search_term = request.GET.get("Images")
        searched_Images = Images.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'gallery/search.html',{"message":message,"Images": searched_Images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'gallery/search.html',{"message":message})
