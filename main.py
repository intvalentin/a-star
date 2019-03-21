import sys
from tkinter import *
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
        try:
            nextNode=[[0,0]]
            i=0
            try:
                currentNode = listTables.get(listTables.curselection())
            
            except Exception as e:
                print(e)
                messagebox.showwarning(
                    'Error', "Please RESET the graph!")
            while currentNode != '2.  Bucharest':

                if DG.order() and i == 0:
                    a.cla()
                    DG.clear()
                    DG.add_node(listTables.get(listTables.curselection()))
                    nx.draw_networkx(DG, pos, ax=a)
                    a.axis('off')
                    canvas.draw()
                    time.sleep(2)
                    i+=1
                else:
                    nodeNumber = currentNode.split(". ")

                    y=0
                    for x in datasetCost[int(nodeNumber[0])-1]:

                        if x != -1:
                            DG.add_weighted_edges_from([(currentNode, datasetNames[y][0], x)],length=x)

                            nx.draw_networkx_labels(DG,pos,ax=a)
                            nx.draw_networkx_edge_labels(DG,pos,edge_labels=nx.get_edge_attributes(DG,'weight'),font_color='red',edge_color='r',ax=a)
                            nx.draw_networkx(DG, pos, ax=a)
                            canvas.draw()
                            time.sleep(1)
                            if nextNode[0][0] == 0:
                                nextNode = [[datasetNames[y][0],x+int(datasetNames[y][1])]]
                                print(nextNode)

                            elif x+int(datasetNames[y][1])< nextNode[0][1]:
                                nextNode = [[datasetNames[y][0],x+int(datasetNames[y][1])]]
                                print(nextNode)
                        y+=1
                    currentNode = nextNode[0][0]
                    print('currentNode : '+currentNode)







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
            name = datasetNames[x][0]

            i = 0
            for y in datasetCost[x]:
                if y != -1:
                    DG.add_weighted_edges_from([(name, datasetNames[i][0], y)])
                i+=1
        nx.draw_networkx_edge_labels(DG,pos,edge_labels=nx.get_edge_attributes(DG,'weight'),font_color='red',edge_color='r',ax=a)
        nx.draw_networkx(DG, pos, ax=a)
        canvas.draw()



if __name__ == '__main__':


    root = Tk()
    root.config(background='white')
    root.geometry("1000x700")

    f = Figure(figsize=(5, 4), dpi=100)
    a = f.add_subplot(111)
    a.axis('off')

    listTables = Listbox(root, height=30)
    listTables.pack(side=LEFT)
    # draw(listTables,a)
    description= Label(master=root, width=100)
    description.pack(side=TOP)

    #DataStart
    DG = nx.DiGraph()
    datasetNames =[
        ['1.  Arad',366]     ,['2.  Bucharest', 0]   ,['3.  Craiova', 160]  ,['4.  Dobreta', 242] ,['5.  Eforie',161],
        ['6.  Fagaras', 176] ,['7.  Giurgiu', 77]    ,['8.  Hirsova', 151]  ,['9.  Iasi', 226]    ,['10. Lugoj', 244],
        ['11. Mehadia', 241] ,['12. Neamt', 234]     ,['13. Oradea', 380]   ,['14. Pitesti', 10]  ,['15. Ramnicu Vilcea', 193],
        ['16. Sibiu', 253]   ,['17. Timisoara', 392] ,['18. Urziceni', 80]  ,['19. Vaslui', 199]  ,['20. Zerind', 374]
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
        name = datasetNames[x][0]
        listTables.insert(END, datasetNames[x][0])
        i = 0
        for y in datasetCost[x]:
            if y != -1:
                DG.add_weighted_edges_from([(name, datasetNames[i][0], y)])
            i+=1
    # print(DG.nodes())
    # print('number of nodes in the graph:', DG.number_of_nodes())

    pos = nx.spring_layout(DG,weight=300)
    nx.draw_networkx(DG, pos,font_size=16, with_labels=False,ax=a)
    nx.draw_networkx_labels(DG,pos,ax=a)
    nx.draw_networkx_edge_labels(DG,pos,edge_labels=nx.get_edge_attributes(DG,'weight'),font_color='red',edge_color='r',ax=a)
    # EndData
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)
    b = Button(root, text="Start",command=nextGraph,width=10)
    b.pack(side=TOP)
    b = Button(root, text="Reset",command=resetGraph,width=10)
    b.pack(side=TOP)

    button = Button(master=root, text='Quit', command=_quit,width=10)
    button.pack(side=TOP)


    root.mainloop()
