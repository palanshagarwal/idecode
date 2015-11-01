from .forms import SnippetForm
from .models import Snippet
from django.shortcuts import render, redirect


def simple(request):
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            source = form.cleaned_data['text']
            lang = form.cleaned_data['lang']
            print source
            form.save()
        form = SnippetForm(initial={'text': source, 'lang':lang})
        return render(request, "snippets.html", {
            "form": form,
            "snippets": Snippet.objects.all()
        })
    else:
        form = SnippetForm()
    return render(request, "snippets.html", {
        "form": form,
        "snippets": Snippet.objects.all()
    })
