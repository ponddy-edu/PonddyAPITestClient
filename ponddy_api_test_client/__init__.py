from django.test.client import Client


class PayloadClient(Client):

    def delete(self, *args, **kwargs):
        """ Construct a DELETE request that includes data. """
        kwargs.update({'REQUEST_METHOD': 'DELETE'})
        kwargs.update({'content_type': 'application/json'})
        return super().put(*args, **kwargs)

    def patch(self, *args, **kwargs):
        kwargs.update({'REQUEST_METHOD': 'PATCH'})
        kwargs.update({'content_type': 'application/json'})
        return super().put(*args, **kwargs)

    def put(self, *args, **kwargs):
        kwargs.update({'REQUEST_METHOD': 'PUT'})
        kwargs.update({'content_type': 'application/json'})
        return super().put(*args, **kwargs)

    def post(self, *args, **kwargs):
        kwargs.update({'content_type': 'application/json'})
        return super().post(*args, **kwargs)

    def get(self, *args, **kwargs):
        kwargs.update({'content_type': 'application/json'})
        return super().get(*args, **kwargs)


class SSOClient(PayloadClient):

    def __init__(self, token=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token

    def delete(self, *args, **kwargs):
        kwargs.update({'HTTP_AUTHORIZATION': self.token})
        return super().delete(*args, **kwargs)

    def patch(self, *args, **kwargs):
        kwargs.update({'HTTP_AUTHORIZATION': self.token})
        return super().patch(*args, **kwargs)

    def put(self, *args, **kwargs):
        kwargs.update({'HTTP_AUTHORIZATION': self.token})
        return super().put(*args, **kwargs)

    def post(self, *args, **kwargs):
        kwargs.update({'HTTP_AUTHORIZATION': self.token})
        return super().post(*args, **kwargs)

    def get(self, *args, **kwargs):
        kwargs.update({'HTTP_AUTHORIZATION': self.token})
        return super().get(*args, **kwargs)


class APIClient(PayloadClient):

    def __init__(self, app=None, api=None,
                 token=None, status=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app, self.api, self.token, self.status = app, api, token, status
        self._headers = {
            'HTTP_APP': self.app,
            'HTTP_API': self.api,
            'HTTP_AUTHORIZATION': self.token,
            'HTTP_STATUS': self.status
        }

    def _update(self, dictionary):
        for key, val in self._headers.items():
            dictionary.setdefault(key, val)

    def delete(self, *args, **kwargs):
        self._update(kwargs)
        return super().delete(*args, **kwargs)

    def patch(self, *args, **kwargs):
        self._update(kwargs)
        return super().patch(*args, **kwargs)

    def put(self, *args, **kwargs):
        self._update(kwargs)
        return super().put(*args, **kwargs)

    def post(self, *args, **kwargs):
        self._update(kwargs)
        return super().post(*args, **kwargs)

    def get(self, *args, **kwargs):
        self._update(kwargs)
        return super().get(*args, **kwargs)
