#!/usr/bin/env python3

import time
import psutil

# RAM & CPU monitor
# Track the usage of your CPU and RAM


def show_bars(usage: float, bars: int) -> str:
    '''
    This takes the usage information and returns into a strig of charecters

    Fill in the usage with "█", and what is not in use, fill in with "-".
    '''
    # Calculate the percentage of use depending on the desired width (bars)
    percent = (usage / 100.0)
    length = int(percent * bars)

    bar = "█" * int(length) + "-" * (bars - int(length))

    return bar


def show_usage(cpu_usage: float, memory_usage: float, bars: int = 50):
    '''
    Displays cpu and ram usage along with a "graph" represented with text
    strings.
    '''
    # Assigns the "graph" to variables
    cpu_bar = show_bars(cpu_usage, bars)
    mem_bar = show_bars(memory_usage, bars)

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  ", end="")
    print(f"MEM Usage: |{mem_bar}| {memory_usage:.2f}%  ", end="\r")


if __name__ == "__main__":
    try:
        while True:
            show_usage(psutil.cpu_percent(),
                       psutil.virtual_memory().percent, 20)
            time.sleep(0.5)
    except (KeyboardInterrupt, EOFError):
        print("\n[+] Exitings...")
        exit(0)
