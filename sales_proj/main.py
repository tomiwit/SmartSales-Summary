import pandas as pd


def load_file(name):
    try:
        df = pd.read_csv(name)
        return df
    except FileNotFoundError:
        print(f"File {name} not found. Please check the file name.")
        return None


def main():
    while True:
        file_name = input("Enter the file name\n")
        pepco = load_file(file_name)

        if pepco is None:
            continue

        categories = pepco['Category'].unique().tolist()

        print("--------------- BEST SELLING PRODUCTS PER CATEGORY ---------------\n")
        for category in categories:
            print(f"Category: {category}")
            best_selling = (
                pepco.query('Category == @category')
                .groupby('Product')
                .agg({'Total_Amount': 'sum', 'Quantity': 'sum'})
                .sort_values(by='Total_Amount', ascending=False)
            )
            print(best_selling)
            print("\n")

        print("--------------- AVERAGE SALES PER CATEGORY ---------------\n")
        for category in categories:
            avg_sales = pepco.query('Category == @category').groupby('Category')['Total_Amount'].mean()
            print(f"Category: {category} - Average Sales: {avg_sales.values[0]:.2f}")
            print("\n")

        print("------------- WORST SELLING PRODUCTS -------------\n")
        n = input("Enter how many products would you like to see: ")
        worst_selling = pepco.groupby('Product')['Quantity'].sum().sort_values().head(int(n))
        print(worst_selling)
        print("\n")

        option = input("Do you want to upload another file? (Y/N)").strip().lower()
        if option == "n":
            break


if __name__ == "__main__":
    main()
