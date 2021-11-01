from .base import BaseClient
from ..debug import register_redactions_from_response

import json


class Client(BaseClient):
    def _get_request(self, path, params):
        self.ensure_updated_refresh_token()

        dest = 'https://api.tdameritrade.com' + path

        req_num = self._req_num()
        self.logger.debug('Req {}: GET to {}, params={}'.format(
            req_num, dest, json.dumps(params, indent=4)))

        # resp = self.session.get(dest, params=params)
        resp = self.session.request('get', dest, params=params)
        self._log_response(resp, req_num)
        register_redactions_from_response(resp)
        return resp

    def _post_request(self, path, data):
        self.ensure_updated_refresh_token()

        dest = 'https://api.tdameritrade.com' + path

        req_num = self._req_num()
        self.logger.debug('Req {}: POST to {}, json={}'.format(
            req_num, dest, json.dumps(data, indent=4)))

        # resp = self.session.post(dest, json=data)
        resp = self.session.request('post', dest, json=data)
        self._log_response(resp, req_num)
        register_redactions_from_response(resp)
        return resp

    def _put_request(self, path, data):
        self.ensure_updated_refresh_token()

        dest = 'https://api.tdameritrade.com' + path

        req_num = self._req_num()
        self.logger.debug('Req {}: PUT to {}, json={}'.format(
            req_num, dest, json.dumps(data, indent=4)))

        # resp = self.session.put(dest, json=data)
        resp = self.session.request('put', dest, json=data)
        self._log_response(resp, req_num)
        register_redactions_from_response(resp)
        return resp

    def _patch_request(self, path, data):
        self.ensure_updated_refresh_token()

        dest = 'https://api.tdameritrade.com' + path

        req_num = self._req_num()
        self.logger.debug('Req {}: PATCH to {}, json={}'.format(
            req_num, dest, json.dumps(data, indent=4)))

        # resp = self.session.patch(dest, json=data)
        resp = self.session.request('patch', dest, json=data)
        self._log_response(resp, req_num)
        register_redactions_from_response(resp)
        return resp

    def _delete_request(self, path):
        self.ensure_updated_refresh_token()

        dest = 'https://api.tdameritrade.com' + path

        req_num = self._req_num()
        self.logger.debug('Req {}: DELETE to {}'.format(req_num, dest))

        # resp = self.session.delete(dest)
        resp = self.session.request('delete', dest)
        self._log_response(resp, req_num)
        register_redactions_from_response(resp)
        return resp
