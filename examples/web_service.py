from itty import *

@get('/get/(?P<name>\w+)')
def test_get(request, name=', world'):
    return 'Hello {}!'.format(name)

@post('/post')
def test_post(request):
    return "'foo' is: {}".format(request.POST.get('foo', 'not specified'))

@put('/put')
def test_put(request):
    return "'foo' is: {}".format(request.PUT.get('foo', 'not specified'))

@delete('/delete')
def test_delete(request):
    return 'Method received was {}.'.format(request.method)

run_itty()
