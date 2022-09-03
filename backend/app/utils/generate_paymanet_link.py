
from app.src.payment.schemas import paymentLink
import requests
from app.utils.random_string import generate_pay_ref


def get_payment_link(data: paymentLink)->str:
    response: requests = requests.post("https://api.flutterwave.com/v3/payments",
                                       headers={
                                           "Authorization": f"Bearer $process.env.FLW_SECRET_KEY"},
                                       json=data.dict()
                                       )
    if response.status_codes == 200:
        return response.json()
    print(response.text)
