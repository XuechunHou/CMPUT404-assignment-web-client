
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

import urllib.parse
class URL(object):
    def __init__(self, url):
        self.url = url
        self.parse_url()
    def parse_url(self):
        parsed_url = urllib.parse.urlparse(self.url)
        self.path = parsed_url.path
        self.query = parsed_url.query
        self.fragment = parsed_url.fragment
        self.hostname = parsed_url.hostname
        self.port = parsed_url.port
        self.scheme = parsed_url.scheme
    def construct_full_path(self):
        full_path = self.path
        if not self.path:
            full_path = "/"
        
        if self.query:
            full_path = full_path + "?" + self.query
        if self.fragment:
            full_path = full_path + "#" + self.fragment
        return full_path
    def set_port(self):
        if not self.port and self.scheme == "http":
            self.port = 80
        elif not self.port and self.scheme == "https":
            self.port = 443
        elif not self.port:
            self.port = 8080