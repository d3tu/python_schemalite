```python
from schemalite import Schema
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