from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from butter_cms import ButterCMS
from os import environ

client = ButterCMS(environ.get("BUTTER_CMS_KEY"))

def to_home(request):
  return redirect("/saas-landing-page")

def handler(request, slug):
  page = client.pages.get("*", slug)
  menu = client.content_fields.get(['menu'], {
    "fields.name": "landing_page"
  })
  return render(request, "index.html", {
    "data": page["data"]["fields"],
    "menu": menu["data"]["menu"][0]["menu_items"],
  })