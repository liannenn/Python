import matplotlib.pyplot as plt

def main():
    # This program displays a simple line graph.
    
    x_coords = [0, 1, 2 ,3, 4]
    y_coords = [0, 3, 1, 5, 2]
    
    #add a title
    plt.title("Sales by Year")
    
    #add lavels to the axes 
    plt.xlabel('Year')
    plt.ylabel('Sales')
    
    #set the axis limits
    #plt.xlim(xmin = -1, xmax = 10)
    
    #plt.ylim(ymin = -1, ymax = 6)
    
    #label the sides
    plt.xticks([0, 1, 2, 3, 4],
           ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 1, 2, 3, 4, 5],
           ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    
    # Build the line graph.
    plt.plot(x_coords, y_coords, marker = 'o')
    
    #Display the line graph
    plt.show()
    
def bar_graph1():
    left_edges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]
    bar_width = 5

    plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'w', 'k'))
    plt.show()
    
def bar_chart(): #Program 7-24
    #bar chart accepts no arguments
    #it creates two lists for left edges
    #and bar heights and uses matplotlib to plot a bar chart
    
    #create a list for bar center and height
    left_edges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]
        
    #set bar width
    bar_width = 10
    
    #plot the chart
    plt.bar(left_edges, heights, bar_width,
        color = ('r', 'g', 'b', 'y', 'k'))
        
    #add a title
    plt.title('Sales by Year')
        
    #add labels for axes
    plt.xlabel('Year')
    plt.ylabel('Sales')
        
    #add custom tick marks
    plt.xticks([5, 15, 25, 35, 45],
                ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 100, 200, 300, 400, 500],
    ['$0m','$2m','$3m','$4m','$5m'])
        
    #show the chart
    plt.show()
        
def pie_chart(): #Program 7-27
    #pie chart accepts no arguments
    #it creates a list of values
    #and uses a matplotlib to plot a pie chart
    
    #set values
    values = [20, 60, 80, 40]
    
    #draw the pie chart
    plt.pie(values)
    
    #show the pie chart
    plt.show()

def pie_chart2(): #Program 7-28
    #pie chart accepts no arguments
    #it creates a list of values
    #and uses matplotlib to plot a pie chart
    
    #set values
    sales = [100, 400, 300, 600]
    
    #set slice labels
    slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']
    
    #set the pie colors
    plt.pie(sales, colors=('r', 'g', 'b', 'y', 'k'))
    
    #draw the pie chart
    plt.pie(sales, labels=slice_labels)
    
    #add a title
    plt.title('Sales by Quarter')
    
    #show the pie chart
    plt.show()
    
    
    