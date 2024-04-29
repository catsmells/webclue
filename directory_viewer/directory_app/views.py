from django.shortcuts import render
from .forms import URLForm
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

def directory_view(request):
    directories = None
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            website = form.save()
            url = website.url
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                directories = {urlparse(url).netloc: []}
                for link in soup.find_all('a'):
                    href = link.get('href')
                    if href.endswith('/'):
                        directories[urlparse(url).netloc].append(href)
    else:
        form = URLForm()
    return render(request, 'directory_app/directory_view.html', {'form': form, 'directories': directories})
