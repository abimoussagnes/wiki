from django.shortcuts import render
from . import util
import markdown2
from random import choice


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def new(request):
    return render(request, "encyclopedia/new_page.html")

def create_entry(request):
    if request.method == 'POST':
        #Retrieve what the user typed in the input fields
        title = request.POST.get("title")
        content = request.POST.get("markdown_content")
        
        #Check if the title already exists
        entries = util.list_entries()
        for entry in entries:
            if title.lower() == entry.lower():
                return render(request, "encyclopedia/page_exists.html")
            
        #Save the entry and show the new entry page to the user
        util.save_entry(title, content)
        html = markdown2.markdown(content)
        return render(request, "encyclopedia/page.html", {
            "content": html,
            "name": title
        })

def get_content(request, title):
    entry = util.get_entry(title)
    if (entry == None):
        return render(request, "encyclopedia/error.html")
    html = markdown2.markdown(entry)
    return render(request, "encyclopedia/page.html", {
        "content": html,
        "name": title
    })

def search(request):
    query = request.GET.get("q")
    entries = util.list_entries()
    matched_entries = [entry for entry in entries if query.lower() in entry.lower()]
    
    for entry in entries:
        if query.lower() == entry.lower():
            return get_content(request, entry)
    
    return render(request, "encyclopedia/search.html", {
        "entries": matched_entries,
        "query": query
    })
    
def random_page(request):
    entries = util.list_entries()
    entry = choice(entries)
    return get_content(request, entry)

def edit_page(request, name):
    return render(request, "encyclopedia/edit.html", {"title": name, "content": util.get_entry(name)})

def edited_page(request, name):
    if request.method == 'POST':
        #retrieve the new markdown content
        content = request.POST.get("new_content")
        #Replace the entry with the new content
        util.save_entry(name, content)
        return get_content(request, name)