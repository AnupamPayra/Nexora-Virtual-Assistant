import asyncio
from desktop_notifier import DesktopNotifier

async def reminder(task, time):

    notifier = DesktopNotifier()
    await  asyncio.sleep(time)
    await notifier.send(title="Hey Anupam", message=f"Did you {task}")
