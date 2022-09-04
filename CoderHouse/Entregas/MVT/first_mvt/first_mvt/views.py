from django.http import HttpResponse
from django.template import Template, Context, loader
from mvt_app.models import Familiares

def Welcome (request):
    return HttpResponse("<b>Welcome to my family tree, please redirect yourself to localhost:8000/family/ to visualize it.<b>")


def family_template(request):
    myhtml = open("/Users/felielosu/Documents/VSCode /CoderHouse/Entregas/MVT/first_mvt/mvt_app/templates/family.html")
    data = Familiares.objects.all()
    dictionary = {'familiares':data}
    template = Template(myhtml.read())
    myhtml.close()
    mycontext = Context(dictionary)
    html_document = template.render(mycontext)

    return HttpResponse(html_document)