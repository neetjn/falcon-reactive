class Reactive(object):

    @staticmethod
    def respond(responder):
        def wrapped(*args, **kwargs):
            resp = args[2]
            if not resp.context.get('cached'):
                responder(*args, **kwargs)
        return wrapped

    @staticmethod
    def handle(responder):
        def wrapped(*args, **kwargs):
            resp = args[2]
            if not resp.context.get('cached'):
                responder(*args, **kwargs)
        return wrapped
