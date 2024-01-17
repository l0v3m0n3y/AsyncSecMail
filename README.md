# AsyncSecMail.py
Async library for 1secmail.com
![68747470733a2f2f6769746875622e636f6d2f7176636f2f317365634d61696c2d507974686f6e2f6173736574732f37373338323736372f66646536396331612d623935662d346437382d616631612d326463613331353230346263](https://github.com/aminobotskek/AsyncSecMail/assets/94906343/932155a4-f5e7-477f-a8b1-d7a05d5fe40c)

# Install
```
git clone https://github.com/aminobotskek/AsyncSecMail
```


# Example
```python3
import AsyncSecMail
import asyncio
async def main():
	client=AsyncSecMail.AsyncSecMail()
	data=await client.generate_email()
	print(data)
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
