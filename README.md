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

## Building a Docker Container

```bash
docker build -t nestpension:test .
```

## Docker Compose File

```yaml
version: "3.1"

services:
  nestpension:
    image: nestpension:test
    environment:
      NEST_USERNAME: USERNAME
      NEST_PASSWORD: PASSWORD
      HOURS: 12
      DB_HOST: HOST ADDRESS
      DB_PORT: 3306
      DB_USERNAME: user
      DB_PASSWORD: pass
      DB_DATABASE: finance
```
