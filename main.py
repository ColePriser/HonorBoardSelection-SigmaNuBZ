import pandas as pd


def random_names(url):
    # Convert url into CSV export URL
    csv_export_url = url.replace('/edit#gid=', '/export?format=csv&gid=')
    test = pd.read_csv(csv_export_url, index_col=0, )
    print(test.head(1))


def main():
    random_names('https://docs.google.com/spreadsheets/d/16dbqX7Sfi9EgQ2CaKADGSJ499jncEEk0TJRxNzj5Ixw/edit#gid=0')
    return


if __name__ == '__main__':
    main()
