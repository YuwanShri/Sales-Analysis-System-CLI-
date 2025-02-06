import matplotlib.pylab as plt
import pandas as pd
from abc import ABC, abstractmethod

class Analysis(ABC):
    @abstractmethod
    def  performAnalysis():
        pass

class BranchAnalysis(Analysis):
    def  performAnalysis(self):
        # load data set into panda frame
        df = pd.read_csv('C:\Sampath Food City\Sampath Food City\APDP\sales.csv')  
        # summarize filtered data to find total quantity for each branch
        result = df.groupby ('Branch')['Quantity'].sum().reset_index()
        print (result)   # print summary
        # Draw Bar Chart - Branches for X Axis  Total Quantities for Y Axis                     
        plt.bar (result['Branch'], result['Quantity'],width=0.6,color=['pink','lightblue', 'purple'] )
        plt.xlabel("Branches")
        plt.ylabel("Sales Quantity")
        plt.title("Sales Analysis By Branch")
        plt.show()



class WeeklyAnalysis(Analysis):
    def  performAnalysis(self):
        # load data file into panda frame
        df = pd.read_csv('C:\Sampath Food City\Sampath Food City\APDP\sales.csv')
        # input first day of the week 
        day1 =  int (input("Enter the starting day of the week (1 for Monday, 7 for Sunday): "))
        # filter data for 7 days starting from input day
        day2 = day1 + 6
        filtered_df = df.loc[(df['Day'] >=day1) & (df['Day']<=day2) ]
        # add up sales quantities for each branch
        result = filtered_df.groupby('Branch')['Quantity'].sum().reset_index()
        # display summary result in tabular form
        print("****** Total sales for each branch during the selected week:")
        print(result)  
        # draw bar chart - branches for X axis , quantities for Y axis
        plt.bar(result['Branch'], result['Quantity'], width=0.6, color=['blue', 'green', 'salmon'])
        plt.xlabel("Branches")
        plt.ylabel("Sales Quantity")
        plt.title("Sales Analysis By Branch for the Selected Week")
        plt.show()
        

class PriceAnalysis(Analysis):
    def  performAnalysis(self):
        df = pd.read_csv('C:\Sampath Food City\Sampath Food City\APDP\sales.csv')  # load data file into panda frame
        product =  input ("Enter Product name  |")
        filtered_df = df.loc[(df['Product'] == product )]
        x = filtered_df["Day"]
        y = filtered_df["Price"]
        print (filtered_df)
        plt.plot(x, y, marker ='o' )
        plt.xlabel(product)
        plt.ylabel("Price")
        plt.title ("Price Analysis of a given Product")
        plt.show()

# Preference Analysis
class PreferenceAnalysis(Analysis):
    def performAnalysis(self):
        # Load dataset into a Pandas DataFrame
        df = pd.read_csv('C:\Sampath Food City\Sampath Food City\APDP\sales.csv')
        
        # Summarize total quantity sold for each product
        result = df.groupby('Product')['Quantity'].sum().reset_index()
        
        # Sort products by total quantity sold (most preferred first)
        result = result.sort_values(by='Quantity', ascending=False).reset_index(drop=True)
        
        # Print product preference summary
        print("* * * * * * PRODUCT PREFERENCE ANALYSIS * * * * * * ")
        print(result)
        
        # Plot bar chart for product preferences
        plt.bar(result['Product'], result['Quantity'], width=0.6, color=['Cyan', 'yellow', 'pink', 'green'])
        plt.xlabel("Products")
        plt.ylabel("Total Quantity Sold")
        plt.title("Most Preferred Products")
        plt.show()


# Distribution Analysis
class DistributionAnalysis(Analysis):
    def performAnalysis(self):
        # Load dataset into a Pandas DataFrame
        df = pd.read_csv('C:\Sampath Food City\Sampath Food City\APDP\sales.csv')
        
        # Calculate total sales amount for each branch (Price * Quantity)
        df['Total Sales'] = df['Price'] * df['Quantity']
        result = df.groupby('Branch')['Total Sales'].sum().reset_index()
        
        # Print sales distribution summary
        print("* * * - - - Branch-Wise Sales Distribution Summary - - - * * *")
        print(result)
        
        # Plot pie chart for total sales amounts by branch
        plt.pie(result['Total Sales'], labels=result['Branch'], autopct='%1.1f%%', colors=['red', 'Cyan', 'green'])
        plt.title("Branch-Wise Sales Distribution")
        plt.show()


class  ProcessStrategy:
    def  executeStrategy( self, analysis_object ):
        analysis_object.performAnalysis()

class  StrategySelector:                                           
    def  openMenu(self):
        while (True):
            print ("Sampath Food City - Sales Analysis")
            print ("1 - Analysis By Branch")
            print ("2 - Weekly Analysis")
            print ("3 - Price Analysis of Products")
            print ("4 - Product Preference Analysis")
            print ("5 - Distribution Analysis")
            print ("6 - Exit")
            choice = int ( input ("Enter Choice [1|2|3|4|5|6] | "))
            if (choice<1  or choice>6):
                print ("* * * Invalid Choice . . . ! ! !")
            else:
                ps = ProcessStrategy()
                if (choice==1):
                    branchAnalysisObj =  BranchAnalysis()
                    ps.executeStrategy(branchAnalysisObj)
                if (choice ==2):
                    weeklyAnalysisObj = WeeklyAnalysis()
                    ps.executeStrategy(weeklyAnalysisObj)
                if (choice ==3):
                    pa = PriceAnalysis()
                    ps.executeStrategy(pa)
                if (choice == 4):
                    pf = PreferenceAnalysis()
                    ps.executeStrategy(pf)
                if (choice ==5):
                    da = DistributionAnalysis()
                    ps.executeStrategy(da)
                if (choice ==6):
                    break;
        print ("- - - - * END * - - - -")
    

class  Admin:
    count=0
    def  __init__(self, un, pw):
        if  (Admin.count==0):
            self.username = un
            self.password = pw
            Admin.count = Admin.count + 1
        else:
            print ("* * * Admin already exists* * *")
    
    def  logon(self):
        un = input ("Enter User Name -: ")
        pw= input ("Enter Password -: ")
        if  (un == self.username and pw == self.password):
            s1 = StrategySelector()
            s1.openMenu()
        else:
            print ("* * * Incorrect User Name OR Password..! ! !")
            
    
# main
a1 = Admin("yuwan", "123")
a1.logon()
