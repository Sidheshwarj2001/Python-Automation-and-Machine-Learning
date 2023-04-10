import multiprocessing

def main():
    print("Number of core are : ",multiprocessing.cpu_count())

if __name__ == "__main__":
    main()