import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

class post_trade_analysis:
    def __init__(self, returns):
        if isinstance(returns, pd.Series):
            returns = returns.to_frame()
        elif not isinstance(returns, pd.DataFrame):
            raise TypeError("Input should be a pandas DataFrame or Series")
        
        self.returns = returns.copy() 

    def cumulative_returns(self):
        self.cum_returns = (1 + self.returns).cumprod() - 1
        return self.cum_returns

    def max_drawdown(self):
        running_max = self.cumulative_returns().cummax()
        drawdown = running_max - self.cumulative_returns()
        drawdown_pct = drawdown / running_max
        return drawdown_pct.max()

    def sharpe_ratio(self, risk_free_rate=0.08):
        #convert annual risk free rate to daily risk free return 
        risk_free_rate=(1+risk_free_rate)**(1/252)-1
        excess_returns = self.returns - risk_free_rate
        std_excess_returns = np.std(excess_returns, axis=0)
        avg_excess_returns = np.mean(excess_returns, axis=0)
        return avg_excess_returns / std_excess_returns * np.sqrt(252)

    def sortino_ratio(self, risk_free_rate=0.08):
    #convert annual risk free rate to daily risk free return 
        risk_free_rate=(1+risk_free_rate)**(1/252)-1 
        excess_returns = self.returns - risk_free_rate
        downside_risk = np.std(excess_returns[excess_returns < 0], axis=0)
        return np.mean(excess_returns) / downside_risk * np.sqrt(252)

    def hit_ratio(self):
        return (self.returns > 0).mean()

    def monthly_returns_heatmap(self):
        returns_df = self.returns.copy() 
        returns_df.index = pd.to_datetime(returns_df.index) 
        returns_df['year'] = returns_df.index.year
        returns_df['month'] = returns_df.index.month
        monthly_returns = returns_df.pivot_table(index='year', columns='month', values=returns_df.columns[0], aggfunc='sum')

        plt.figure(figsize=(12, 8))
        sns.heatmap(monthly_returns, annot=True, fmt=".2%", cmap="coolwarm", cbar=True)
        plt.title("Monthly Returns Heatmap")
        plt.xlabel("Month")
        plt.ylabel("Year")
        plt.show()

    def plot_cumulative_returns(self):
        cumulative_returns = self.cum_returns
        cumulative_returns.plot(figsize=(10, 6), title="Cumulative Returns")
        plt.xlabel("Date")
        plt.ylabel("Cumulative Returns")
        plt.grid(True)
        plt.show()