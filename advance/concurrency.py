import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate a network delay
    print("Data fetched!")
    return {"data": "Sample Data"}

async def main():
    print("Starting main function...")
    data = await fetch_data()
    print("Data received:", data)

if __name__ == "__main__":
    asyncio.run(main())
    print("Main function completed.")