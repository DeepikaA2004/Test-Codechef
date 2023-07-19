def can_complete_book(pages, pages_per_day, num_days):
    total_pages = pages_per_day * num_days
    return total_pages >= pages

# Main function to read inputs and call the helper function for each test case
def main():
    # Read the number of test cases
    t = int(input().strip())

    # Process each test case
    for _ in range(t):
        pages, pages_per_day, num_days = map(int, input().strip().split())
        if can_complete_book(pages, pages_per_day, num_days):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
