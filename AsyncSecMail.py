import aiohttp,asyncio
class AsyncSecMail():
	def __init__(self):
		self.session = aiohttp.ClientSession()
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
		self.api="https://www.1secmail.com/api/v1"
	def __del__(self):
		try:
		          loop = asyncio.get_event_loop()
		          loop.create_task(self._close_session())
		except RuntimeError:
		          loop = asyncio.new_event_loop()
		          loop.run_until_complete(self._close_session())
	async def _close_session(self):
		if not self.session.closed: await self.session.close()
	async def domain_list(self):
		async with self.session.get(f"{self.api}/?action=getDomainList",headers=self.headers) as req:
			return await req.json()
	async def generate_email(self, count: int = 1):
		async with self.session.get(f"{self.api}/?action=genRandomMailbox&count={count}",headers=self.headers) as req:
			return await req.json()
	async def get_messages(self, email: str):
		email = email.split("@")
		async with self.session.get(f"{self.api}/?action=getMessages&login={email[0]}&domain={email[1]}",headers=self.headers) as req:
			return await req.json()
	async def read_message(self, email: str, id: str):
		email = email.split("@")
		async with self.session.get(f"{self.api}/?action=readMessage&login={email[0]}&domain={email[1]}&id={id}",headers=self.headers) as req:
			return await req.json()