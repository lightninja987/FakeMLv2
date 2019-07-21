from tkinter import *


def graphics(text):
    if text == "['REAL']":
        root = Tk()

        text1 = Text(root, height=100, width=100)
        text1.insert(END,'\n')
        
        
        text2 = Text(root, height=100, width=100)
        scroll = Scrollbar(root, command=text2.yview)
        text2.configure(yscrollcommand=scroll.set)
        text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        text2.tag_configure('big', font=('Arial', 20, 'bold'))
        text2.tag_configure('color', foreground='#476042', 
        						font=('Arial', 12, 'bold'))
        text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
        text2.insert(END,'\nPrediction: Real News\n', 'big')
        quote = """
        The news article has been classified as real. While the facts in this article may not be 
        completely true, it is also not misleading or manipulative. The article includes primary sources
        and can most likely be verified. Overall, this news should not be flagged for being fake or 
        misleading, however you should still fact check this article.
        """
        text2.insert(END, quote, 'color')
        text2.insert(END, '\n', 'follow')
        text2.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)
        root.mainloop()
    else:
        root = Tk()

        text1 = Text(root, height=100, width=100)
        text1.insert(END,'\n')
        
        
        text2 = Text(root, height=100, width=100)
        scroll = Scrollbar(root, command=text2.yview)
        text2.configure(yscrollcommand=scroll.set)
        text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
        text2.tag_configure('big', font=('Arial', 20, 'bold'))
        text2.tag_configure('color', foreground='#ff3300', 
        						font=('Arial', 12, 'bold'))
        text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END, "Not now, maybe later!"))
        text2.insert(END,'\nPrediction: Fake News\n', 'big')
        quote = """
        This news article has been classified as fake. While the facts found in this article might be
        truthful, it's intent is to be misleading and manipulative. The article can most likely not be
        verified or contain any primary sources. Overall, this news article should be flagged for concern.
        """ 
        text2.insert(END, quote, 'color')
        text2.insert(END, '\n', 'follow')
        text2.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)
        root.mainloop()
