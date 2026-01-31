if __name__ == '__main__':
    # sizes = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
    sizes = [1, 2, 4, 8, 16, 32]
    times = []
    for n in sizes:
        input_text = make_input(n)
        start = time.perf_counter()
        ###########################
        recipients, proposers = Matcher.format_preferences(input_text)
        temp = Matcher.matcher(recipients=recipients, proposers=proposers)
        ###########################
        end = time.perf_counter()
        times.append(end - start)

    plt.scatter(sizes, times, color='red')

    sizes = np.array(sizes)
    times = np.array(times)
    z = np.polyfit(x=sizes, y=times, deg=len(sizes))
    p = np.poly1d(z)
    plt.plot(sizes, p(sizes))

    plt.title('Gale-Shapely Matcher Scalability')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Runtime (s)")
    plt.legend()

    plt.show()