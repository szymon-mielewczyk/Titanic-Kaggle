# Preprocess and clean data
def clean_df(df, test=False):
    
    # Drop PassengerId and Name
    df.drop('PassengerId', axis='columns', inplace=True)
    df.drop('Name', axis='columns', inplace=True)

    # Cabin dictionary, char to int
    cabin_dict = {
    'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,
    'F':6,
    'G':7,
    'H':8,
    'T':9
    }

    # Define list for new column in dataframe
    chars_ids = []
    numbers = []
    # Change cabin column to cabin letter column and cabin number column
    # Iterate by rows
    for c_i, cabin in enumerate(df['Cabin']):
        # Change only value with str datatype
        if not isinstance(cabin,str):
            continue
        # Iterate by row value
        for n_i ,char in enumerate(cabin):
            # Start iterating from last to first char
            index = -1 - n_i
            # If given char in cabin dictionary
            if cabin[index] in cabin_dict.keys():
                # Append cabin id
                chars_ids.append(int(cabin_dict[cabin[index]]))
                # Cabin number
                cabin_number = str(df['Cabin'][c_i][index+1:])
                # If cabin number == cabin letter put 0
                if cabin_number in cabin_dict.keys(): cabin_number = 0
                # Append cabin number
                numbers.append(int(cabin_number))
                break

    # Create new columns
    df['Cabin_char_id'] = chars_ids
    df['Cabin_number'] = numbers
    # Delete old Cabin column
    df.drop('Cabin', axis='columns', inplace=True)

    # Change ticket value just to numbers
    # Iterate by rows
    for t_i, ticket in enumerate(df['Ticket']):
        # If ticket value == LINE change to 0
        if ticket == 'LINE':
            df.loc[t_i, 'Ticket'] = 0
        # Iterate by row value
        for c_i ,char in enumerate(ticket):
            # Start iterating from last to first char
            index = -1 - c_i
            # If whitespace found 
            if ticket[index] == ' ':
                # Change value to numbers after whitespace
                df.loc[t_i, 'Ticket'] = df['Ticket'][t_i][index+1:]   
                break
        continue

    # Reset dataframe indexing
    df.reset_index()

    # Create column for each embarked
    df['Embarked_C'] = [1 if embarked == 'C' else 0 for embarked in df['Embarked']]
    df['Embarked_Q'] = [1 if embarked == 'Q' else 0 for embarked in df['Embarked']]
    df['Embarked_S'] = [1 if embarked == 'S' else 0 for embarked in df['Embarked']]

    # delete old embarked column
    df.drop('Embarked', axis='columns', inplace=True)

    # Sex dictionary, str to int
    sex_dict = {
        'male':0,
        'female':1
    }

    # Replace values in dataframe with dictionary
    df.replace({'Sex':sex_dict}, inplace=True)

    # Fill na values with mean
    df.fillna(
                {
                'Fare': df['Fare'].mean(),
                },
                inplace=True
                ) 

    # If training data save temporary column
    if not test:
        df_y = df['Survived']
        df_y= (df_y).astype(float)
        # drop survived from dataframe
        df.drop('Survived', axis='columns', inplace=True)
    
    # drop rows with empty Ticket value
    df = df[df.Ticket != '']
    
    # Change Ticket datatype
    df['Ticket'] = (df['Ticket']).astype(float)

    # Change dataframe values range from 0 to 1
    df=(df-df.min())/(df.max()-df.min())

    # If training join Survived column
    if not test:
        df = df.join(df_y)

    return df