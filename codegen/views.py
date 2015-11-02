from .forms import SnippetForm
from .models import Snippet
import requests

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse

COMPILE_URL = 'https://api.hackerearth.com/v3/code/compile/'
RUN_URL = 'https://api.hackerearth.com/v3/code/run/'

CLIENT_SECRET = 'de88e83b32f8ac80fa060182170efc867355b051'
DOWNLOAD_PREFIX = 'https://code.hackerearth.com/download/'


def simple(request):
    """
    This method creates a new snippet object when a code is
    compiled & run for first time.
    """
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = Snippet()
            snippet.text = form.cleaned_data['text']
            snippet.lang = form.cleaned_data['lang']
            snippet.file_name = form.cleaned_data['file_name']
            snippet.save()
            key = generate_key(snippet.code_id)
            snippet.write_key = key
            snippet.save()
            return custom_redirect(
                'update_code',
                snippet.code_id,
                key=snippet.write_key)
        else:
            form = SnippetForm(initial={'file_name': 'Untitled File'})
    else:
        form = SnippetForm(initial={'file_name': 'Untitled File'})
    return render(request, "snippets.html", {
        "form": form,
    })


def custom_redirect(url_name, *args, **kwargs):
    """
    This method redirects the view to the url_name passed
    with arguments and GET parameters.
    """
    from django.core.urlresolvers import reverse
    import urllib
    url = reverse(url_name, args=args)
    params = urllib.urlencode(kwargs)
    return HttpResponseRedirect(url + "?%s" % params)


def generate_key(code_id):
    """
    This method generates a unique md5 hash using the
    combination of current time and code_id passed.
    """
    from hashlib import md5
    from time import localtime
    return "%s" % (md5(str(localtime()) + str(code_id)).hexdigest())


def compile_n_run(source, lang, inputt=None):
    """
    This method calls the hackerearth APIs to compile & run
    the code according to parameters passed.
    """
    data = {
        'client_secret': CLIENT_SECRET,
        'async': 0,
        'source': source,
        'lang': lang,
        'time_limit': 5,
        'memory_limit': 262144,
    }
    if inputt:
        data['input'] = inputt
    r = requests.post(RUN_URL, data=data)
    return r.json()


def update_code(request, code_id):
    """
    This method implements the core logic after a code is compiled & run once.
    It takes care of read only and read & write permissions associated with the
    code.
    It also updates the run count variable associated with each code snippet
    object atomically.
    """
    from django.db.models import F
    from django.core.exceptions import ObjectDoesNotExist
    context = RequestContext(request)
    try:
        code = Snippet.objects.get(pk=code_id)

    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')

    write_key = request.GET.get('key', False)
    code_input = False

    if request.method == 'GET':
        if write_key == code.write_key:
            # Run the code if it has not been run atleast once.
            if code.run_count == 0:
                code_output = compile_n_run(code.text, code.lang)
                read_only = write_key
                code.download_url = DOWNLOAD_PREFIX + \
                    str(code_output['code_id'])
                # code.run_count += 1
                code.run_count = F('run_count') + 1
                code.save()
                try:
                    code = Snippet.objects.get(pk=code_id)

                except ObjectDoesNotExist:
                    return HttpResponseRedirect('/')
            else:
                code_output = False
                read_only = write_key
        else:
            read_only = False
            code_output = False

    else:
        form = SnippetForm(request.POST)
        if form.is_valid():
            write_key = form.cleaned_data['write_key']

        else:
            return HttpResponseRedirect('/')

        if write_key == code.write_key:
            code.text = form.cleaned_data['text']
            code.lang = form.cleaned_data['lang']
            code.file_name = form.cleaned_data['file_name']
            code.save()
            if form.cleaned_data['custom_input']:
                code_input = form.cleaned_data['manual_input']
                code_output = compile_n_run(code.text, code.lang, code_input)
            else:
                code_output = compile_n_run(code.text, code.lang)
            read_only = write_key
            # code.run_count += 1
            code.run_count = F('run_count') + 1
            code.save()
            try:
                code = Snippet.objects.get(pk=code_id)

            except ObjectDoesNotExist:
                return HttpResponseRedirect('/')

        else:
            lang = form.cleaned_data['lang']
            if form.cleaned_data['custom_input']:
                code_input = form.cleaned_data['manual_input']
                code_output = compile_n_run(code.text, lang, code_input)
            else:
                code_output = compile_n_run(code.text, lang)
            read_only = False
            # code.run_count += 1
            code.run_count = F('run_count') + 1
            code.save()
            try:
                code = Snippet.objects.get(pk=code_id)

            except ObjectDoesNotExist:
                return HttpResponseRedirect('/')

    form = SnippetForm(
        initial={
            'text': code.text,
            'file_name': code.file_name})
    context_list = {
        'form': form,
        'code': code,
        'code_output': code_output,
        'read_only': read_only,
        'code_input': code_input,
    }
    return render_to_response('codepage.html', context_list, context)


def clone_code(request, code_id):
    """
    This method clones the code associated with the code_id
    as another snippet object.
    """
    try:
        code = Snippet.objects.get(pk=code_id)

    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')
    snippet = Snippet()
    snippet.text = code.text
    snippet.lang = code.lang
    snippet.file_name = code.file_name
    snippet.save()
    key = generate_key(snippet.code_id)
    snippet.write_key = key
    snippet.save()
    return custom_redirect(
        'update_code',
        snippet.code_id,
        key=snippet.write_key)
