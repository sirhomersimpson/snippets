# My favorite references bookmarks
https://realpython.com/ <br/>
https://github.com/wilfredinni/python-cheatsheet <br/>

# Context Manager 
https://rednafi.github.io/digressions/python/2020/03/26/python-contextmanager.html <br/>

Code snippet: <> <br/>

# Switch case in python - equivalent

```
>>> def south(): return "South"
... 
>>> def west(): return "west"
... 
>>> switch_case = { 1:south, 2:west}
>>> switch_case[1]
<function south at 0x7eff8812dee0>
>>> switch_case[1]()
'South'
>>> switch_case[2]()
```

# get UTC time
```
now = datetime.datetime.now(timezone.utc)
timestamp = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
```
ref: https://www.geeksforgeeks.org/get-utc-timestamp-in-python/ <br>

# Logging
```
import logging

logger = logging.getLogger(__name__)
c_handler = logging.StreamHandler()
c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
logger.addHandler(c_handler)

logger.setLevel(logging.DEBUG)
```
ref: https://realpython.com/python-logging/ <br>
