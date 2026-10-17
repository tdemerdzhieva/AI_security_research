import asyncio
from fastmcp import Client

client = Client("http://{target}/")

async def read_resource(uri):
    try:
        result = await client.read_resource(uri)

        # If the result is a list, extract text from each block
        if isinstance(result, list):
            for block in result:
                if hasattr(block, "text"):
                    print(block.text)
        # If it's a single content object, print its text directly
        elif hasattr(result, "text"):
            print(result.text)

    except Exception as e:
        print(f"Error reading {uri}: {e}")

async def main():
    async with client:
        await read_resource("resource://logs")
        await read_resource("resource://items")

asyncio.run(main())