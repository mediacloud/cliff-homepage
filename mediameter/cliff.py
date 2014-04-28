import logging
import requests

class Cliff():
    '''
    Make requests to a cliff server
    '''

    PATH_TO_CLIFF = "/CLIFF/parse/text"

    def __init__(self,host,port):
        self._log = logging.getLogger('cliff')
        self._url = host+":"+str(port)+Cliff.PATH_TO_CLIFF

    def query(self,text):
        payload = {'q':text}
        try:
            r = requests.get(self._url, params=payload)
            self._log.info(r.content)
            return r.json()
        except requests.exceptions.RequestException as e:
            self._log.error("RequestException " + str(e))
        return ""
