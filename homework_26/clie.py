import asyncio
import websockets


async def receive_messages(websocket):
    async for message in websocket:
        print(message)


async def send_messages(websocket):
    loop = asyncio.get_event_loop()
    while True:
        message = await loop.run_in_executor(None, input)
        await websocket.send(message)


async def main():
    uri = "ws://localhost:8080"
    username = input("შეიყვანეთ თქვენი იუზერნეიმი: ")

    async with websockets.connect(uri) as websocket:
        # პირველივე რაც იგზავნება, არის იუზერნეიმი
        await websocket.send(username)
        print(f"დაუკავშირდით ჩატს, როგორც {username}. დაწერეთ მესიჯი და დააჭირეთ Enter-ს.\n")

        # ერთდროულად ველოდებით შემომავალ მესიჯებს და ვგზავნით ჩვენსას
        await asyncio.gather(
            receive_messages(websocket),
            send_messages(websocket)
        )


if __name__ == "__main__":
    asyncio.run(main())
