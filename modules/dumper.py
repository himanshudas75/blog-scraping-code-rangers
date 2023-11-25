import pandas as pd

def dump_data(data, file, sheet):
    # Convert the data so to add HYPERLINKS
    for i in range(len(data)):
        img_url = data[i]['Image']
        data[i]['Image'] = f'=HYPERLINK("{img_url}", "{img_url}")'

    df = pd.DataFrame(data)
    df.drop('Page Number', axis=1, inplace=True)
    df['Date'] = pd.to_datetime(df['Date']).dt.date

    df.to_excel(file, index=True, index_label="Index")