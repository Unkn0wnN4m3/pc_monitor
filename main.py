#!/usr/bin/env python3

import time
import os
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

    bar = "█" * length + "-" * (bars - length)

    return bar


def show_usage(cpu_usage: float, memory_usage: float, bars: int = 20) -> None:
    '''
    Displays cpu and ram usage along with a "graph" represented with text
    strings.
    '''
    # Assigns the "graph" to variables
    cpu_bar = show_bars(cpu_usage, bars)
    mem_bar = show_bars(memory_usage, bars)

    print("CPU Usage: |{}| {}%  MEM Usage: |{}| {}%  ".format(
        cpu_bar, round(cpu_usage, 2), mem_bar, round(memory_usage, 2)),
          end="\r")


def main():
    term_size = int(os.get_terminal_size().columns / 4)

    while True:
        show_usage(psutil.cpu_percent(),
                   psutil.virtual_memory().percent, term_size)
        time.sleep(0.5)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n[+] Exitings...")
        exit(0)
