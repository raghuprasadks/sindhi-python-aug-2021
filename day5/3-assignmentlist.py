"""
Refer to IPLDashboard
name	team	season	runs	wickets

1. Find the total runs for all seasons
2. Find the highest run getter for a given season
3. Find the highest wicket taker for a given season
By getting the required user inputs
"""
ipldashboard=[]
header=['name','team','reason','runs','wickets']
player1=['virat','rcb',2020,500,0]
player2=['abd','rcb',2020,450,0]
player3=['jadeja','csk',2020,400,10]
player4=['rohit','mi',2020,499,4]
player5=['virat','rcb',2019,550,0]
player6=['abd','rcb',2019,480,0]
player7=['jadeja','csk',2019,450,12]
player8=['rohit','mi',2019,599,4]
ipldashboard.append(header)
ipldashboard.append(player1)
ipldashboard.append(player2)
ipldashboard.append(player3)
ipldashboard.append(player4)
ipldashboard.append(player5)
ipldashboard.append(player6)
ipldashboard.append(player7)
ipldashboard.append(player8)
print('ipl dashboard ',ipldashboard)

totalruns=0
maxrunsforseason=0
maxrungetter=''
season=int(input("Enter season"))
for i in range(len(ipldashboard)):
    #print(i)
    if(i==0):
        continue
    playerinfo = ipldashboard[i]
    totalruns = totalruns +playerinfo[3]  
    if (season ==playerinfo[2]):
        if(playerinfo[3]>maxrunsforseason):
            maxrunsforseason=playerinfo[3]
            maxrungetter = playerinfo[0]            
print('total runs for all seasons ',totalruns)
print('season ',season,'Maximum run getter ',maxrungetter, ' maximum runs',maxrunsforseason)


    










