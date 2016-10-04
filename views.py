from django.shortcuts import render

from django.core.urlresolvers import get_resolver

import datetime

def remove_html_tags(taglist):
    import re
    string = str(taglist[0])
    m = re.findall ( '<(.*?)>', string, re.DOTALL)
    for tag in m:
       string = string.replace('<' + tag + '>', '')
    string = string[:250] + '...'
    return string

def make_datetime_and_article_context(urls, calling_method):
    django_context = []
    first_p = None
    first_image = None
    cleaned_first_p = None

    for url in urls:
        date_object = datetime.datetime(int(url[:4]), int(url[5:7]), int(url[8:10]))
        article_title = url[11:].replace('/', ' ')
        
        html_file = url.replace('/', '-')
        html = html_file[:-1] + '.html'

        if calling_method == "home":
            import BeautifulSoup as bs
            soup = bs.BeautifulSoup(open("/home/mrjd26/mysite/static/" + html))

            first_image = soup.img['src']

            first_p = soup.findAll('p', {'class':'first'})
            
            cleaned_first_p = remove_html_tags(first_p)

        django_context.append(
                                 {
                                     'date': date_object, 
                                     'article_title': article_title,
                                     'url': url,
                                     'first_image':first_image,
                                     'first_p': cleaned_first_p
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

    django_context = make_datetime_and_article_context(clean_urls, 'serve_article')

    path = request.path
    html_file = path.replace('/', '-')
    html = html_file[1:-1] + '.html'

    return render(request, html, {'date_and_title': django_context})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def store(request):
    return render(request, 'store.html')

def privacy_policy(request):
    return render(request, 'privacy-policy.html')
