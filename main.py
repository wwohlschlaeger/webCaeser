#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2, string

def build_page(textarea_content):
    header =("<DOCTYPE= html>" +
            "<html>" + "<head>" +
            "<h2>Web Caeser</h2>" + "</head>" + "<body>")
    footer = ("</body" + "</html>")
    rot_message = "<label>Rotate message by how many characters:</label>" + "<input type='number' name='rotateChar'/>"
    textarea =("<label>Type the message:</label><br>" "<textarea name='message1' style='margin: 8px; height: 100px; width: 400px'>"
                + textarea_content + "</textarea>")
    submit = "<input type='submit'/>"
    form1= "<form method='post'>" + textarea + "<br>" + rot_message + "<br>" + submit + "</form>"

    return header + form1

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)

    def post(self):
        rot_num= self.request.get("rotateChar")
        message1= self.request.get('message1')
        encrypted_message= encrypt(message1,rot_num)
        content = build_page(encrypted_message)
        self.response.write(content)

def encrypt(exp,pos):
    temp = ""
    x = 0
    pos = int(pos)
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    for i in range(len(exp)):
        if exp[i].isalpha():
            if exp[i].isupper():
                x = upper.find(exp[i])
                if x+pos > 25:
                    temp = temp+upper[x-(26-pos)]
                else:
                    temp = temp+upper[x+pos]
            else:
                x = lower.find(exp[i])
                if x+pos > 25:
                    temp = temp+lower[x-(26-pos)]
                else:
                    temp = temp+lower[x+pos]
        else:
            temp = temp + exp[i]
    return temp

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
