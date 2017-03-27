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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        message = 'Hellooooo world!'
        encrypted_message=encrypt(message,13)

        textarea = "<textarea>" + encrypted_message + "</textarea>"
        submit = "<input type='submit'/>"
        form1= "<form>" + textarea + "<br>" +submit + "</form>"
        self.response.write(form1)

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
