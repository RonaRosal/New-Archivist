        
#-----Statement of Authorship----------------------------------------#
#
#  This is an iindividual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: N10360387
#    Student name:RONA MAE ROSAL
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/). [1PT9102]
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  News Archivist
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface development to produce a useful
#  application for maintaining and displaying archived news or
#  current affairs stories on a topic of your own choice.  See the
#  instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  You should be able to complete this assignment using
# these functions only.

# Import the function for opening a web document given its URL.
from urllib.request import urlopen

# Import the function for finding all occurrences of a pattern
# defined via a regular expression, as well as the "multiline"
# and "dotall" flags.
from re import findall, MULTILINE, DOTALL

# A function for opening an HTML document in your operating
# system's default web browser. We have called the function
# "webopen" so that it isn't confused with the "open" function
# for writing/reading local text files.
from webbrowser import open as webopen

# A module with useful functions on pathnames including:
# normpath: function for 'normalising' a  path to a file to the path-naming
# conventions used on this computer.  Apply this function to the full name
# of your HTML document so that your program will work on any operating system.
# exists: returns True if the supplied path refers to an existing path
from os.path import *

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your HTML document.
from os import getcwd
 
# Import the standard Tkinter GUI functions.
from tkinter import *

# Import the SQLite functions.
from sqlite3 import *

# Import the date and time function.
from datetime import datetime

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.


# Name of the folder containing your archived web documents.  When
# you submit your solution you must include the web archive along with
# this Python program. The archive must contain one week's worth of
# downloaded HTML/XML documents. It must NOT include any other files,
# especially image files.
internet_archive = 'InternetArchive'


############### PUT YOUR SOLUTION HERE #################

#create the canvas
window = Tk()
#Change canvas title and resize
window.title('News Archivist')
window.geometry('950x400')
window.configure(background = 'white')


# Import and add image for GUI
journal_image = PhotoImage(file = 'wallstreet.gif')
gui_image = Label(window, image = journal_image)
gui_image.grid(column = 1, rowspan = 20)

#create a initial display area for the chosen dates
Display_text = Label(window,width = '35',text = 'CHOOSE A DATE TO EXTRACT',
                 bg = 'yellow',relief = 'groove', font=('bold arial',8))
Display_text.grid(column = 2, row = 1, padx = 5)


#script for downloading the latest news
#This code is written by Donna Teague
def download(url = 'https://www.wsj.com/news/world',
     target_filename = 'Internetarchive/Latest News',
     filename_extension = 'html'):
        Display_text['text']= 'Latest News archived succesfully'
    # Import the function for opening online documents
        from urllib.request import urlopen

        # Import an exception raised when a web server denies access
        # to a document
        from urllib.error import HTTPError

        # Open the web document for reading
        try:
            web_page = urlopen(url)
        except ValueError:
            raise Exception("Download error - Cannot find document at URL '" + url + "'")
        except HTTPError:
            raise Exception("Download error - Access denied to document at URL '" + url + "'")
        except:
            raise Exception("Download error - Something went wrong when trying to download " + \
                            "the document at URL '" + url + "'")

        # Read its contents as a Unicode string
        try:
            web_page_contents = web_page.read().decode('UTF-8')
        except UnicodeDecodeError:
            raise Exception("Download error - Unable to decode document at URL '" + \
                            url + "' as Unicode text")

        # Write the contents to a local text file as Unicode
        # characters (overwriting the file if it
        # already exists!)
        try:
            text_file = open(target_filename + '.' + filename_extension,
                             'w', encoding = 'UTF-8')
            text_file.write(web_page_contents)
            text_file.close()
        except:
            raise Exception("Download error - Unable to write to file '" + \
                            target_file + "'")

        # Return the downloaded document to the caller
        return web_page_contents

    #-----------------------------------------------------------
    #
    # A main program to call the function.  If you want to download a
    # specific web document, add its URL as the function's argument.
    #
        download()

        
#variable used to interact widgets
select = IntVar()

#function to dispaly the selected date in the status bar
def display_text():
        global select    

        if select.get() == 1:
                Display_text['text']= 'May 12 2019 '

        elif select.get() == 2:
                Display_text['text']= 'May 13 2019'

        elif select.get() == 3:
                Display_text['text']= 'May 14 2019'

        elif select.get() == 4:
                Display_text['text']= 'May 15 2019'

        elif select.get() == 5:
                Display_text['text']= 'May 16 2019'

        elif select.get() == 6:
                Display_text['text']= 'May 17 2019'

        elif select.get() == 7:
                Display_text['text']= 'May 19 2019'

        elif select.get() == 8:
                Display_text['text'] = 'Latest News'

#Function to activate and manipulate widgets button.                
def extract_html():
        selected_date = select.get()

        if selected_date == 1:
                date = 'May 12 2019'
                Display_text['text']= 'May 12 extracted successfully!'
        elif selected_date == 2:
                date = 'May 13 2019'
                Display_text['text']= 'May 13 extracted successfully!'
        elif selected_date == 3:
                date = 'May 14 2019'
                Display_text['text']= 'May 14 extracted successfully!'
        elif selected_date == 4:
                date = 'May 15 2019'
                Display_text['text']= 'May 15 extracted successfully!'
        elif selected_date == 5:
                date = 'May 16 2019'
                Display_text['text']= 'May 16 extracted successfully!'
        elif selected_date == 6:
                date = 'May 17 2019'
                Display_text['text']= 'May 17 extracted successfully!'
        elif selected_date == 7:
                date = 'May 19 2019'
                Display_text['text']= 'May 19 extracted successfully!'
        elif selected_date == 8:
                date = 'Latest News'
                Display_text['text']= 'Latest news extracted successfully!'

        else:
                Display_text['text'] = 'INVALID! SELECT A DATE TO EXTRACT!'
                Display_text['fg']= 'red'
                Display_text['font']= ('strong arial', 8)
        
        #------------------------------ creating and writing in a new HTML File--------------------------#
        #Opening a file for reading
        text_file = open('Internetarchive/' + date + '.html', encoding="utf8")
        text = text_file.read()

        #Using the Regex to extract web information
        image = findall('src=\"(.*.jpg)\"',text)
        article_link = findall('<a class=\"\" href=\"(.*)\">.*<\/a>',text)
        summary = findall('<p class=\"WSJTheme__summary_12br5Svc0SkakLvKF-Jpuj \">(.*)<span class="WSJTheme__stats_2waJk-qlbOxxzBKwfnN8tc "></span><\/p>',text)
        headline = findall('<a class="" href=".*">(.*)<\/a>',text)
        day = findall('<p class="">(.*)<\/p>',text)
        url = 'Link to full story:'

        
        extracted_file = open('WSJ News File.html','w')
        extracted_file.write("""<!DOCTYPE html>

        <html border: 2px solid>

        <head>

        <title> The Wall street Journal Archive </title>

        <!--Masterhead-->
        <h1 align = "center"> WSJ News Archive (world) </h1>
        <p align="center"><img src = https://write2market.com/wp-content/uploads/Wall-Street-Journal-Logo.jpg"></p>
        <p align = "center"><strong> News source: </strong><a href = "https://www.wsj.com/news/world">https://www.wsj.com/news/world  </p></a> """
        '<h4 align = "center"; style="color:red;">'+str(day)+'</h4>'
        """"<p align = "center"> Archivist: Rona Rosal </p>
                

        </head>

        <style>

        body {background-color:beige}
        h1 {width: 80; margin-left:auto ; margin-right: auto; text-align: center}
        h2 {width: 80; margin-left:auto ; margin-right: auto; text-align: center}
        h3 {width: 80; margin-left:auto ; margin-right: auto; text-align: center}
        hr {width: 80; margin-left:auto ; margin-right: auto; text-align: center}
        border {4px:4px:4px:4px; solid}


        </style>

        </head>""")

        #writing thr body of html file
        extracted_file.write(""" <body>""")
        
        
       #extracting information from archive files to html filem (8 days)
        extracted_file.write('<h3>1) "'+str(headline[1])+'</h3>')
        extracted_file.write('<p align = "center""><img src="' +str(image[1])+'">')
        extracted_file.write('<p >'+str(summary[0]+'</p>'))
        extracted_file.write('<p <strong>'+str(url)+'</strong><a href="'+str(article_link[1])+'">'+str(article_link[1])+'</p></a>')

        extracted_file.write('<h3>2) "'+str(headline[2])+'</h3>')
        extracted_file.write('<p align = "center""><img src="' +str(image[2])+'">')
        extracted_file.write('<p >'+str(summary[1]+'</p>'))
        extracted_file.write('<p <strong>'+str(url)+'</strong><a href="'+str(article_link[2])+'">'+str(article_link[2])+'</p></a>')

        extracted_file.write('<h3>3) "'+str(headline[3])+'</h3>')
        extracted_file.write('<p align = "center""><img src="' +str(image[3])+'">')
        extracted_file.write('<p >'+str(summary[2]+'</p>'))
        extracted_file.write('<p <strong>'+str(url)+'</strong><a href="'+str(article_link[3])+'">'+str(article_link[3])+'</p></a>')

        extracted_file.write('<h3>4) "'+str(headline[4])+'</h3>')
        extracted_file.write('<p align = "center""><img src="' +str(image[4])+'">')
        extracted_file.write('<p >'+str(summary[3]+'</p>'))
        extracted_file.write('<p <strong>'+str(url)+'</strong><a href="'+str(article_link[4])+'">'+str(article_link[4])+'</p></a>')


        extracted_file.write('<h3>5) "'+str(headline[5])+'</h3>')
        extracted_file.write('<p align = "center""><img src="' +str(image[5])+'">')
        extracted_file.write('<p >'+str(summary[4]+'</p>'))
        extracted_file.write('<p <strong>'+str(url)+'</strong><a href="'+str(article_link[5])+'">'+str(article_link[5])+'</p></a>')

        extracted_file.write('<h3>6) "'+str(headline[6])+'</h3>')
        extracted_file.write('<p align = "center""><img src="' +str(image[6])+'">')
        extracted_file.write('<p >'+str(summary[5]+'</p>'))
        extracted_file.write('<p <strong>'+str(url)+'</strong><a href="'+str(article_link[6])+'">'+str(article_link[6])+'</p></a>')

        extracted_file.write('<h3>7) "'+str(headline[7])+'</h3>')
        extracted_file.write('<p align = "center""><img src="' +str(image[7])+'">')
        extracted_file.write('<p >'+str(summary[6]+'</p>'))
        extracted_file.write('<p <strong>'+str(url)+'</strong><a href="'+str(article_link[7])+'">'+str(article_link[7])+'</p></a>')

        extracted_file.write('<h3>8) "'+str(headline[8])+'</h3>')
        extracted_file.write('<p align = "center""><img src="' +str(image[8])+'">')
        extracted_file.write('<p >'+str(summary[7]+'</p>'))
        extracted_file.write('<p <strong>'+str(url)+'</strong><a href="'+str(article_link[8])+'">'+str(article_link[8])+'</p></a>')

        extracted_file.write('<h3>9) "'+str(headline[9])+'</h3>')
        extracted_file.write('<p align = "center""><img src="' +str(image[9])+'">')
        extracted_file.write('<p >'+str(summary[8]+'</p>'))
        extracted_file.write('<p <strong>'+str(url)+'</strong><a href="'+str(article_link[9])+'">'+str(article_link[9])+'</p></a>')

        extracted_file.write('<h3>10) "'+str(headline[10])+'</h3>')
        extracted_file.write('<p align = "center""><img src="' +str(image[10])+'">')
        extracted_file.write('<p >'+str(summary[9]+'</p>'))
        extracted_file.write('<p <strong>'+str(url)+'</strong><a href="'+str(article_link[10])+'">'+str(article_link[10])+'</p></a>')


         #close the writing for html file       
        extracted_file.write('''

        
        </body>

        </html>''')


        #Closing the HTML File   
        extracted_file.close()
 
        
def display_html():
        pass
                

### create and the radiobuttons where dates are stored

may_12 = Radiobutton(window, text = 'May 12 2019',variable = select, value = 1, command = display_text,
                           bg = 'Dark Blue', font = ('times bold', 10), fg = 'red')
may_13 = Radiobutton(window, text = 'May 13 2019',variable = select, value = 2, command = display_text,
                           bg = 'dark blue', font = ('times bold', 10), fg = 'red')
may_14 = Radiobutton(window, text = 'May 14 2019',variable = select, value = 3, command = display_text,
                           bg = 'dark blue', font = ('times bold', 10), fg = 'red')
may_15 = Radiobutton(window, text = 'May 15 2019',variable = select, value = 4, command = display_text,
                           bg = 'dark blue', font = ('times bold', 10), fg = 'red')
may_16 = Radiobutton(window, text = 'May 16 2019',variable = select, value = 5, command = display_text,
                           bg = 'dark blue', font = ('times bold', 10), fg = 'red')
may_17 = Radiobutton(window, text = 'May 17 2019',variable = select, value = 6, command = display_text,
                           bg = 'dark blue', font = ('times bold', 10), fg = 'red')
may_18 = Radiobutton(window, text = 'May 19 2019',variable = select, value = 7, command = display_text, 
                           bg = 'dark blue', font = ('times bold', 10), fg = 'red')
latestnews = Radiobutton(window, text='Latest News', bg= 'dark blue', font = ('times bold',10), fg = 'red',
                           variable = select, value = 8,command = display_text)

#Pack radio buttons
may_12.grid(column = 2, row = 2)
may_13.grid(column = 2, row = 3)
may_14.grid(column = 2, row = 4)
may_15.grid(column = 2, row = 5)
may_16.grid(column = 2, row = 6)
may_17.grid(column = 2, row = 7)
may_18.grid(column = 2, row = 8)
latestnews.grid(column = 2, row = 9)


#Add and pack Buttons for Archiving latest news from the web
archive_button= Button (window,text = 'Archive latest news from the web', font = ('Bold Times', 10),
                 activebackground = 'yellow', width = '28', bd = '5', command = download)
archive_button.grid(column = 4,row = 3)

#Add and pack Buttons for extracting archived HTML
extract_button = Button(window, text = 'Extract from archive to HTML news file',font = ('Bold Times', 10),
                  activebackground = 'yellow',width = '28',bd = '5', command = extract_html)
extract_button.grid(column = 4, row = 4)

#Add and pack Buttons for Displaying HTML news file
display_button = Button(window, text = 'Display HTML news file',font = ('Bold Times', 10),
                 activebackground = 'yellow',width = '28',bd = '5', command = display_html)
display_button.grid(column= 4 , row = 5)




