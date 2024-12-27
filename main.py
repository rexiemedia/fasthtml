from fasthtml.common import *
import sqlite3
from templates import *
app, rt = fast_app()

def navigation_bar():
   return Ul(
        Li(P(A("Home", href="#"), A("About US", href="/about"), A("Check", href="/check"))),
        Li("two"),
        Li("three")
    )

# def footer():
#     links = Div(A('Home', hx_get='/about'), A('About Us', hx_get='/'))
#     return links

@rt("/")
def get():

    return Titled(Div(P("Hello Home", navigation_bar())))

@rt("/about")
def get():

    return Titled(Div(P("Hello About"),navigation_bar()))

@app.get("/check")
def check():
    return Title("Count Demo"), Main(
        H1("Count Demo"),
       Div(P("Hello Ceck"),P(A("Home", href="/")),  P(A("About US", href="/#")))
    )

serve()