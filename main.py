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
from  draw import draw,aStar



def nextGraph():
        try:
            neighbors = [n for n in DG.neighbors(listTables.get(listTables.curselection()))]
            print(neighbors)
            print("gggg")
        except Exception as e:
            print(e)
            messagebox.showwarning(
                'Error', "Something wrong with DataBase!")
def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                # Fatal Python Error: PyEval_RestoreThread: NULL tstate

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
        '1.  Arad'    ,'2.  Bucharest' ,'3.  Craiova'  ,'4.  Dobreta' ,'5.  Eforie'         ,
        '6.  Fagaras' ,'7.  Giurgiu'   ,'8.  Hirsova'  ,'9.  Iasi'    ,'10. Lugoj'          ,
        '11. Mehadia' ,'12. Neamt'     ,'13. Oradea'   ,'14. Pitesti' ,'15. Ramnicu Vilcea' ,
        '16. Sibiu'   ,'17. Timisoara' ,'18. Urziceni' ,'19. Vaslui'  ,'20. Zerind'
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
        name = datasetNames[x]
        listTables.insert(END, datasetNames[x])
        i = 0
        for y in datasetCost[x]:
            if y != -1:
                DG.add_weighted_edges_from([(name, datasetNames[i], y)])
            i+=1
    # print(DG.nodes())
    # print('number of nodes in the graph:', DG.number_of_nodes())
    pos = nx.spring_layout(DG,weight=300)
    nx.draw_networkx(DG, pos,font_size=16, with_labels=False,ax=a)
    nx.draw_networkx_labels(DG,pos,ax=a)
    nx.draw_networkx_edge_labels(DG,pos,edge_labels=nx.get_edge_attributes(DG,'weight'),font_color='red',ax=a)
    # EndData
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)
    b = Button(root, text="next",command=nextGraph,width=10)
    b.pack(side=TOP)

    button = Button(master=root, text='Quit', command=_quit,width=10)
    button.pack(side=TOP)


    root.mainloop()
