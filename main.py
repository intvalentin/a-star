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
            while True:
                if DG.order() and i == 0:
                    description.config(text='Current Node-> ' +str(currentNode)+'\n' +'Next Node to choose-> ')
                    a.cla()
                    DG.clear()
                    DG.add_node(listTables.get(listTables.curselection()),rank=0)
                    nx.draw_networkx(DG, pos, ax=a )
                    a.axis('off')
                    canvas.draw()
                    time.sleep(1)
                    i+=1
                else:
                    nodeNumber = currentNode.split(". ")

                    y=0

                    for x in datasetCost[int(nodeNumber[0])-1]:

                        if x != -1:

                            DG.add_weighted_edges_from([(currentNode, datasetNames[y][0], x)],length=x)
                            nx.draw_networkx_edge_labels(DG,pos,edge_labels=nx.get_edge_attributes(DG,'weight'),font_color='red',ax=a)
                            if datasetNames[y][0] == previousNode:
                                edgeColorsAnimation.append('g')
                            else:
                                edgeColorsAnimation.append('r')

                            if nextNode[0][0] == 0 and datasetNames[y][0] != previousNode: #check if next node to choose allready exists
                                nextNode = [[datasetNames[y][0],x+int(datasetNames[y][1])]]
                                description.config(text=description.cget('text')+str(nextNode[0][0]+' Cost: '+str(nextNode[0][1])))
                            elif x+int(datasetNames[y][1])< nextNode[0][1] and datasetNames[y][0] != previousNode: # choose the smallest cost node to bucharest
                                nextNode = [[datasetNames[y][0],x+int(datasetNames[y][1])]]
                                description.config(text=description.cget('text')+' > '+str(nextNode[0][0]+' Cost: '+str(nextNode[0][1])))

                            nx.draw_networkx(DG, pos, ax=a,edge_color=edgeColorsAnimation)
                            canvas.draw()
                            time.sleep(1)
                        y+=1

                    previousNode = currentNode
                    currentNode = nextNode[0][0]
                    description.config(text=description.cget('text')+'\n'+'Current Node-> ' +str(currentNode)+'\n' )
                    if currentNode != '2.  Bucharest':
                        description.config(text=description.cget('text')+'Next Node to choose-> ')

                    nextNode=[[0,0]]
                    if currentNode == '2.  Bucharest':
                        break

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
        nx.draw_networkx_edge_labels(DG,pos,edge_labels=nx.get_edge_attributes(DG,'weight'),edge_color='r',ax=a)
        nx.draw_networkx(DG, pos, ax=a,with_labels=False,edge_color='g')
        # for p in pos:  # raise text positions
        #     pos[p][1] += 0.07
        nx.draw_networkx_labels(DG,pos,ax=a)
        canvas.draw()



if __name__ == '__main__':


    root = tk.Tk()
    root.config(background='white')
    root.geometry("1000x700")

    f = Figure(figsize=(5, 4), dpi=100)
    a = f.add_subplot(111)
    a.axis('off')

    listTables = tk.Listbox(root, height=100)
    listTables.pack(side=tk.LEFT)
    # draw(listTables,a
    description= tk.Label(master=root, width=100)
    description.pack(side=tk.BOTTOM)

    #DataStart
    DG = nx.DiGraph()
    datasetNames =[
        ['1.  Arad [366]',366]     ,['2.  Bucharest', 0]   ,      ['3.  Craiova [160]', 160]  ,['4.  Dobreta [242]', 242] ,['5.  Eforie [161]',161],
        ['6.  Fagaras [176]', 176] ,['7.  Giurgiu [77]', 77]    , ['8.  Hirsova [151]', 151]  ,['9.  Iasi [226]', 226]    ,['10. Lugoj [244]', 244],
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
        name = datasetNames[x][0]
        listTables.insert('end', datasetNames[x][0])
        i = 0
        for y in datasetCost[x]:
            if y != -1:
                DG.add_weighted_edges_from([(name, datasetNames[i][0], y)])
            i+=1


    pos = nx.spring_layout(DG,fixed = None)
    nx.draw_networkx_edge_labels(DG,pos,edge_labels=nx.get_edge_attributes(DG,'weight'),ax=a)

    nx.draw_networkx(DG, pos,font_size=16, with_labels=False,edge_color='g',ax=a)
    # for p in pos:  # raise text positions
    #     pos[p][1] += 0.07
    nx.draw_networkx_labels(DG,pos,ax=a)



    # EndData
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
    bstart = tk.Button(root, text="Start",command=nextGraph,width=10)
    bstart.pack(side=tk.TOP)
    breset = tk.Button(root, text="Reset",command=resetGraph,width=10)
    breset.pack(side=tk.TOP)

    button = tk.Button(master=root, text='Quit', command=_quit,width=10)
    button.pack(side=tk.TOP)


    root.mainloop()
