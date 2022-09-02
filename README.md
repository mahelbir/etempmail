# ETempMail

A simple Python module to get free disposable temporary email address.

## Installation

To install etempmail use pip:

```bash
pip install etempmail
```

## Usage

```python
from etempmail import TempMail

# recovery: str = None, url: str = 'https://etempmail.com', debug_response: bool = True
temp_mail = TempMail()  # or TempMail('WHHKSIX7915')

print(temp_mail.domains())  # response -> (domain_id, domain_name)
# [('5', 'gmail.com'), ('4', 'hotmail.com'), ('2', 'yandex.com')]
print(temp_mail.id)
# 7915
print(temp_mail.email)
# sidavm5dhc@istanbultaksi.xyz
print(temp_mail.recovery)
# WHHKSIX7915
print(temp_mail.inbox())
# [{'subject': 'test', 'from': 'Anonymousemail <noreply@gmail.com>', 'date': '16/08/2022 19:40:47', 'body': 'Test Body Code: 123'}]

temp_mail.recover('LHKXDMG7910')  # Recover email address
temp_mail.change()  # Change email address by random domain
temp_mail.change(4)  # Change email address by domain_id
```

## License

The MIT License (MIT). Please see [License File](LISENCE) for more information.