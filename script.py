import pandas as pd
import matplotlib.pyplot as plt

#load rankings data:
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

#function to plot rankings over time for 1 roller coaster:
def rank_over_time(data, coaster, park):
    ranking_df = data[(data["Name"] == coaster) & (data["Park"] == park)]
    year = ranking_df["Year of Rank"]
    rank = ranking_df["Rank"]
    y_values = [int(i) for i in rank]
    ax = plt.subplot()
    plt.plot(year, rank, marker='o')
    ax.invert_yaxis()
    ax.set_yticks(y_values)
    ax.set_yticklabels(y_values)
    plt.xlabel("Year")
    plt.ylabel("Golden Ticket Ranking")
    plt.title("Year-by-year ranking of " + coaster)
    plt.show()

#test case
rank_over_time(wood, "El Toro", "Six Flags Great Adventure")
plt.clf()

#function to plot rankings over time for 2 roller coasters:
def rank_comparison(data, coaster_1, park_1, coaster_2, park_2):
    df_1 = data[(data["Name"] == coaster_1) & (data["Park"] == park_1)]
    df_2 = data[(data["Name"] == coaster_2) & (data["Park"] == park_2)]
    ax = plt.subplot()
    plt.plot(df_1["Year of Rank"], df_1["Rank"], marker='o')
    plt.plot(df_2["Year of Rank"], df_2["Rank"], marker='o')
    ax.invert_yaxis()
    plt.xlabel("Year")
    plt.ylabel("Golden Ticket Ranking")
    plt.title("Year-by-year ranking of " + coaster_1 + " and " + coaster_2)
    plt.legend([coaster_1, coaster_2])
    plt.show()

#test case
rank_comparison(wood, "El Toro", "Six Flags Great Adventure", "Boulder Dash", "Lake Compounce")
plt.clf()

#function to plot top n rankings over time:
def top_n(data, n):
    df = data[data["Rank"] <= n]
    ax = plt.subplot()
    ax.invert_yaxis()
    plt.xlabel("Year")
    plt.ylabel("Golden Ticket Ranking")
    plt.title("Top " + str(n) + " coasters each year")
    for coaster in set(df["Name"]):
        ranking = df[df["Name"] == coaster]
        ax.plot(ranking["Year of Rank"], ranking["Rank"], marker='o', label=coaster)
    plt.legend()
    plt.show()

#test case
top_n(wood, 5)
plt.clf()

#load roller coaster data here:
coasters = pd.read_csv('roller_coasters.csv')
print(coasters.head())

#function to plot histogram of column values:
def histogram(data, column):
    plt.hist(data[column].dropna(), bins=100)
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.title("Distribution of roller coaster " + column + "s")
    plt.show()

#test case
histogram(coasters, "length")
plt.clf()

#function to plot inversions by coaster at a park:
def inversion(data, park):
    df = data[(data["park"] == park) & (data["num_inversions"] > 0)]
    names = df["name"]
    inversions = df["num_inversions"]
    xvalues = range(len(names))
    plt.bar(xvalues, inversions)
    ax = plt.subplot()
    ax.set_xticks(xvalues)
    ax.set_xticklabels(names)
    plt.ylabel("Number of inversions")
    plt.xlabel("Coaster name")
    plt.title("Number of inversion on each coaster")
    plt.show()
    
#test case
inversion(coasters, "Parc Asterix")
plt.clf()

#function to plot pie chart of operating status:
def pie_chart(data):
    operating = data[data["status"] == "status.operating"]
    closed = data[data["status"] == "status.closed.definitely"]
    status = [len(operating), len(closed)]
    ax = plt.subplot()
    ax.pie(status, autopct="%0.1f%%", labels=["Open", "Closed"])
    ax.set_title('Operating Status')
    ax.axis('equal')
    plt.show()

#test case
pie_chart(coasters)
plt.clf()

#function to create scatter plot of any two numeric columns:
def scatter(data, col1, col2):
    column1 = data[col1]
    column2 = data[col2]
    plt.scatter(column1, column2, marker='x')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title(col1 + " vs. " + col2)
    plt.show()

#test case
scatter(coasters, "speed", "num_inversions")
plt.clf()