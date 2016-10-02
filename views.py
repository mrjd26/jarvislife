from django.shortcuts import render

from django.core.urlresolvers import get_resolver

import datetime

def make_datetime_and_article_context(urls, calling_method):
    django_context = []

    for url in urls:
        date_object = datetime.datetime(int(url[:4]), int(url[5:7]), int(url[8:10]))
        article_title = url[11:].replace('/', ' ')

        if calling_method == "home":
            html_file = url.replace('/', '-')
            html = html_file[:-1] + '.html'
            import BeautifulSoup as bs
            soup = bs.BeautifulSoup(open("/home/mrjd26/mysite/static/" + html))

            first_image = soup.img['src']

            first_p = soup.findAll('p', {'class':'first'})

        django_context.append(
                                 {
                                     'date': date_object, 
                                     'article_title': first_p,
                                     'url': url,
                                     'output':first_image

                                 },
                             )

    return django_context

def get_url_list():

    urls = []
    clean_urls = []
    urlpatterns = get_resolver(None).reverse_dict
    urlpatterns_dictionary = dict(urlpatterns.iterlists())

    for key, value in urlpatterns_dictionary.iteritems():
        if key.__name__ == 'serve_article':
            urls = value

    for url in urls:
        if url[1][0].isdigit():
            clean_urls.append(url[1])

    return clean_urls

def home(request):

    clean_urls = get_url_list()

    django_context = make_datetime_and_article_context(clean_urls, 'home')
 
    return render(request, "home.html", {'date_and_title': django_context})

def serve_article(request):

    clean_urls = get_url_list()

    path = request.path
    html_file = path.replace('/', '-')
    html_file[1:-1] + '.html'

    django_context = make_datetime_and_article_context(clean_urls, 'serve_article')

    return render(request, html_file, {'date_and_title': django_context})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def store(request):
    return render(request, 'store.html')
