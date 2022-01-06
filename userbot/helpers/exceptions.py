import math
import time
from typing import Dict, Tuple

from telethon.errors.rpcerrorlist import MessageNotModifiedError

from ..Config import Config

_TASKS: Dict[str, Tuple[int, int]] = {}


class CancelProcess(Exception):
    """
    Cancel Process
    """


async def progress(
    current,
    total,
    gdrive,
    start,
    prog_type,
    file_name=None,
    is_cancelled=False,
    delay=5,
):  # sourcery no-metrics
    if is_cancelled is True:
        raise CancelProcess
    task_id = f"{gdrive.chat_id}.{gdrive.id}"
    if current == total:
        if task_id not in _TASKS:
            return
        del _TASKS[task_id]
        try:
            await gdrive.edit("`finalizing process ...`")
        except MessageNotModifiedError:
            pass
        except Exception as e:
            LOGS.error(str(e))
        return
    now = time.time()
    if task_id not in _TASKS:
        _TASKS[task_id] = (now, now)
    start, last = _TASKS[task_id]
    elapsed_time = now - start
    oldtmp = ""
    if (now - last) >= delay:
        _TASKS[task_id] = (start, now)
        percentage = current * 100 / total
        speed = current / elapsed_time
        eta = round((total - current) / speed)
        elapsed_time = round(elapsed_time)
        if "upload" in prog_type.lower():
            status = "Uploading"
        elif "download" in prog_type.lower():
            status = "Downloading"
        else:
            status = "Unknown"
        progress_str = "`{0}` | `[{1}{2}] {3}%`".format(
            status,
            "".join(
                Config.FINISHED_PROGRESS_STR for i in range(math.floor(percentage / 5))
            ),
            "".join(
                Config.UNFINISHED_PROGRESS_STR
                for i in range(20 - math.floor(percentage / 5))
            ),
            round(percentage, 2),
        )
        tmp = (
            f"{progress_str}\n"
            f"`{humanbytes(current)} of {humanbytes(total)}"
            f" @ {humanbytes(speed)}`\n"
            f"**ETA :**` {time_formatter(eta)}`\n"
            f"**Duration :** `{time_formatter(elapsed_time)}`"
        )
        if tmp != oldtmp:
            if file_name:
                await gdrive.edit(
                    f"**{prog_type}**\n\n"
                    f"**File Name : **`{file_name}`**\nStatus**\n{tmp}"
                )
            else:
                await gdrive.edit(f"**{prog_type}**\n\n" f"**Status**\n{tmp}")
            oldtmp = tmp


# FIREX
