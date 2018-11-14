例子如下：

```
import json
import numpy as np


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        return json.JSONEncoder.default(self, obj)


dict = {'id': 1, 'title': b'\xe7\xac\xac\xe4\xb8\x80\xe7\xab\xa0 \xe7\xa7\xa6\xe7\xbe\xbd'}
dup = json.dumps(dict, cls=MyEncoder, ensure_ascii=False, indent=4)
print(dup)
```
