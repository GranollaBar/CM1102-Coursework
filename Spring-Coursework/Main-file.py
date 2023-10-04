from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import timedelta
import re

app = Flask(__name__)
app.secret_key = "itsasecret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AllDetailsDatabase.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

app.app_context().push()

class AllDetailsDatabase(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    title = db.Column(db.String)
    image = db.Column(db.String)
    description = db.Column(db.String)
    environment = db.Column(db.String)
    price = db.Column(db.String)
    fullprice = db.Column(db.String)
    shoppingcart = db.Column(db.String)

    def __init__(self, firstname, surname, email, password, title, image, description, environment, price, fullprice, shoppingcart):
        self.firstname = firstname
        self.surname = surname
        self.email = email
        self.password = password
        self.title = title
        self.image = image
        self.description = description
        self.environment = environment
        self.price = price
        self.fullprice = fullprice
        self.shoppingcart = shoppingcart

allproducts = [["Hawksmoor 1200W 32cm Electric Lawnmower 230V", "images/product-images/real_product1.png", "Take the hassle out of cutting your grass with this Hawksmoor electric lawnmower. With a 32cm cutting width and a generous 10m of cable, its perfect for mowing smaller gardens; you can even choose from three cutting heights for a variety of finishes. | Designed with a robust but lightweight polypropylene deck, the 1200W lawnmower weighs just 8.2kg so pushing and manoeuvring it around your garden requires little effort. The 30L grass collection box keeps your lawn tidy while letting you mow for longer, and the large wheels are specially designed to protect your grass. | • Three cutting heights from 25-65mm for a choice of finishes | • 32cm cutting width is perfect for mowing small lawns | • 30L grass collection box; more mowing, less emptying | • 10m cable gives you plenty of reach to move freely around lawn | • Polypropylene deck is lightweight but robust | • Large wheels are specially designed to protect your lawn | • Weighs just 8.2kg; easy to push and manoeuvre", "3.82KG CO2 per year or 8.4IB CO2 per year", "--- Item-Price: £98.96 ---"],
            ["Mountfield HP164 39CM 123CC Hand-Propelled Rotary Petrol Lawn Mower", "images/product-images/real_product2.png", "Powered by a Mountfield ST120 OHV 123cc engine and features a tough, corrosion-free polypropylene cutter deck. Lightweight, easy to use and economical to run. Includes 4 height adjusters with 5 pre-set cutting positions ranging from 25-70mm. Can also be used without the collector to leave the cuttings. Suitable for lawns up to 400m². | • 123cc 4-Stroke Mountfield Engine | • 5 Cutting Heights (25-70mm) | • 40Ltr Grass Collector | • Polypropylene Deck | • Hardened Steel Blade | • 2 Year Manufacturer's Guarantee (T&Cs Apply) | • Without Mulching Facility | • Hand-Propelled | • Folding Handles", "45.5KG CO2 per year or 100IB CO2 per year", "--- Item-Price: £169.99 ---"],
            ["Flymo Easiglide 330 1700W 33CM Hover Mower 230V", "images/product-images/real_product3.png", "Designed for small to medium gardens, the Flymo EasiGlide 330 is a 33cm electric hover collect mower with a powerful 1700W motor. Highly manoeuvrable: floats on a cushion of air whilst cutting. Equipped with dual lever handles, an easy to empty 20Ltr grassbox and convenient cable storage. Folds down for storage and can be wall-mounted. | • 1700W | • 3 Cutting Heights (10-30mm) | • 20Ltr Grass Box | • 1 Year Guarantee | • Metal Blade | • Plastic Deck | • Without Mulching Facility | • Hover Technology | •Vacuum Collection | • On-Top Grass Box","5.41KG CO2 per year or 11.9IB CO2 per year", "--- Item-Price: £119.99 ---"],
            ["Titan TTLMP300SP40 41CM 125CC Self-Propelled Rotary Petrol Lawn Mower", "images/product-images/real_product4.png", "Features advanced cutting blades for reliable performance. Includes 41cm cutting deck and universal blade with mulching, catching and overload protection. No cords, therefore ideal for keeping lawns tidy even when there is no power source in reach. | • 125cc 4-Stroke Briggs & Stratton OHV Engine | • 7 Cutting Heights (25-75mm) | • 50Ltr Grass Collector | • Steel Deck | • Hardened Steel Blade | • 2 Year Manufacturer's Guarantee (T&Cs Apply) | • With Mulching Facility", "45.5KG CO2 per year or 100IB CO2 per year", "--- Item-Price: £219.99 ---"],
            ["Mountfield MTF 108H SD 108CM 432CC Ride On Mower", "images/product-images/real_product5.png", "Dedicated side-discharge garden tractor powered by Stiga ST450 432cc single cylinder engine. Ideal for lawns, orchards and paddocks up to 3 acres. Twin-bladed deck with 108cm cutting blade and 7 cutting heights, between 25-80mm. Seat features safety engine cut-out switch if driver dismounts whilst blades are turning. | Pedal-operated hydrostatic transmission provides variable ground speed control. Easy to clean, attach a hose to deck nozzle and engage the blades. Can be used with optional extras including battery charger, mulching plug and tow hitch (sold separately). | • 4-Stroke Stiga Engine | • Hydrostatic Forward & Reverse Drive | • 7 Cutting Heights (25-80mm) | • Mulching Adaptor Available (Not Included) | • Steel Deck & Steel Blades | • Turning Radius 65cm | • Suitable for Lawns up to 3 Acres | • 1 Year Guarantee", "73.5KG CO2 per year or 161.7IB CO2 per year", "--- Item-Price: £2599.00 ---"],
            ["Bosch Advanced Rotak 36-750 36V 1 X 4.0AH LI-ION Cordless 44CM Lawn Mower", "images/product-images/real_product6.png", "Quiet, cordless lawn mower with ProSilence technology. Choose from 7 cutting heights using the AdvancedRotak height adjustment. Features 50Ltr grass box and a LeafCollect blade. Supplied with a 4Ah battery and charger. | • 1 x 4.0Ah Li-Ion Battery | • 7 Cutting Heights (25-80mm) | • 50Ltr Grass Box | • 125min Charge Time | • 3 Year Manufacturer's Guarantee (T&Cs Apply) | • Cutting Blades | • Metal & Plastic Deck | • Without Mulching Facility", "None (however, CO2 emissions of manufacturing per battery is 25.2KG CO2 or 55.4IB CO2 per year)", "--- Item-Price: £464.99 ---"],
            ["Webb 30CM Hand-Push Roller Lawn Mower", "images/product-images/real_product7.png", "Lightweight, hand-push mower with a 12 inch hardened steel cutting cylinder and 5 blades. With large rear roller for classic stripes, simple tool-free cutting height settings and 18ltr grass collector. | Eco-friendly with no fuel or electricity costs. With a classic British Racing Green livery. Suitable for lawns up to 83m². | • Variable Cutting Heights (13-23.5mm) | • 18Ltr Grass Collector | • 2 Year Manufacturer's Guarantee (T&Cs Apply) | • Roller Blade | • Chain Drive from Roller to Cylinder", "No CO2 emissions", "--- Item-Price: £119.99 ---"],
            ["Einhell GC-HM 300 30CM Hand Lawn Mower", "images/product-images/real_product8.png", "Robust, functional cylinder lawn mower, ideal for clean, quiet mowing of lawns of up to 150m² in size. Ball-bearing mounted mower spindle with 5 high-grade steel blades is designed for a cutting width of 30cm, with a 45cm diameter plastic roller. | Features 4-level cutting height adjustment facility between 13mm-37mm, large, lawn-friendly wheels and an ergonomic curved long handle. Park position allows easy and secure storage of mower. 16Ltr removable grass catch bag is easy to empty. | • 4 Cutting Heights (13-37mm) | • 16Ltr Grass Bag | • 2 Year Guarantee | • 5-Blade Hardened Steel Cutting Cylinder", "No CO2 emissions", "--- Item-Price: £54.95 ---"],
            ["Bosch 18V 2.5AH LI-ION Power For All Cordless 19CM Indego XS 300 Robotic Lawn Mower", "images/product-images/real_product9.png", "Intelligent and efficient mowing in neat, parallel lines. Keeps lawns looking good and saves energy and battery power. LogiCut defines different mowing directions for each session to avoid leaving permanent tracks. | Features automatic calculation of a tailored mowing schedule. Suitable for lawns up to 300m². Part of the Bosch Green Power for All alliance system, where the 18V battery can operate a large variety of tools from different brands. | • 2.5Ah Li-Ion Battery | • 3 Cutting Heights (30-50mm) | • 45min Charge Time | • Steel Blade | • Max. Incline: 27% | • Safety Switch | • 2 Year Manufacturer's Guarantee (T&Cs Apply) | • With Mulching Facility", "None (however, CO2 emissions of manufacturing per battery is 7.88KG CO2 or 17.3IB CO2 per year)", "--- Item-Price: £651.95 ---"]]


@app.route("/", methods=["POST","GET"])
def login():
    if request.method == "POST":
        loginEmail = request.form['loginEmail']
        loginPassword = request.form['loginPassword']
        try:
            logincheckbox = request.form['loginCheckBox']
            if logincheckbox:
                session.permanent = True
        except:
            pass
        if loginEmail == "" or loginEmail is None or loginPassword == "" or loginPassword is None:
            pass
        else:
            existantEmail = AllDetailsDatabase.query.filter_by(email=loginEmail).first()
            if existantEmail is None or existantEmail == "":
                flash(f"{loginEmail} and/or {loginPassword} were not found in the database","info")
                return redirect(url_for("login")) 
            session["email"] = existantEmail.email
            finalEmail = session["email"]
            root = AllDetailsDatabase.query.filter_by(email=finalEmail).first()               
            if loginEmail == root.email and loginPassword == root.password:
                session["firstname"] = existantEmail.firstname
                session["surname"] = existantEmail.surname
                return redirect(url_for("main"))
            flash(f"{loginEmail} and/or {loginPassword} were not found in the database","info")
            return redirect(url_for("login"))
    else:
        rows = AllDetailsDatabase.query.count()
        if rows == 0:
            for elements in allproducts:
                firstname = None
                surname = None
                email = None
                password = None
                title = elements[0]
                image = elements[1]
                description = elements[2]
                environment = elements[3]
                price = elements[4]
                fullprice = None
                shoppingcart = None

                productSQLData = AllDetailsDatabase(firstname, surname, email, password, title, image, description, environment, price, fullprice, shoppingcart)
                db.session.add(productSQLData)
                db.session.commit()

        if "email" in session:
            return redirect(url_for("main"))

        return render_template("Login_Page.html")


@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "POST":
        rFirstname = request.form['registerFirstname']
        rSurname = request.form['registerSurname']
        rEmail = request.form['registerEmail']
        rPassword = request.form['registerPassword']
        if rFirstname == "" or rFirstname is None or rSurname == "" or rSurname is None or rEmail == "" or rEmail is None or rPassword == "" or rPassword is None:
            pass
        else:
            existantUser = AllDetailsDatabase.query.filter_by(email=rEmail).first()
            if existantUser:
                flash(f"user {rEmail} already exists, choose a different email","info")
                return redirect(url_for("register"))
            else:
                rtitle = None
                rimage = None
                rdescription = None
                renvironment = None
                rprice = None
                rfullprice = ""
                rshoppingcart = ""
                SQLData = AllDetailsDatabase(rFirstname, rSurname, rEmail, rPassword, rtitle, rimage, rdescription, renvironment, rprice, rfullprice, rshoppingcart)
                db.session.add(SQLData)
                db.session.commit()
                flash("Registered Successfully","info")
                return redirect(url_for("login"))
    else:
        return render_template("Registration_Page.html")


@app.route("/main", methods=["POST","GET"])
def main():
    try:
        session.pop("productID",None)
    except:
        pass
    product1 = AllDetailsDatabase.query.filter_by(_id=1).first()
    product2 = AllDetailsDatabase.query.filter_by(_id=2).first()
    product3 = AllDetailsDatabase.query.filter_by(_id=3).first() 
    product4 = AllDetailsDatabase.query.filter_by(_id=4).first() 
    product5 = AllDetailsDatabase.query.filter_by(_id=5).first() 
    product6 = AllDetailsDatabase.query.filter_by(_id=6).first() 
    product7 = AllDetailsDatabase.query.filter_by(_id=7).first() 
    product8 = AllDetailsDatabase.query.filter_by(_id=8).first() 
    product9 = AllDetailsDatabase.query.filter_by(_id=9).first() 
    userFirstname = session["firstname"]
    userSurname = session["surname"]
    userEmail = session["email"]
    user = AllDetailsDatabase.query.filter_by(email=userEmail).first()
    if user.shoppingcart:
        shoppingCartImage = "images/other-images/final_shopping_cart_items.png"
    else:
        shoppingCartImage = "images/other-images/final_shopping_cart.png"
    return render_template("Main_Page.html", finalFirstname=userFirstname, finalSurname=userSurname, finalCartImage=shoppingCartImage, finalproduct1=product1, finalproduct2=product2, finalproduct3=product3, finalproduct4=product4, finalproduct5=product5, finalproduct6=product6, finalproduct7=product7, finalproduct8=product8, finalproduct9=product9)


@app.route("/productSelected", methods=["POST","GET"])
def productSelected():
    allproductnumbers = ["1","2","3","4","5","6","7","8","9"]
    productselected = request.form['products']
    if int(productselected) <= 9:
        for number in allproductnumbers:
            if productselected == number:
                session["productID"] = int(productselected)
                return redirect(url_for("product"))
            else:
                pass
    else:
        finalString = str(productselected)[1]
        finalInt = int(finalString) + 1
        finalemail = session["email"]
        finaluser = AllDetailsDatabase.query.filter_by(email=finalemail).first()
        if finaluser.shoppingcart == "":
            finaluser.shoppingcart = str(finalInt)
            db.session.commit()
        else:
            finaluser.shoppingcart += (", " + str(finalInt)) 
            db.session.commit()
            shoppingcartstring = re.findall(r'\d+', finaluser.shoppingcart)
            shoppingcartlist = list(map(int, shoppingcartstring))
            shoppingcartlistsorted = sorted(shoppingcartlist)
            finalcartstring = ""
            found = True
            for numbs in shoppingcartlistsorted:
                if shoppingcartlistsorted.index(numbs) == 0 and found == True:
                    finalcartstring += str(numbs)
                    found = False
                else:
                    finalcartstring += (", " + str(numbs))
            finaluser.shoppingcart = finalcartstring
            db.session.commit()
        return redirect(url_for("main"))


@app.route("/product", methods=["POST","GET"])
def product():
    userEmail = session["email"]
    theuser = AllDetailsDatabase.query.filter_by(email=userEmail).first()
    if request.method == "POST":
        choiceselected = request.form['productChoice']
        if choiceselected == "add":
            productselectetion = session["productID"]
            if theuser.shoppingcart == "":
                theuser.shoppingcart = str(productselectetion)
                db.session.commit()
            else:
                theuser.shoppingcart += (", " + str(productselectetion))
                db.session.commit()
                shoppingcartstring = re.findall(r'\d+', theuser.shoppingcart)
                shoppingcartlist = list(map(int, shoppingcartstring))
                shoppingcartlistsorted = sorted(shoppingcartlist)
                finalcartstring = ""
                found = True
                for numbs in shoppingcartlistsorted:
                    if shoppingcartlistsorted.index(numbs) == 0 and found == True:
                        finalcartstring += str(numbs)
                        found = False
                    else:
                        finalcartstring += (", " + str(numbs))
                theuser.shoppingcart = finalcartstring
                db.session.commit()
        else:
            return redirect(url_for("payment"))

    item = session["productID"]
    if item == 1 or item == 3 or item == 7 or item == 8:
        pricecolour = "lightgreen"
    elif item == 4 or item == 6:
        pricecolour = "orange"
    elif item == 2:
        pricecolour = "lightseagreen"
    else:
        pricecolour = "red"
    finalproduct = AllDetailsDatabase.query.filter_by(_id=item).first()
    if theuser.shoppingcart != "":
        shoppingCartImage = "images/other-images/final_shopping_cart_items.png"
    else:
        shoppingCartImage = "images/other-images/final_shopping_cart.png"
    return render_template("Product_Page.html", fullproduct=finalproduct, finalcolour=pricecolour, finalCartImage=shoppingCartImage)


@app.route("/shoppingCart", methods=["POST","GET"])
def shoppingCart():
    try:
        session.pop("productID",None)
    except:
        pass
    userEmail = session["email"]
    userQuery = AllDetailsDatabase.query.filter_by(email=userEmail).first()
    if userQuery.shoppingcart == "":
        flash("Cannot access the shopping cart as no items have been placed there yet","info")
        return redirect(url_for("main"))
    else:
        fulllist = re.findall(r'\d+', userQuery.shoppingcart)
        numbersList = list(map(int, fulllist))
        allnumberslist = sorted(numbersList)
        allDetailsList = []
        quantityList = []
        newNumberList = []
        for i in range(1,10):
            value = allnumberslist.count(i)
            if value > 0:
                quantityList.append(value)
        finaltotalprice = 0
        [newNumberList.append(x) for x in numbersList if x not in newNumberList]
        for j, values in enumerate(newNumberList):
            dataQuery = AllDetailsDatabase.query.filter_by(_id=values).first()
            allDetailsList.append(values)
            allDetailsList.append(dataQuery.title)
            imageString = "images/product-images/real_product_smaller_"
            imageString += str(values)
            imageString += ".png"
            allDetailsList.append(imageString)
            stringPrice = re.findall("\d+\.\d+", dataQuery.price)
            finalprice = float(stringPrice[0]) * quantityList[j]
            allDetailsList.append(stringPrice[0])
            allDetailsList.append(quantityList[j])
            finalfinalprice = "{:.2f}".format(finalprice)
            allDetailsList.append(finalfinalprice)
            finaltotalprice += finalprice
            allDetailsList.append(str(values))
        finalDetails = [allDetailsList[i:i + 7] for i in range(0, len(allDetailsList), 7)]
        numberIndex = len(finalDetails) -1
        finalfinaltotalprice = "{:.2f}".format(finaltotalprice)
        userQuery.fullprice = finalfinaltotalprice
        db.session.commit()
        return render_template("Cart_Page.html", finalAllDetails=finalDetails, finalallprice=finalfinaltotalprice, finalnumberIndex=numberIndex)


@app.route("/allProductsQuery", methods=["POST","GET"])
def allProductsQuery():
    everyproductnumber = ["1","2","3","4","5","6","7","8","9"]
    buttonRequest = request.form['ProductQuery']
    if int(buttonRequest) < 10:
        for number in everyproductnumber:
            if str(buttonRequest) == number:
                usersEmail = session["email"]
                finaluser = AllDetailsDatabase.query.filter_by(email=usersEmail).first()
                usershoppingcartstring = re.findall(r'\d+', finaluser.shoppingcart)
                usershoppingcartlist = list(map(int, usershoppingcartstring))
                removedDeletedItemList = [i for i in usershoppingcartlist if i != int(buttonRequest)]
                usershoppingcartlistsorted = sorted(removedDeletedItemList)
                userfinalcartstring = ""
                found = True
                for numbs in usershoppingcartlistsorted:
                    if usershoppingcartlistsorted.index(numbs) == 0 and found == True:
                        userfinalcartstring += str(numbs)
                        found = False
                    else:
                        userfinalcartstring += (", " + str(numbs))
                finaluser.shoppingcart = userfinalcartstring
                db.session.commit()
                return redirect(url_for("shoppingCart"))
            else:
                pass

    elif int(buttonRequest) == 10:
        newShoppingCartString = ""
        usersEmail = session["email"]
        requestuser = AllDetailsDatabase.query.filter_by(email=usersEmail).first()
        requestuser.shoppingcart = newShoppingCartString
        db.session.commit()
        return redirect(url_for("shoppingCart"))

    else:
        return redirect(url_for("payment"))


@app.route("/payment", methods=["POST","GET"])
def payment():
    if request.method == "POST":
        paymentname = request.form['nameField']
        paymentcvv = request.form['cvvField']
        paymentcard = request.form['cardField']
        typeRequest = request.form['confirmfinalpayment']
        for char in paymentname:
            if char.isalpha() or char == " " or char == ".":
                pass
            else:
                flash(f"name on card conatained an invalid character - {char}","info")
                return redirect(url_for("payment"))
        if paymentcvv.isdigit():
            pass
        else:
            flash(f"CVV conatained a non-digit character","info")
            return redirect(url_for("payment"))
        for digit in paymentcard:
            if digit.isdigit() or digit == " " or digit == "-":
                pass
            else:
                flash(f"card number conatained an invalid character - {digit}","info")
                return redirect(url_for("payment"))
        if "-" not in paymentcard and " " not in paymentcard and len(paymentcard) > 16:
            flash(f"Card number is too long, and thus, does not exist","info")
            return redirect(url_for("payment"))            

        session['value'] = typeRequest
        return redirect(url_for("paymentconfirmed"))              

    try:
        userconnectID = session["productID"]
        userconnectIDQuery = AllDetailsDatabase.query.filter_by(_id=userconnectID).first()
        totalstringPrice = re.findall("\d+\.\d+", userconnectIDQuery.price)
        valueID = "1"
        return render_template("Payment_Page.html", finalprice=totalstringPrice[0], finalvalue=valueID)        
    except:
        userconnectemail = session["email"]
        userconnectEmailQuery = AllDetailsDatabase.query.filter_by(email=userconnectemail).first()
        totalprice = userconnectEmailQuery.fullprice
        value = "2"
        return render_template("Payment_Page.html", finalprice=totalprice, finalvalue=value)


@app.route("/paymentconfirmed", methods=["POST","GET"])
def paymentconfirmed():
    finalvalue = session["value"]
    finaluser = session["email"]
    finalEmailQuery = AllDetailsDatabase.query.filter_by(email=finaluser).first()
    finalcart = finalEmailQuery.shoppingcart
    if request.method == "POST":
        if str(finalvalue) == "1":
            session.pop("value",None)
            return redirect(url_for("main"))
        else:
            finalEmailQuery.shoppingcart = ""
            db.session.commit()
            session.pop("value",None)
            return redirect(url_for("main"))            
    else:
        if str(finalvalue) == "1":
            finalID = session["productID"]
            return render_template("Payment_Successful_Page.html", finalvalue=finalID)
        else:

            return render_template("Payment_Successful_Page.html", finalvalue=finalcart)


@app.route("/logout")
def logout():
    messagefullname = session["firstname"] + " " + session["surname"]
    flash(f"{messagefullname} Logged out Successfully","info")
    session.pop("email",None)
    session.pop("firstname",None)
    session.pop("surname",None)
    session.permanent = False
    return redirect(url_for("login"))



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)