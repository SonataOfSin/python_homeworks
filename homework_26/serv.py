import asyncio
import websockets

# ინახავს დაკავშირებულ კლიენტებს: {websocket: username}
connected_clients = {}


async def broadcast(message, exclude=None):
    for client in list(connected_clients.keys()):
        if client != exclude:
            try:
                await client.send(message)
            except websockets.exceptions.ConnectionClosed:
                pass


async def handle_client(websocket):
    # პირველი მესიჯი, რომელსაც კლიენტი გამოგზავნის, არის მისი იუზერნეიმი
    username = await websocket.recv()
    connected_clients[websocket] = username
    print(f"{username} დაუკავშირდა სერვერს!")

    await broadcast(f"!!! {username} შემოუერთდა ჩატს!")

    try:
        async for message in websocket:
            formatted_message = f"{username}: {message}"
            print(f"მიღებულია: {formatted_message}")

            # მესიჯი ეგზავნება ყველას, გამომგზავნის გარდა
            await broadcast(formatted_message, exclude=websocket)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        # კლიენტის გათიშვისას წავშალოთ სიიდან და ვაცნობოთ დანარჩენებს
        del connected_clients[websocket]
        print(f"{username} გავიდა ჩატიდან.")
        await broadcast(f"!!! {username} გავიდა ჩატიდან.")


async def main():
    async with websockets.serve(handle_client, "localhost", 8080):
        print("სერვერი გაშვებულია ws://localhost:8080-ზე...")
        await asyncio.Future()  # უსასრულოდ მუშაობს


if __name__ == "__main__":
    asyncio.run(main())
