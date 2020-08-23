import json


class Invoice:
    amount = 0
    customer_id = 0
    email = ''
    code = ''
    first_name = ''
    middle_name = ''
    last_name = ''
    expires = ''
    metadata = None

    def __init__(self, amount):
        self.amount = amount

    def set_code(self, code):
        self.code = code

    def from_json(self, data):
        self.amount = data['amount']
        self.code = data['code']
        self.expires = data['expires']

    def get_body(self):
        body = {"amount": self.amount * 100}

        if self.code:
            body["code"] = self.code
        if self.metadata:
            body["metadata"] = json.dumps(self.metadata)
        if self.email:
            body["email"] = self.email
        if self.customer_id:
            body["customer_id"] = self.customer_id
        if self.first_name:
            body["first_name"] = self.first_name
        if self.middle_name:
            body["middle_name"] = self.middle_name
        if self.last_name:
            body["last_name"] = self.last_name

        return body
