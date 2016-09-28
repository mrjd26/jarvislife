from django.shortcuts import render

from django.core.urlresolvers import get_resolver

import datetime

def serve_home_or_article(path):

    if path == '/':
        return 'home.html'
    else:
        html_file = path.replace('/', '-')

        return html_file[1:-1] + '.html'

def make_datetime_and_article_context(urls):
    django_context = []

    for url in urls:
        date_object = datetime.datetime(int(url[:4]), int(url[5:7]), int(url[8:10]))
        #string_date = date_object.strftime('%Y-%m-%d')
        article_title = url[11:].replace('/', ' ')
        django_context.append({'date':date_object, 'article_title':article_title, 'url':url})

    return django_context

def home(request):
    urls = []
    clean_urls = []
    urlpatterns = get_resolver(None).reverse_dict
    urlpatterns_dictionary = dict(urlpatterns.iterlists())

    for key, value in urlpatterns_dictionary.iteritems():
        if key.__name__ == 'home':
            urls = value

    for url in urls:
        if url[1][0].isdigit():
            clean_urls.append(url[1])

    html_file = serve_home_or_article(request.path)

    django_context = make_datetime_and_article_context(clean_urls)

    return render(request, html_file, {'date_and_title': django_context})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')
