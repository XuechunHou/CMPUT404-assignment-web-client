# Copyright 2020 Xuechun Hou

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#      http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from abc import ABC, abstractmethod
import urllib.parse
class HTTPRequest(ABC):
    def __init__(self, url_object):
        self.http_version = "HTTP/1.1"
        self.url_object = url_object
        self.header = []

    @abstractmethod
    def construct_request_header(self):
        pass
    @abstractmethod
    def construct_request_body(self):
        pass
    @abstractmethod
    def construct_request_whole(self):
        pass
    

class GETRequest(HTTPRequest):
    def __init__(self,url_object):
        super().__init__(url_object)


    def construct_request_header(self):
        # construct starter line  header
        starter_line = "GET {} {}".format(self.url_object.construct_full_path(), self.http_version)
        self.header.append(starter_line)
        # construct Host header
        host_line = "Host: {}".format(self.url_object.hostname)
        if self.url_object.port:
            host_line = host_line + ":" + str(self.url_object.port)
        self.header.append(host_line)
        # append default header
        self.header.append("Accept: */*")
        self.header.append("Connection: close")
        
    def construct_request_body(self):
        return None
    
    def construct_request_whole(self):
        self.construct_request_header()
        return "\r\n".join(self.header) + "\r\n\r\n"

class POSTRequest(HTTPRequest):
    def __init__(self,url_object, args):
        super().__init__(url_object)
        self.args = args
    def construct_request_header(self):
        # construct starter line  header
        starter_line = "POST {} {}".format(self.url_object.construct_full_path(),self.http_version)
        self.header.append(starter_line)
        # construct Host header
        host_line = "Host: {}".format(self.url_object.hostname)
        if self.url_object.port:
            host_line = host_line + ":" + str(self.url_object.port)
        self.header.append(host_line)
        # append default header
        self.header.append("Accept: */*")
        self.header.append("Content-Type: application/x-www-form-urlencoded")
        self.header.append("Connection: close")
        
    def construct_request_body(self):
        if self.args:
            return urllib.parse.urlencode(self.args)
        return ""
    def construct_request_whole(self):
        self.construct_request_header()
        body = self.construct_request_body()
        self.header.append("Content-Length: {}".format(len(body)))
        if body:
            return "\r\n".join(self.header) + "\r\n\r\n" + body
            
        return "\r\n".join(self.header) + "\r\n\r\n"
            