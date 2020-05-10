import pandas as pd
import matplotlib.pyplot as plt

#load rankings data here:
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

#function to plot rankings over time for 1 roller coaster here:
def rank_over_time(data, coaster, park):
    ranking_df = data[(data["Name"] == coaster) & (data["Park"] == park)]
    year = ranking_df["Year of Rank"]
    rank = ranking_df["Rank"]
    y_values = [int(i) for i in rank]
    ax = plt.subplot()
    plt.plot(year, rank)
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

# write function to plot rankings over time for 2 roller coasters here:










plt.clf()

# write function to plot top n rankings over time here:










plt.clf()

# load roller coaster data here:



# write function to plot histogram of column values here:










plt.clf()

# write function to plot inversions by coaster at a park here:










plt.clf()

# write function to plot pie chart of operating status here:










plt.clf()

# write function to create scatter plot of any two numeric columns here:










plt.clf()
