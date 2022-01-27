import requests


class PayApi(object):

    @staticmethod
    def auth(card, amount):
        pay_url = "https://www.baidu.com"
        data = {'card': card, 'amount': amount}
        response = requests.post(pay_url, data=data)
        return response.status_code

    def pay(self, card, amount):
        status_code = self.auth(card, amount)
        try:

            if status_code == 200:
                print("User {} Pay {} Success".format(card, amount))
                return 'success'
            elif status_code == 500:
                print("User {} Pay {} Failed".format(card, amount))
                return 'failed'
            else:
                return 'error'
        except Exception as e:
            print(e)
            return 'error'


if __name__ == '__main__':
    pass
