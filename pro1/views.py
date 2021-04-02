from django.http import HttpResponse
def index(request):
    return HttpResponse("HELLO WORLD")

def page2(request):
    return HttpResponse("<h1>HEY BUDDY</h1>")

def page3(request):
    content = """<h1>REDDY</h1>
    <h2>KAMAL</h2>"""
    return HttpResponse(content)