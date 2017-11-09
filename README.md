# Intercom API console

A lightweight wrapper around the Intercom REST API. Provides an interactive IPython console from which 
API operations may be performed. The client does not construct objects from the results and instead
returns simple Python dictionaries. 

### Example usage:

- Open an interactive shell:
```shell
python main.py
```
- Use the API:
```python
In [1]: user = client.users.create_with_email("console_user@example.com")
Request completed with status code: 200

In [2]: user['email']
Out[2]: u'console_user@example.com'
```

### Install/Configure:

- Clone the repo
- `pip install -r requirements.txt`
- Set access token as env variable INTERCOM_TOKEN

### Status:

This is not anywhere close to being complete yet. PRs welcome!

### Disclaimer:

This is **NOT** official Intercom software. Intercom does **NOT** support this code.
