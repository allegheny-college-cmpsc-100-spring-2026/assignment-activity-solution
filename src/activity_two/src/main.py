def main():
    num_range = input("Enter a range (x-y): ")
    start, end = num_range.split("-")
    print(f"Calculating {start}-{end}")
    start = int(start)
    end = int(end)
    num_of_terms = end - start + 1
    sum_of_terms = start + end
    print(int((num_of_terms/2) * sum_of_terms))

if __name__ == "__main__":
    main()