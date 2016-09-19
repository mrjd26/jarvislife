from django.shortcuts import render

from django.core.urlresolvers import get_resolver

def home(request):
    allurls = []
    urls = []
    urlpatterns = get_resolver(None).reverse_dict
    urlpatterns_dictionary = dict(urlpatterns.iterlists())
    values = urlpatterns_dictionary.values()
    for value in values:
        if value[0][1] not in allurls:
            allurls.append(value[0][1])

    for url in allurls:
        if url[0].isdigit():
            urls.append(url)

    path = request.path

    if path == '/':
        html_file = 'home.html'
    else:
        html_file = path.replace('/', '-')

        html_file = html_file[1:-1] + '.html'

    return render(request, html_file, {'urls': allurls})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')
