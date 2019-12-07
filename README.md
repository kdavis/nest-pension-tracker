# NEST Pension Python Class

## Install the requirements

Install Python 3+

```bash
pip3 install -r requirements.txt
```

## Start using the new class

```python
from nestpension import NestPension

my_pension = NestPension("my username", "my password")
my_pension.login()

print("My fund value is: £%s" % (my_pension.get_value()))
```
