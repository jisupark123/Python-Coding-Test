def memory_usage(message: str = "debug"):
    import psutil

    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2**20  # Bytes to MB
    print(f"[{message}] memory usage: {rss: 10.5f} MB")
