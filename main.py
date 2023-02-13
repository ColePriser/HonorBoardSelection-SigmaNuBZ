import pandas as pd


def random_names(url):
    # Convert url into CSV export URL
    csv_export_url = url.replace('/edit#gid=', '/export?format=csv&gid=')
    # Read CSV URL into dataframe
    df = pd.read_csv(csv_export_url, index_col=0, )

    ## Separate roster by academic year
    freshman = df.loc[df['LEAD Phase'] == 'Phase 1']
    freshman_names = freshman['LEAD Phase']
    sophomore = df.loc[df['LEAD Phase'] == 'Phase 2']
    sophomore_names = sophomore['LEAD Phase']
    junior = df.loc[df['LEAD Phase'] == 'Phase 3']
    junior_names = junior['LEAD Phase']
    senior = df.loc[df['LEAD Phase'] == 'Phase 4']
    senior_names = senior['LEAD Phase']

    ## Randomly select class member from each year and load into array
    jury = [freshman_names.sample(n=1), sophomore_names.sample(n=1),
            junior_names.sample(n=1), senior_names.sample(n=1)]
    return jury


def main():
    jury = random_names('https://docs.google.com/spreadsheets/d/16dbqX7Sfi9EgQ2CaKADGSJ499jncEEk0TJRxNzj5Ixw/edit#gid=0')
    print(jury)


if __name__ == '__main__':
    main()
