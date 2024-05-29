# etempmail

[![PyPI](https://img.shields.io/pypi/v/etempmail)](https://pypi.org/project/etempmail/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/etempmail)](https://pypi.org/project/etempmail/)
[![PyPI - License](https://img.shields.io/pypi/l/etempmail)](https://pypi.org/project/etempmail/)

A simple module to get free disposable temporary email address.

## Installation

To install etempmail use pip:

```bash
pip install etempmail
```

## Usage

```python
from etempmail import TempMail

# recovery: str = None, url: str = 'https://etempmail.com', debug_response: bool = True
temp_mail = TempMail()  # or TempMail('OGFHVIX7915')

print(temp_mail.id)
# 7915

print(temp_mail.email)
# sidavm5dhc@upperbox.xyz

print(temp_mail.recovery)
# OGFHVIX7915

print(temp_mail.inbox())
# [{'subject': 'test', 'from': 'Anonymousemail <noreply@gmail.com>', 'date': '16/08/2022 19:40:47', 'body': 'Test Body Code: 123'}]

temp_mail.recover('OGFHVSZ115741')  # Recover email address
temp_mail.change()  # Change email address
```

## Note

You can use the following domains or similar:

+ https://etempmail.com
+ https://gecicimail.com.tr
+ https://toprakmail.com
+ https://segamail.com

## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.