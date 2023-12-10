
import asyncio
import time


@router.get("/terrible-ping")
async def terrible_catastrophic_ping():
    time.sleep(10)  # I/O blocking operation for 10 seconds
    pong = service.get_pong()  # I/O blocking operation to get pong from DB

    return {"pong": pong}
