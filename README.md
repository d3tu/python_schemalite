`pip install schemax`
```python
from schemax import Schema
schema = Schema({
    'a': {
        'b': str
    }
})
schema.test({
    'a': {
        'b': 'c'
    }
}) # True
schema.parse({
    'a': {}
}) # {'a': {'b': ''}}
```