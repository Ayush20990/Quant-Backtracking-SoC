import matplotlib.pyplot as plt
def plot_data(Dataframe,symbol):
    plt.figure(figsize=(10,6))
    plt.plot(Dataframe.index,Dataframe['Close'],label='Close price')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title(f"Closing price of {symbol}")
    plt.show()