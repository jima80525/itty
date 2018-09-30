from itty import *

@get('/')
def test_get(request):
    return "'foo' is: {}".format(request.GET.get('foo', 'not specified'))

run_itty()
