from itty import *

@get('/upload')
def upload(request):
    return open('examples/html/upload.html', 'r').read()

@post('/test_upload')
def test_upload(request):
    myfilename = ''
    
    if request.POST['myfile'].filename:
        myfilename = request.POST['myfile'].filename
        myfile_contents = request.POST['myfile'].file.read()
        uploaded_file = open(myfilename, 'wb')
        uploaded_file.write(myfile_contents)
        uploaded_file.close()
    
    html = """
    'foo' is: {}<br>
    'bar' is: {}
    """.format(request.POST.get('foo', 'not specified'), myfilename)
    return html

run_itty()
