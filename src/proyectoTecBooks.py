import tkinter 
from tkinter import ttk
from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
from tkinter import filedialog


class Book:
   def __init__(self, title, author, year, genre, description, filename):
      self.title = title
      self.author = author
      self.year = year
      self.genre = genre
      self.description = description
      self.filename = filename



class Library:
   def __init__(self):
      self.root = tkinter.Tk()
      self.root.title("Librería TEC Books")
      self.root.geometry('1100x1000')
      nb = ttk.Notebook(self.root)
      #self.root.iconbitmap(r'C:\Users\valer\Downloads\icon_library.ico')
      self.books = []
      nb.pack(fill='both', expand='yes',)
      self.pl = tkinter.Frame(nb, background='#F4EEE1')
      self.p2 = tkinter.Frame(nb, background= '#E0D5CC')
   
      icono1 = Image.open("assets/icono1.jpeg")
      width, height = 64, 64
      icono1 = icono1.resize((width, height), Image.ANTIALIAS)
      icono1TK = ImageTk.PhotoImage(icono1)

      icono2 = Image.open("assets/icono2.png")
      width, height = 64, 64
      icono2 = icono2.resize((width, height), Image.ANTIALIAS)
      icono2TK = ImageTk.PhotoImage(icono2)

      icono3 = Image.open("assets/icono3.png")
      width, height = 64, 64
      icono3 = icono3.resize((width, height), Image.ANTIALIAS)
      icono3TK = ImageTk.PhotoImage(icono3)

      icono4 = Image.open("assets/icono4.jpeg")
      width, height = 64, 64
      icono4 = icono4.resize((width, height), Image.ANTIALIAS)
      icono4TK = ImageTk.PhotoImage(icono4)


      icono5 = Image.open("assets/icono5.jpg")
      width, height = 64, 64
      icono5 = icono5.resize((width, height), Image.ANTIALIAS)
      icono5TK = ImageTk.PhotoImage(icono5)


      nb.add(self.pl, text='Homepage')
      nb.add(self.p2, text='Menu')
   
      self.Label1 = ttk.Label(self.pl, text= 'Welcome to TecBooks Bookstore!', font= ('Times New Roman', 20), anchor= 'center', background='#F4EEE1')
      self.Label1.pack(pady=20)
      self.Label2 = ttk.Label(self.pl, text= 'Books added:', font= ('Times New Roman', 16), anchor= 'center', background='#F4EEE1')
      self.Label2.pack(pady=30)
      self.Label3 = ttk.Label(self.p2, text= 'Welcome to menu', font= ('Times New Roman', 20), anchor= 'center', background='#E0D5CC' )
      self.Label3.pack(pady=20)
      self.Label4 = ttk.Label(self.p2, text= 'Select what you want to do below:', font= ('Times New Roman', 16), anchor= 'center', background='#E0D5CC')
      self.Label4.pack(pady=30)
   
      self.boton1=ttk.Button(self.pl, compound="top", image=icono1TK, text="Orgullo y\n Prejuicio", command=self.openPDF1)
      self.boton1.place(relx=0.15, rely=0.25)

      self.boton2=ttk.Button(self.pl, compound="top", image=icono2TK, text="Diseño Lógico\n de Bases de Datos", command=self.openPDF2)
      self.boton2.place(relx=0.26, rely=0.25)
      
      self.boton3=ttk.Button(self.pl, compound="top", image=icono3TK, text="Los 7 Pasos para\n Aumentar tu Confianza", command=self.openPDF3)
      self.boton3.place(relx=0.4, rely=0.25)
      
      self.boton4=ttk.Button(self.pl, compound="top", image=icono4TK, text="Romeo et Juliette", command=self.openPDF4)
      self.boton4.place(relx=0.57, rely=0.25)

      self.boton5=ttk.Button(self.pl, compound="top", image=icono5TK, text="Una mirada a la Salud\n Mental de los Adolescentes", command=self.openPDF5)
      self.boton5.place(relx=0.7, rely=0.25)


      self.botonAdd=ttk.Button(self.p2, compound="top", text="Add book", command= self.addBook)
      self.botonAdd.pack(pady=50)
      self.botonDelete=ttk.Button(self.p2, compound="top", text="Delete book", command=self.deleteBook)
      self.botonDelete.place(relx=0.465, rely=0.3)
      self.botonConsult=ttk.Button(self.p2, compound="top", text="Consult books", command=self.searchBook)
      self.botonConsult.place(relx=0.4621, rely=0.343)

      def create_buttons(self):
         for i, book in enumerate(self.books):
            button = ttk.Button(self.root, compound="top", text=book.title, command=lambda book=book: self.openPDFX(self, book))
            button.place(relx=0.7, rely=0.25 + i * 0.1)

      self.root.mainloop()

   def openPDFX(self):
      for book in self.books:
         ventana_secundaria = tkinter.Toplevel()
         ventana_secundaria.title("Book to be read")
         ventana_secundaria.config(width=300, height=300)
         notebook = ttk.Notebook(ventana_secundaria)
         notebook.pack(fill=tkinter.BOTH, expand=True)
   
         pdf_frame = tkinter.Frame(notebook)
         pdf_frame.pack(fill=tkinter.BOTH, expand=True)
         pdf = open(book.filename, 'rb')
         reader = PyPDF2.PdfReader(pdf)
   
         text_widget = tkinter.Text(pdf_frame)
         text_widget.pack(fill=tkinter.BOTH, expand=True)
   
         for page in range(len(reader.pages)):
            infoPage = reader._get_page(page)
            extractInfo = infoPage.extract_text()
            numPage = "Page: ", page + 1
      
            text_widget.insert(tkinter.END, f"----\n{extractInfo}\n{numPage}\n*********\n\n")
   
         notebook.add(pdf_frame, text="Book to be read")
   
         metadataFrame = tkinter.Frame(notebook)
         notebook.add(metadataFrame, text="Book metadata")

         metadataEditable = tkinter.Text(metadataFrame)
         metadataEditable.pack(fill=tkinter.BOTH, expand=True)

         initialText = "Book metadata: \nTitle: {book.title} \nAuthor: {book.author} \nISBN Code: {book.code} \nGenre: {book.genre} \n\nSummary: {book.description}"
         metadataEditable.insert(tkinter.END, initialText)
         try:
            with open('text/texto_guardado1.txt', 'r') as file:
               savedText = file.read()
               metadataEditable.delete("1.0", tkinter.END)
               metadataEditable.insert(tkinter.END, savedText)
         except FileNotFoundError:
            pass
   
      def saveText():
         with open('text/texto_guardado1.txt', 'w') as file:
         file.write(metadataEditable.get("1.0", tkinter.END))
         ventana_secundaria.destroy()
         ventana_secundaria.protocol("WM_DELETE_WINDOW", saveText)

   def openPDF1(self):
   ventana_secundaria = tkinter.Toplevel()
   ventana_secundaria.title("Book to be read")
   ventana_secundaria.config(width=300, height=300)
   notebook = ttk.Notebook(ventana_secundaria)
   notebook.pack(fill=tkinter.BOTH, expand=True)
   
   pdf_frame = tkinter.Frame(notebook)
   pdf_frame.pack(fill=tkinter.BOTH, expand=True)
   pdf = open('books/OrgulloYPrejuicio.pdf', 'rb')
   reader = PyPDF2.PdfReader(pdf)
   
   text_widget = tkinter.Text(pdf_frame)
   text_widget.pack(fill=tkinter.BOTH, expand=True)
   
   for page in range(len(reader.pages)):
         infoPage = reader._get_page(page)
         extractInfo = infoPage.extract_text()
         numPage = "Page: ", page + 1
      
         text_widget.insert(tkinter.END, f"----\n{extractInfo}\n{numPage}\n*********\n\n")
   
   notebook.add(pdf_frame, text="Book to be read")
   
   metadataFrame = tkinter.Frame(notebook)
   notebook.add(metadataFrame, text="Book metadata")

   metadataEditable = tkinter.Text(metadataFrame)
   metadataEditable.pack(fill=tkinter.BOTH, expand=True)

   initialText = "Book metadata: \nTitle: Orgullo y Prejuicio \nAuthor: Jane Austen \nISBN Code: 9781238709626 \nGenre: Romance \n\nSummary: En un pequeño pueblo inglés, la señora Bennet, una madre ansiosa por casar a sus cinco hijas, \nrecibe la noticia de que un hombre rico, el señor Bingley, ha llegado a la vecindad. \nLa familia Bennet asiste a un baile en la mansión Netherfield, donde la señorita Bennet, \nJane, y el señor Bingley parecen enamorarse. Sin embargo, la señorita Bennet más orgullosa y cautelosa, Elizabeth, se encuentra con el amigo del \nseñor Bingley, el señor Darcy, quien la encuentra poco atractiva y, a su vez, Elizabeth lo considera arrogante.  "
   metadataEditable.insert(tkinter.END, initialText)
   try:
      with open('text/texto_guardado1.txt', 'r') as file:
         savedText = file.read()
         metadataEditable.delete("1.0", tkinter.END)
         metadataEditable.insert(tkinter.END, savedText)
   except FileNotFoundError:
      pass
   
   def saveText():
      with open('text/texto_guardado1.txt', 'w') as file:
         file.write(metadataEditable.get("1.0", tkinter.END))
         ventana_secundaria.destroy()
   ventana_secundaria.protocol("WM_DELETE_WINDOW", saveText)
         
         

   def openPDF2(self):
      ventana_secundaria = tkinter.Toplevel()
      ventana_secundaria.title("Book to be read")
      ventana_secundaria.config(width=300, height=200)
      notebook = ttk.Notebook(ventana_secundaria)
      notebook.pack(fill=tkinter.BOTH, expand=True)
   
      pdf_frame = tkinter.Frame(notebook)
      pdf_frame.pack(fill=tkinter.BOTH, expand=True)
      pdf = open('books/BasesDeDatos.pdf', 'rb')
      reader = PyPDF2.PdfReader(pdf)
      text_widget = tkinter.Text(pdf_frame)
      text_widget.pack(fill=tkinter.BOTH, expand=True)
      for page in range(len(reader.pages)):
         infoPage = reader._get_page(page)
         extractInfo = infoPage.extract_text()
         numPage = "Page: ", page + 1
      
         text_widget.insert(tkinter.END, f"----\n{extractInfo}\n{numPage}\n*********\n\n")
   
      notebook.add(pdf_frame, text="Book to be read")

      metadataFrame = tkinter.Frame(notebook)
      notebook.add(metadataFrame, text="Book metadata")
      
      metadataEditable = tkinter.Text(metadataFrame)
      metadataEditable.pack(fill=tkinter.BOTH, expand=True)

      initialText = "Book metadata: \nTitle: Diseño Lógico de Bases de Datos \nAuthor: Xavier Burgués \nISBN Code: 9787538401320 \nGenre: Informatica \n\nSummary: En este libro, encontrarás todo tipo de información relacionada al diseño de bases de datos, como el diseño lógico, las trampas de diseño, la transformación del modelo conceptual en el modelo relacional, la normalización y sus prácticas."
      metadataEditable.insert(tkinter.END, initialText)
      try:
         with open('text/texto_guardado2.txt', 'r') as file:
            savedText = file.read()
            metadataEditable.delete("1.0", tkinter.END)
            metadataEditable.insert(tkinter.END, savedText)
      except FileNotFoundError:
         pass
   
      def saveText():
         with open('text/texto_guardado2.txt', 'w') as file:
            file.write(metadataEditable.get("1.0", tkinter.END))
            ventana_secundaria.destroy()
      ventana_secundaria.protocol("WM_DELETE_WINDOW", saveText)
         
      
   def openPDF3(self):
      ventana_secundaria = tkinter.Toplevel()
      ventana_secundaria.title("Book to be read")
      ventana_secundaria.config(width=300, height=200)
      notebook = ttk.Notebook(ventana_secundaria)
      notebook.pack(fill=tkinter.BOTH, expand=True)
   
      pdf_frame = tkinter.Frame(notebook)
      pdf_frame.pack(fill=tkinter.BOTH, expand=True)
      pdf = open('books/Confianza.pdf', 'rb')
      reader = PyPDF2.PdfReader(pdf)
      text_widget = tkinter.Text(pdf_frame)
      text_widget.pack(fill=tkinter.BOTH, expand=True)
      for page in range(len(reader.pages)):
         infoPage = reader._get_page(page)
         extractInfo = infoPage.extract_text()
         numPage = "Page: ", page + 1
      
         text_widget.insert(tkinter.END, f"----\n{extractInfo}\n{numPage}\n*********\n\n")
   
      notebook.add(pdf_frame, text="Book to be read")

      metadataFrame = tkinter.Frame(notebook)
      notebook.add(metadataFrame, text="Book metadata")

      metadataEditable = tkinter.Text(metadataFrame)
      metadataEditable.pack(fill=tkinter.BOTH, expand=True)

      initialText = "Book metadata: \nTitle: Los 7 Pasos para Aumentar tu Confianza \nAuthor: Mónica Fernández \nISBN Code: 9789689465130 \nGenre: Psychology \n\nSummary: ¿Cómo puedes aprender a tener una confianza insuperable? Leyendo este libro. Aquí te enseñaremos a cómo tener esa confianza que tanto has anhelado en tu vida. Conócete, cree en la positividad, reinicia tu mente, suelta, busca esa mejor versión de ti mismo aquí."
      metadataEditable.insert(tkinter.END, initialText)
      try:
         with open('text/texto_guardado3.txt', 'r') as file:
            savedText = file.read()
            metadataEditable.delete("1.0", tkinter.END)
            metadataEditable.insert(tkinter.END, savedText)
      except FileNotFoundError:
         pass
   
      def saveText():
         with open('text/texto_guardado3.txt', 'w') as file:
            file.write(metadataEditable.get("1.0", tkinter.END))
            ventana_secundaria.destroy()
      ventana_secundaria.protocol("WM_DELETE_WINDOW", saveText)
         

   def openPDF4(self):
      ventana_secundaria = tkinter.Toplevel()
      ventana_secundaria.title("Book to be read")
      ventana_secundaria.config(width=300, height=200)
      notebook = ttk.Notebook(ventana_secundaria)
      notebook.pack(fill=tkinter.BOTH, expand=True)
   
      pdf_frame = tkinter.Frame(notebook)
      pdf_frame.pack(fill=tkinter.BOTH, expand=True)
      pdf = open('books/Frances.pdf', 'rb')
      reader = PyPDF2.PdfReader(pdf)
      text_widget = tkinter.Text(pdf_frame)
      text_widget.pack(fill=tkinter.BOTH, expand=True)
      for page in range(len(reader.pages)):
         infoPage = reader._get_page(page)
         extractInfo = infoPage.extract_text()
         numPage = "Page: ", page + 1
      
         text_widget.insert(tkinter.END, f"----\n{extractInfo}\n{numPage}\n*********\n\n")
   
      notebook.add(pdf_frame, text="Book to be read")

      metadataFrame = tkinter.Frame(notebook)
      notebook.add(metadataFrame, text="Book metadata")

      metadataEditable = tkinter.Text(metadataFrame)
      metadataEditable.pack(fill=tkinter.BOTH, expand=True)

      initialText = "Book metadata: \nTitle: Romeo et Juliette \nAuthor: William Shakespeare \nISBN Code: 9788458002627 \nGenre: Idiom \n\nSummary: En este libro para practicar tu francés, verás una famosa tragedia escrita por William Shakespeare que narra la historia de dos jóvenes amantes cuyo amor prohibido desencadena una serie de eventos trágicos. Ambientada en la ciudad italiana de Verona, la obra explora los temas universales del amor, el destino y el conflicto entre familias rivales. A través de su profunda pasión y sacrificio, Romeo y Julieta se convierten en símbolos eternos del amor verdadero y la inevitabilidad de la tragedia. "
      metadataEditable.insert(tkinter.END, initialText)
      try:
         with open('text/texto_guardado4.txt', 'r') as file:
            savedText = file.read()
            metadataEditable.delete("1.0", tkinter.END)
            metadataEditable.insert(tkinter.END, savedText)
      except FileNotFoundError:
         pass
      
      def saveText():
         with open('text/texto_guardado4.txt', 'w') as file:
            file.write(metadataEditable.get("1.0", tkinter.END))
            ventana_secundaria.destroy()
      ventana_secundaria.protocol("WM_DELETE_WINDOW", saveText)


   
   def openPDF5(self):
      ventana_secundaria = tkinter.Toplevel()
      ventana_secundaria.title("Book to be read")
      ventana_secundaria.config(width=300, height=200)
      notebook = ttk.Notebook(ventana_secundaria)
      notebook.pack(fill=tkinter.BOTH, expand=True)
   
      pdf_frame = tkinter.Frame(notebook)
      pdf_frame.pack(fill=tkinter.BOTH, expand=True)
      pdf = open('books/SaludMental.pdf', 'rb')
      reader = PyPDF2.PdfReader(pdf)
      text_widget = tkinter.Text(pdf_frame)
      text_widget.pack(fill=tkinter.BOTH, expand=True)
      for page in range(len(reader.pages)):
         infoPage = reader._get_page(page)
         extractInfo = infoPage.extract_text()
         numPage = "Page: ", page + 1
      
         text_widget.insert(tkinter.END, f"----\n{extractInfo}\n{numPage}\n*********\n\n")
   
      notebook.add(pdf_frame, text="Book to be read")

      metadataFrame = tkinter.Frame(notebook)
      notebook.add(metadataFrame, text="Book metadata")
      metadataEditable = tkinter.Text(metadataFrame)
      metadataEditable.pack(fill=tkinter.BOTH, expand=True)

      initialText = "Book metadata: \nTitle: Una Mirada a la Salud Mental de los Adolescentes \nAuthor: Argyris Stringaris \nISBN Code: 9788458379521 \nGenre: Psychology \n\nSummary: En este libro hay conocimiento para fomentar valores y hábitos saludables. Encontrarás más de 1.000 consejos de salud clasificados en cinco grupos distintos de edad y temáticas variadas, desde la alimentación hasta información sobre enfermedades o sobre el comportamiento y el aprendizaje."
      metadataEditable.insert(tkinter.END, initialText)
      try:
         with open('text/texto_guardado5.txt', 'r') as file:
            savedText = file.read()
            metadataEditable.delete("1.0", tkinter.END)
            metadataEditable.insert(tkinter.END, savedText)
      except FileNotFoundError:
         pass
      
      def saveText():
         with open('text/texto_guardado5.txt', 'w') as file:
            file.write(metadataEditable.get("1.0", tkinter.END))
            ventana_secundaria.destroy()
      ventana_secundaria.protocol("WM_DELETE_WINDOW", saveText)




   def addBook(self):
      ventana_secundaria = tkinter.Toplevel()
      ventana_secundaria.title("Add a Book")
      ventana_secundaria.geometry('500x400')

      code = ttk.Label(ventana_secundaria, text="Book's code?")
      code.place(relx=0.5, rely=0.1, anchor="center")
      codeEntry = ttk.Entry(ventana_secundaria, width=20)
      codeEntry.place(relx=0.5, rely=0.15, anchor="center")
      title = ttk.Label(ventana_secundaria, text="Book's name?")
      title.place(relx=0.5, rely=0.2, anchor="center")
      titleEntry = ttk.Entry(ventana_secundaria, width=20)
      titleEntry.place(relx=0.5, rely=0.25, anchor="center")
      author = ttk.Label(ventana_secundaria, text="Author?")
      author.place(relx=0.5, rely=0.3, anchor="center")
      authorEntry = ttk.Entry(ventana_secundaria, width=20)
      authorEntry.place(relx=0.5, rely=0.35, anchor="center")
      genre = ttk.Label(ventana_secundaria, text="Book's genre?")
      genre.place(relx=0.5, rely=0.4, anchor="center")
      genre2 = ttk.Label(ventana_secundaria, text="1 for romance, 2 for psychology, 3 for languages, 4 for informatica, 5 for comedy, 6 for science fiction, 7 for adventure, 8 for drama, 9 for horror, 10 for science, 11 for history")
      genre2.place(relx=0.5, rely=0.45, anchor="center")
      genreEntry = ttk.Entry(ventana_secundaria, width=20)
      genreEntry.place(relx=0.5, rely=0.5, anchor="center")
      description = ttk.Label(ventana_secundaria, text="Enter the book's description in the desired language")
      description.place(relx=0.5, rely=0.55, anchor="center")
      descriptionEntry = ttk.Entry(ventana_secundaria, width=20)
      descriptionEntry.place(relx=0.5, rely=0.6, anchor="center")
      numPages = ttk.Label(ventana_secundaria, text="Number of pages")
      numPages.place(relx=0.5, rely=0.65, anchor="center")
      pagesEntry = ttk.Entry(ventana_secundaria, width=20)
      pagesEntry.place(relx=0.5, rely=0.7, anchor="center")
      

      selected_book_label = ttk.Label(ventana_secundaria, text="Selected book: ")
      selected_book_label.place(relx=0.5, rely=0.75, anchor="center")
      
      # change selected book label contents
      selected_book_label.configure(text="Selected book: "+titleEntry.get())
      
      # Function for opening the
      # file explorer window
      filename = ""
      def browseFiles():
         global filename
         filename = filedialog.askopenfilename(initialdir = "/",
                                                title = "Select a File",
                                                filetypes = (("PDF files",
                                                            "*.pdf"),
                                                            ("all files",
                                                            "*.*")))
         print("Selected file: ", filename)
         updateSelectedBook()

      def updateSelectedBook():
            selected_book_label.configure(text="File Opened: " + filename)

      # BUTTON TO OPEN THE FILE EXPLORER
      button_explore = Button(ventana_secundaria, text = "Browse Files", command = browseFiles)
      button_explore.place(relx=0.5, rely=0.8, anchor="center")

      
      

      def saveBook():
         title = titleEntry.get()
         author = authorEntry.get()
         genre = genreEntry.get()
         description = descriptionEntry.get()
         pages = int(pagesEntry.get())
         code = int(codeEntry.get())
         filename = filename.get()
         print(title, author, genre, description, pages, code)
         global book
         book = Book(title, author, genre, description, pages, code, filename)
         self.books.append(book)

   def deleteBook(self):
      ventana_secundaria = tkinter.Toplevel()
      ventana_secundaria.title("Delete a Book")
      ventana_secundaria.config(width=300, height=200)
      notebook = ttk.Notebook(ventana_secundaria)
      notebook.pack(fill=tkinter.BOTH, expand=True)



   def searchBook(self):
      ventana_secundaria = tkinter.Toplevel()
      ventana_secundaria.title("Consult a Book")
      ventana_secundaria.config(width=300, height=200)
      notebook = ttk.Notebook(ventana_secundaria)
      notebook.pack(fill=tkinter.BOTH, expand=True)


aplicacion1 = Library()