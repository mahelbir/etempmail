# ETempMail

A simple Python module to get free disposable temporary email address.

## Installation

To install etempmail use pip:

```bash
$ pip install etempmail
```

## Usage

```python
from etempmail import TempMail

temp_mail = TempMail()  # or TempMail('WHHKSIX7915')
print(temp_mail.id)  # 7998
print(temp_mail.email)  # sidavm5dhc@istanbultaksi.xyz
print(temp_mail.recovery)  # WHHKSIX7915
print(temp_mail.inbox())  # [{'subject': 'test', 'from': 'Anonymousemail <noreply@anonymousemail.me>', 'date': '16/08/2022 19:40:47', 'body': 'Test Body Code: 123'}]
```

## License

The MIT License (MIT). Please see [License File](LISENCE) for more information.