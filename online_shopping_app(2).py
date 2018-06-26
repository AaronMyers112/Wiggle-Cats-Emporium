
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: *****n10221743*****
#    Student name: *****Aaron Myers*****
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  Online Shopping Application
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application for simulating an online shopping experience.  See
#  the instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.
#

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *


# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed).
from sqlite3 import *

import os

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce
# a meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url,
             target_filename = 'download',
             filename_extension = 'html'):

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



#Creating Functions for the different Windows

#Live/Dynamic Websites
def shop_1():
    download_page = urlopen('http://feeds.feedburner.com/thinkgeek/whatsnew')
    shop1_text = download_page.read().decode('UTF-8')
    shop1_window = Toplevel(shop)
    shop1_window['bg'] = 'black'
    shop1_window.title("Think Geek")
    shop1_items(shop1_window, shop1_text)

def shop_2():
    download_page = urlopen('https://www.amazon.com.au/gp/rss/bestsellers/electronics')
    shop2_text = download_page.read().decode('UTF-8')
    shop2_window = Toplevel(shop)
    shop2_window['bg'] = '#7798EF'
    shop2_window.title("Deal News")
    shop2_items(shop2_window, shop2_text)

#Offline/Static Websites
def shop_3():
    shop3_text = open('Archived Websites\pc case gear.html').read()
    shop3_window = Toplevel(shop)
    shop3_window.title("PC Case Gear")
    shop3_items(shop3_window, shop3_text)

def shop_4():
    shop4_text = open('Archived Websites\MSY.html').read()
    shop4_window = Toplevel(shop)
    shop4_window.title("MSY Computers")
    shop4_items(shop4_window, shop4_text)


#Finding the different parameters for each product
def shop1_items (window, text):
    #name, price, description, and images of the products
    name = findall(' : ([A-Za-a][A-z].[^<]*)', text)
    price = findall('. \$(.[^&]*)', text)
    description = findall('		<description>([A-Za-z][A-z].[^$]*)', text)
    image = ['https://media.giphy.com/media/cPxRDvlSj9QKA/giphy.gif',
             'https://media.giphy.com/media/cPxRDvlSj9QKA/giphy.gif',
             'https://media.giphy.com/media/cPxRDvlSj9QKA/giphy.gif',
             'https://media.giphy.com/media/cPxRDvlSj9QKA/giphy.gif',
             'https://media.giphy.com/media/cPxRDvlSj9QKA/giphy.gif',
             'https://media.giphy.com/media/cPxRDvlSj9QKA/giphy.gif',
             'https://media.giphy.com/media/cPxRDvlSj9QKA/giphy.gif',
             'https://media.giphy.com/media/cPxRDvlSj9QKA/giphy.gif',
             'https://media.giphy.com/media/cPxRDvlSj9QKA/giphy.gif',
             'https://media.giphy.com/media/cPxRDvlSj9QKA/giphy.gif',
             'https://media.giphy.com/media/cPxRDvlSj9QKA/giphy.gif']
    #Creating a nice little title at the top
    title = Label(window, text = 'Think Geek - What\'s New',
                  font = ('Ariel', 18))
    #Running a function to create the different content for each page
    create_content_think_geek(name, price, window, 'white', description, image)
    url = Label(window, text = 'http://feeds.feedburner.com/thinkgeek/whatsnew',
            font = ('Ariel', 7))
    #Specifications for the title
    title['bg'] = 'white'
    title.grid(row = 0)
    url.grid(row = 3)
def shop2_items (window, text):
    #name, price, description, and images of the products
    name = findall("""<item>         <title>#[0-9][0-9]?: (.*?[A-z] .[^$|<]*)""", text)
    price = findall('<b>\$([0-9]*)', text)
    #no description available for products
    description = "              "
    image = findall('><img src="(https?://[0-9]?[-]?[A-z][-]?[A-z].[^"]*)', text)
    #Running a function to create the different content for each page
    create_content(name, price, window, '#89A5F1', description, image)
    #Creating a nice little title at the top
    title = Label(window, text = 'Deal News - What\'s new',
                  font = ('Ariel', 18))
    url = Label(window, text = 'https://www.amazon.com.au/gp/rss/bestsellers/electronics',
            font = ('Ariel', 7))
    #Specifications for the title
    title['bg'] = '#7798EF'
    title.grid(row = 0)
    url.grid(row = 3)

def shop3_items (window, text):
    #name, price, description, and images of the products
    name = findall('jpg" alt="([A-Za-a][A-z].[^"]*)', text)
    price = findall('no-margin">\$(.[^<]*)', text)
    description = findall("""</h5>

          <p>
            ([A-Za-z][A-z].[^<]*)</p>""", text)
    image = findall('<img src="(https://files.pccasegear.com/images/[0-9]+[-]?[A-z][-]?[A-z].[^"]*)', text)
    #Creating a nice little title at the top
    title = Label(window, text = 'PC Case Gear - Graphics Cards',
                  font = ('Ariel', 18))
    create_content(name, price, window, 'white', description, image)
    url = Label(window, text = 'https://www.pccasegear.com/category/193_876/graphics-cards/nvidia-graphics-cards',
            font = ('Ariel', 7))
    title['bg'] = 'white'
    title.grid(row = 0)
    url.grid(row = 3)

def shop4_items (window, text):
    #name, price, description, and images of the products
    name = findall('_blank" title="([A-Za-z][A-z].[^"]*)">[A-Za-z][A-z].[^<]*', text)
    price = findall(' <span class="price" style="display: inline;">\$([0-9].[^<]*)', text)
    #no description available for products
    description = '              '
#    image = findall(' <img src="./Case - QLD Varsitylakes_files/([A-Za-z][-]?[A-z].[^"]*)" alt="[a-zA-Z][(|A-z| |-]*', text)
    image = findall(' <img src="(http://d2n31v7y9dczut.cloudfront.net/qld/varsitylakes/[0-9]+[-]?[a-z]*_default/[A-Za-z][-]?[A-z].[^"]*)" alt="[a-zA-Z][(|A-z| |-]*', text)
    #removing any unwanted images from the list
#    image.remove('case.jpg')
    #Running a function to create the different content for each page
    create_content(name, price, window, '#89A5F1', description, image)
    #Creating a nice little title at the top and displaying ULR at bottom
    title = Label(window, text = 'MSY Computers',
                  font = ('Ariel', 18))
    url = Label(window, text = 'http://www.msy.com.au/16-case',
                font = ('Ariel', 7))
    #Specifications for the title
    title['bg'] = '#7798EF'
    title.grid(row = 0)
    url.grid(row = 3)

def create_content (name, cost, window, color, info, picture):
    #create a little frame for the products to sit in
    label_frame = LabelFrame(window, text = 'Choose a product')
    for item in range(10):
        #remove any html special characters
        name[item] = re.sub("&[^ ;]+;", "\"", name[item])
        #create the label for the product name
        label_info = Label(label_frame, text = name[item])
        #create the add to cart button
        btn = Button(label_frame, text="Add To Cart",
                     command=lambda x = item: cart_btn(name[x], cost[x], info[x], picture[x]))
        #create a label for the price
        label_price = Label(label_frame, text = '$' + cost[item])
        #pack it all into the correct positions
        label_price.grid(column = 0, row = item)
        label_info.grid(column = 1, row = item)
        label_info['bg'] = color
        btn['bg'] = color
        label_price['bg'] = color
        
        btn.grid(column = 2, row = item,
                 padx = 2, pady = 1)
    #choosing colour and position for the frame
    label_frame['bg'] = color
    label_frame.grid(row = 1, padx = 5, pady = 5)

def create_content_think_geek (name, cost, window, color, info, picture):
    #create a little frame for the products to sit in
    label_frame = LabelFrame(window, text = 'Choose a product')
    price_aud = cost
    for item in range(10):
        price_aud = [float(cost[number]) * 1.29 for number in range(10)]
        #remove any html special characters
        name[item] = re.sub("&[^ ;]+;", "\"", name[item])
        #create the label for the product name
        label_info = Label(label_frame, text = name[item])
        #create the add to cart button
        btn = Button(label_frame, text="Add To Cart",
                     command=lambda x = item: cart_btn_think_geek(name[x], cost[x], info[x], picture[x], price_aud[x]))
        #create a label for the price
        label_price = Label(label_frame, text = '$' + cost[item])
        #pack it all into the correct positions
        label_price.grid(column = 0, row = item)
        label_info.grid(column = 1, row = item)
        label_info['bg'] = color
        btn['bg'] = color
        label_price['bg'] = color
        
        btn.grid(column = 2, row = item,
                 padx = 2, pady = 1)
        
    #choosing colour and position for the frame
    label_frame['bg'] = color
    label_frame.grid(row = 1, padx = 5, pady = 5)

#function for the add to cart buttons
def cart_btn (name, price, info, picture):
    global cart
    cart.append(name)
    cost.append(price)
    description.append(info)
    image.append(picture)
    total.append(price)

def cart_btn_think_geek (name, price, info, picture, price_aud):
    global cart
    cart.append(name)
    cost.append(price)
    description.append(info)
    image.append(picture)
    total.append(price_aud)

def close():
    connection = connect('shopping_cart.db')
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM ShoppingCart""")
    cursor.close()
    connection.close()
    exit()

#creating the html invoice
def invoice_btn_function(name, price, info, image):
    #Connecting to databse
    connection = connect('shopping_cart.db')
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM ShoppingCart""")
    total = price
    total = [float(number) for number in total]
    total = sum(total)
    file = open('Test Website\\' + invoice_file, 'w')
    first_section = """
<!doctype html>
<html lang = "en">
<link rel = "stylesheet" type = "text/css" href = "Style\StyleSheet.css">

<head>
<title>
Test Website
</title>
</head>
<body>
<div class="wrapper" align="center">
<div  class="header">
<h1 >
Thank for shopping at Wiggle Cats Nerd and Geek Emporium
</h1>
<img src="https://media.giphy.com/media/cPxRDvlSj9QKA/giphy.gif" class="image">
</div>
<div class="text">
<br>
<p>
Your digital invoice has been created, please view it below
</p>
</div>
<div class="main_body">
<ul class="o-lyt  o-lyt--flush  product-list">
<li class="o-lyt__item  o-lyt__total product-list__item">
<div class="o-lyt__item">
<h2>
You're Total is:
</h2>
</div>
<div class="o-lyt__item">
<h2>
${:0.2f}
</h2>
</div>
</li>
""".format(total)
    second_section = """
<li class="o-lyt__item  product-list__item">
<div class="product">
<figure class="o-lyt">
<div class="o-lyt__item  product__image">
<img src="{}" />
</div><!--
--><figcaption class="o-lyt__item  product__content">
<div class="o-lyt">
<div class="o-lyt__item  product__info">
<h3>
{}
</h3>
<p>
{}
</p>
</div><!--
--><div class="product__price  o-lyt__item">
<h3>
${}
</h3>
</div>
</div>
</figcaption>
</figure>
</div>
</li>
"""
    last_section = """
</ul>
<div class="o-lyt" align=center>
<div class="o-lyt__item">
<h2>
The websites that have been used
</h2>
</div>
<nav>
<div class="o-lyt__item  nav">
<a href='http://feeds.feedburner.com/thinkgeek/whatsnew' target="_blank">
<button href='http://feeds.feedburner.com/thinkgeek/whatsnew' target="_blank" class="button  o-lyt__item  nav__item">Think Geek</button></a>
<a href='https://www.amazon.com.au/gp/rss/bestsellers/electronics' target="_blank">
<button href='http://feeds.feedburner.com/thinkgeek/whatsnew' target="_blank" class="button  o-lyt__item  nav__item">Amazon</button></a>
<a href='https://www.pccasegear.com/category/193_876/graphics-cards/nvidia-graphics-cards' target="_blank">
<button href='http://feeds.feedburner.com/thinkgeek/whatsnew' target="_blank" class="button  o-lyt__item  nav__item">PC Case Gear</button></a>
<a href='http://www.msy.com.au/16-case' target="_blank">
<button href='http://feeds.feedburner.com/thinkgeek/whatsnew' target="_blank" class="button  o-lyt__item  nav__item">MSY Computers</button></a>
</div>
</nav>
</div>
</div>
</div>
</body>

</html>
"""
    file.write(first_section)
    for item in range(len(cart)):
        file.write(second_section.format(image[item], name[item],
                                         info[item], price[item]))
        cursor.execute("""
INSERT into ShoppingCart(item, price) VALUES (?, ?);""", (name[item], price[item]))
        connection.commit()
    cursor.close()
    connection.close()
    file.write(last_section)
    file.close()
    
    os.startfile('Test Website\\' + invoice_file)

#global variable - lists for the different variables

def main_window(background_colour):
    #Defining main window details
    shop['bg'] = background_colour
    shop.title('Wiggle Cat\'s Emporium')

    #Main logo

    image_frame = Label(shop, image = picture)
    image_frame['bg'] = background_colour

    #Main body a.k.a. the actual shop
    live_shop_btn_frame = LabelFrame(shop, relief = 'groove',
                                borderwidth = 2, text = 'Browse a Live Shop',
                                bg = background_colour)
    archived_shop_btn_frame = LabelFrame(shop, relief = 'groove',
                                borderwidth = 2, text = 'Browse a Saved Shop',
                                bg = background_colour)
    shop_slogan = Label(shop, text = 'Welcome to Wiggle Cats Nerd and Geek Emporium',
                        font = ("Arial", 24),
                        bg = background_colour)
    #The different Buttons
    shop1_btn = Button(live_shop_btn_frame, text = 'Think Geek',
                       width = 16, command = shop_1,
                       bg = background_colour)
    shop2_btn = Button(live_shop_btn_frame, text = 'Amazon',
                       width = 16, command = shop_2,
                       bg = background_colour)
    shop3_btn = Button(archived_shop_btn_frame, text = 'PC Case Gear',
                       width = 16, command = shop_3,
                       bg = background_colour)
    shop4_btn = Button(archived_shop_btn_frame, text = 'MSY Computers',
                       width = 16, command = shop_4,
                       bg = background_colour)
    invoice_btn = Button(shop, text = 'Print Invoice',
                        width = 16, command = lambda: invoice_btn_function(cart, cost,
                                                                          description, image),
                         bg = background_colour)
    close_btn = Button(shop, text = 'Close',
                       width = 16, command = close,
                       bg = background_colour)



    #Packing all of the different aspects into their respective places
    shop_slogan.grid(column = 0, row = 0,
                     columnspan = 5, padx = 5)
    image_frame.grid(column = 0, row = 1,
                     columnspan = 3, rowspan = 3)
    live_shop_btn_frame.grid(column = 3, row = 1,
                        columnspan = 1, rowspan = 5)
    archived_shop_btn_frame.grid(column = 4, row = 1,
                                 columnspan = 3, rowspan = 5)
    shop1_btn.grid(column = 1, row = 1,
                   padx = 2, pady = 2)
    shop2_btn.grid(column = 1, row = 2,
                   padx = 2, pady = 2)
    shop3_btn.grid(column = 1, row = 1,
                   padx = 2, pady = 2)
    shop4_btn.grid(column = 1, row = 2,
                   padx = 2, pady = 2)
    invoice_btn.grid(column = 3, row = 3)
    close_btn.grid(column = 4, row = 3,
                   padx = 2, pady = 2)

    # Name of the invoice file. To simplify marking, your program should
    # generate its invoice using this file name.
invoice_file = 'invoice.html'

cart = []
cost = []
description = []
image = []
total = []

shop = Tk()

picture = PhotoImage(file = 'giphy.gif')

main_window('#85929E')

shop.mainloop()


