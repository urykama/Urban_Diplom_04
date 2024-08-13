import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def matplotlib(name):
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple plot')
    plt.show()

def seaborn():
    tips = sns.load_dataset("tips")
    print(tips)
    sns.boxplot(x="day", y="total_bill", data=tips)
    plt.show()

def plotly():
    data = px.data.iris()
    print(data)
    fig = px.scatter(data, x="sepal_width", y="sepal_length", color="species")
    fig.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # matplotlib('PyCharm')
    seaborn()
    plotly()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
