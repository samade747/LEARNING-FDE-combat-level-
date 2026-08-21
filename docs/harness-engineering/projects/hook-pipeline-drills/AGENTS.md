# Hook Pipeline Drills

This project has one job: run the 3 wired hooks (trace, curl-block,
conditional gate) for real and observe what each one does — never assume
their behavior from reading the scripts alone.

Never bypass `block_curl.py` by using `wget` or another fetch method to
"complete" a task it blocked — the drill is about the block, not the
workaround.
