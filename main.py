import sys
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import networkx as nx
from numpy import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
import time





def nextGraph():
        global SetWT
        try:
            nextNode=[[0,0]]
            edgeColorsAnimation = []
            previousNode = 'something'

            i=0
            try:
                currentNode = listTables.get(listTables.curselection())

            except Exception as e:
                print(e)
                messagebox.showwarning(
                    'Error', "Please RESET the graph!")

            while 'Bucharest' not in currentNode:

                if DG.order() and i == 0:
                    description.config(text='Current Node-> ' +str(currentNode)+'\n' +'Next Node to choose-> ')
                    a.cla()
                    DG.clear()
                    print('BADDDD')
                    DG.add_node(listTables.get(listTables.curselection()),rank=0)
                    nx.draw_networkx(DG, pos, ax=a )
                    a.axis('off')
                    canvas.draw()
                    if SetWT == 1:
                        time.sleep(1)
                    i+=1
                else:
                    nodeNumber = currentNode.split(".")

                    y=0

                    for x in datasetCost[int(nodeNumber[0])-1]:

                        if x != -1 :# and datasetNamesB[y][0] != previousNode (add this to if for more performance)

                            DG.add_weighted_edges_from([(currentNode, datasetNamesB[y][0], x)])
                            nx.draw_networkx_edge_labels(DG,pos,edge_labels=nx.get_edge_attributes(DG,'weight'),font_color='red',ax=a)

                            if datasetNamesB[y][0] == previousNode:
                                edgeColorsAnimation.append('r')
                            else:
                                edgeColorsAnimation.append('b')

                            if nextNode[0][0] == 0 and datasetNamesB[y][0] != previousNode: #check if next node to choose allready exists
                                nextNode = [[datasetNamesB[y][0],x+int(datasetNamesB[y][1])]]
                                description.config(text=description.cget('text')+str(nextNode[0][0]+' Cost: '+str(nextNode[0][1])))
                            elif x+int(datasetNamesB[y][1])< nextNode[0][1] and datasetNamesB[y][0] != previousNode: # choose the smallest cost node to Bucharest
                                nextNode = [[datasetNamesB[y][0],x+int(datasetNamesB[y][1])]]
                                description.config(text=description.cget('text')+' > '+str(nextNode[0][0]+' Cost: '+str(nextNode[0][1])))

                            nx.draw_networkx(DG, pos, ax=a,edge_color=edgeColorsAnimation)
                            canvas.draw()

                            if SetWT == 1:
                                time.sleep(1)
                        y+=1

                    previousNode = currentNode
                    currentNode = nextNode[0][0]
                    description.config(text=description.cget('text')+'\n'+'Current Node-> ' +str(currentNode)+'\n' )
                    if 'Bucharest' not in currentNode:
                        description.config(text=description.cget('text')+'Next Node to choose-> ')

                    nextNode=[[0,0]]
                    if 'Bucharest' in currentNode:
                        DG.add_edges_from( [(currentNode,previousNode)] )
                        # edgeColorsAnimation.pop()
                        edgeColorsAnimation.append('r')
                        nx.draw_networkx(DG, pos, ax=a,edge_color=edgeColorsAnimation)
                        canvas.draw()
                        description.config(text=description.cget('text')+'Finish! ')


        except Exception as e:
            print(e)
            messagebox.showwarning(
                'Error', "Error: No selection!")
def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                # Fatal Python Error: PyEval_RestoreThread: NULL tstate
def resetGraph():

    if DG.order():
        a.cla()
        DG.clear()
        a.axis('off')
        for x in range(20):
            name = datasetNamesB[x][0]

            i = 0
            for y in datasetCost[x]:
                if y != -1:
                    DG.add_weighted_edges_from([(name, datasetNamesB[i][0], y)])
                i+=1
        nx.draw_networkx_edge_labels(DG,pos,edge_labels=nx.get_edge_attributes(DG,'weight'),edge_color='b',font_color='red',ax=a)
        nx.draw_networkx(DG, pos, ax=a,with_labels=False,edge_color='b')
        # for p in pos:  # raise text positions
        #     pos[p][1] += 0.07
        nx.draw_networkx_labels(DG,pos,font_size=10,ax=a)
        canvas.draw()

def setTime():
    global SetWT
    if SetWT == 1:
        SetWT = 0
        btime.config(text="Enable WaitTime")
    else:
        SetWT = 1
        btime.config(text="Disable WaitTime")


if __name__ == '__main__':
    global SetWT
    SetWT = 1

    root = tk.Tk()
    root.config(background='white')
    root.geometry("1000x700")

    f = Figure(figsize=(6, 6), dpi=100)
    a = f.add_subplot(111)
    a.axis('off')

    listTables = tk.Listbox(root, height=100,width=25)
    listTables.pack(side=tk.LEFT)
    # draw(listTables,a
    description= tk.Label(master=root, width=100)
    description.pack(side=tk.BOTTOM)

    #DataStart
    DG = nx.DiGraph()
    # datasetNames =[
    #     ['1.  Arad ',366]     ,['2.  Bucharest', 0]    ,['3.  Craiova ', 160]   ,['4.  Dobreta ', 242] ,['5.  Eforie ',161],
    #     ['6.  Fagaras ', 176] ,['7.  Giurgiu ', 77]    ,['8.  Hirsova ', 151]   ,['9.  Iasi ', 226]    ,['10. Lugoj ', 244],
    #     ['11. Mehadia ', 241] ,['12. Neamt ', 234]     ,['13. Oradea ', 380]    ,['14. Pitesti ', 10]  ,['15. Ramnicu Vilcea ', 193],
    #     ['16. Sibiu ', 253]   ,['17. Timisoara ', 392] ,['18. Urziceni ', 80]   ,['19. Vaslui ', 199]  ,['20. Zerind ', 374]
    # ]
    datasetNamesB =[
        ['1.  Arad [366]',366]     ,['2.  Bucharest', 0]         ,['3.  Craiova [160]', 160]  ,['4.  Dobreta [242]', 242] ,['5.  Eforie [161]',161],
        ['6.  Fagaras [176]', 176] ,['7.  Giurgiu [77]', 77]     ,['8.  Hirsova [151]', 151]  ,['9.  Iasi [226]', 226]    ,['10. Lugoj [244]', 244],
        ['11. Mehadia [241]', 241] ,['12. Neamt [234]', 234]     ,['13. Oradea [380]', 380]   ,['14. Pitesti [10]', 10]   ,['15. Ramnicu Vilcea [193]', 193],
        ['16. Sibiu [253]', 253]   ,['17. Timisoara [392]', 392] ,['18. Urziceni [80]', 80]   ,['19. Vaslui [199]', 199]  ,['20. Zerind [374]', 374]
    ]
    nr =[1  ,2  ,3  ,4  ,5  ,6  ,7  ,8  ,9  ,10 ,11 ,12 ,13 ,14 ,15 ,16 ,17 ,18 ,19 ,20 ]

    datasetCost =[
        [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,140,118,-1 ,-1 ,75 ],
        [-1 ,-1 ,-1 ,-1 ,-1 ,211,90 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,101,-1 ,-1 ,-1 ,85 ,-1 ,-1 ],
        [-1 ,-1 ,-1 ,120,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,138,146,-1 ,-1 ,-1 ,-1 ,-1 ],
        [-1 ,-1 ,120,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,75 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ],
        [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,85 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ],
        [-1 ,211,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,99 ,-1 ,-1 ,-1 ,-1 ],
        [-1 ,90 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ],
        [-1 ,-1 ,-1 ,-1 ,86 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,98 ,-1 ,-1 ],
        [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,87 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,92 ,-1 ],
        [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,70 ,-1 ,-1 ,-1 ,-1 ,-1 ,111,-1 ,-1 ,-1 ],
        [-1 ,-1 ,-1 ,75 ,-1 ,-1 ,-1 ,-1 ,-1 ,70 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ],
        [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,87 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ],
        [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,151,-1 ,-1 ,-1 ,71 ],
        [-1 ,101,138,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,97 ,-1 ,-1 ,-1 ,-1 ,-1 ],
        [-1 ,-1 ,145,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,97 ,-1 ,80 ,-1 ,-1 ,-1 ,-1 ],
        [140,-1 ,-1 ,-1 ,-1 ,99 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,151,-1 ,80 ,-1 ,-1 ,-1 ,-1 ,-1 ],
        [118,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,111,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ],
        [-1 ,85 ,-1 ,-1 ,-1 ,-1 ,-1 ,98 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,142,-1 ],
        [-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,92 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,142,-1 ,-1 ],
        [75 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,71 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ,-1 ],
    ]


    for x in range(20):
        name = datasetNamesB[x][0]
        listTables.insert('end', datasetNamesB[x][0]) #If you want nodes without [cost] replace all file  datasetNamesB with datasetNamesA
        i = 0
        for y in datasetCost[x]:
            if y != -1:
                DG.add_weighted_edges_from([(name, datasetNamesB[i][0], y)],pos=(53.5672, 10.0285))
            i+=1


    pos = nx.spring_layout(DG)
    nx.draw_networkx_edge_labels(DG,pos,edge_labels=nx.get_edge_attributes(DG,'weight'),font_color='red',ax=a)
    nx.draw_networkx(DG, pos,font_size=16, with_labels=False,edge_color='b',ax=a)
    # for p in pos:  # raise text positions
    #     pos[p][1] += 0.07
    nx.draw_networkx_labels(DG,pos,font_size=10,ax=a)




    # EndData
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
    bstart = tk.Button(root, text="Start",command=nextGraph,width=13)
    bstart.pack(side=tk.TOP)
    breset = tk.Button(root, text="Reset",command=resetGraph,width=13)
    breset.pack(side=tk.TOP)

    btime = tk.Button(master=root, text="Disable WaitTime",command=setTime,width=13)
    btime.pack(side=tk.TOP)
    button = tk.Button(master=root, text='Quit', command=_quit,width=13)
    button.pack(side=tk.TOP)


    root.mainloop()
