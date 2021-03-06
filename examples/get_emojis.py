import emojigg
import asyncio

import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def main():
    client = emojigg.Client()
    
    emojis = await client.fetch_emojis()
    logging.info(f"Total emojis: {len(emojis)}")
    
asyncio.run(main())