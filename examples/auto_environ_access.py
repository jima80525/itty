from itty import *

@get('/')
def index(request):
    try:
        # Should raise an error.
        return 'What? Somehow found a remote user: %s' % request.REMOTE_USER
    except KeyError:
        pass

    return "Remote Addr: '{}' & GET name: '{}'".format(
            request.REMOTE_ADDR, request.GET.get('name', 'Not found'))

run_itty()
