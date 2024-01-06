import os

from flask import Flask, render_template, request, flash, redirect, session, g, jsonify
from sqlalchemy.exc import IntegrityError
from datetime import date
from forms import UserAddForm, LoginForm, RatingForm
import requests
import json

# from forms import UserAddForm, LoginForm, MessageForm, ProfileEditForm
from models import db, connect_db, User, Ingredients, Ingredients_On_Hand, User_Rating

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.static_folder = "static"

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "postgresql:///bartender"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "mix it up")

with app.app_context():
    connect_db(app)

    db.create_all()


@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.userID


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route("/login", methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm(request.form)
    if request.method == "POST":
        if form.validate():
            user = User.authenticate(form.username.data, form.password.data)

            if user:
                do_login(user)
                flash(f"Hello, {user.username}!", "success")
                return redirect("/")

            flash("Invalid credentials.", "danger")

    return render_template("login.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
            )
            db.session.commit()

        except IntegrityError:
            flash("Username already taken", "danger")
            return render_template("signup.html", form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template("signup.html", form=form)


@app.route("/logout")
def logout():
    """Handle logout of user."""
    do_logout()

    flash("You are now logged out. Goodbye!")

    return redirect("/")


@app.route("/")
def homepage():
    """Display homepage"""

    return render_template("home.html")


@app.route("/start")
def start():
    """Sends user to bar or login"""

    if not g.user:
        return redirect("/login")

    return redirect("/bar")


@app.route("/bar")
def bar():
    """Display user's current on hand ingredients"""
    if g.user:
        user_id = g.user.userID
        ingredients = Ingredients_On_Hand.query.filter_by(userID=user_id).all()

        return render_template("bar.html", ingredients=ingredients)
    else:
        return render_template("home.html")


@app.route("/submit-ingredient", methods=["POST"])
def submit_ingredient():
    user_id = g.user.userID
    try:
        data = request.get_json()
        submitted_ingredient = data.get("ingredient")
        print(submitted_ingredient)
        if not submitted_ingredient:
            return jsonify(
                {"success": False, "message": "Please provide an ingredient"}
            )

        ingredients = [
            ingredient.name.lower() for ingredient in Ingredients.query.all()
        ]

        if submitted_ingredient.lower() not in ingredients:
            return jsonify({"success": False, "message": "Ingredient not in the list"})

        curr_on_hand = [
            ingredient.ingredient.lower()
            for ingredient in Ingredients_On_Hand.query.all()
        ]

        if submitted_ingredient.lower() in curr_on_hand:
            return jsonify({"success": False, "message": "Ingredient already added"})

        new_ingredient = Ingredients_On_Hand(
            userID=user_id, ingredient=submitted_ingredient
        )
        print(new_ingredient)
        db.session.add(new_ingredient)
        db.session.commit()

        flash(f'Ingredient "{submitted_ingredient}" submitted successfully!', "success")

        return jsonify(
            {"success": True, "message": "Ingredient submitted successfully"}
        )

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/delete-ingredient", methods=["DELETE"])
def delete_ingredient():
    try:
        data = request.get_json()
        ingredient_id = data.get("ingredientId")

        # Fetch the ingredient from the database
        ingredient_on_hand = Ingredients_On_Hand.query.get(ingredient_id)
        print(ingredient_on_hand)
        if ingredient_on_hand:
            # Delete the ingredient
            db.session.delete(ingredient_on_hand)
            db.session.commit()

            return jsonify(
                {"success": True, "message": "Ingredient deleted successfully"}
            )
        else:
            return jsonify({"success": False, "message": "Ingredient not found"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


@app.route("/drink-search")
def drink_search():
    selected_ingredients = request.args.get("ingredients")
    formatted_ingredients = selected_ingredients.replace(" ", "_")
    print(selected_ingredients)
    api_url = f"https://www.thecocktaildb.com/api/json/v2/9973533/filter.php?i={formatted_ingredients}"
    try:
        response = requests.get(api_url)
        data = response.json()
        data_dict = json.loads(json.dumps(data))
    except Exception as e:
        return jsonify({"error": str(e)})

    return render_template("test.html", data=data_dict["drinks"])


@app.route("/cocktails/<int:drink_id>")
def drink_page(drink_id):
    """Display page with drink details"""
    api_url = (
        f"https://www.thecocktaildb.com/api/json/v2/9973533/lookup.php?i={drink_id}"
    )
    try:
        response = requests.get(api_url)
        data = response.json()
        drink = data["drinks"][0]
        return render_template("cocktail.html", drink=drink)
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/rating/<int:drink_id>", methods=["GET", "POST"])
def display_rating(drink_id):
    form = RatingForm()
    user_id = g.user.userID
    api_url = (
        f"https://www.thecocktaildb.com/api/json/v2/9973533/lookup.php?i={drink_id}"
    )
    response = requests.get(api_url)
    data = response.json()
    drink = data["drinks"][0]
    if form.validate_on_submit():
        rating = User_Rating(
            userID=user_id,
            drinkID=drink_id,
            name=drink["strDrink"],
            user_rating=form.rating.data,
            user_comments=form.comments.data,
            first_made=date.today(),
        )
        db.session.add(rating)
        db.session.commit()
        return redirect("/history")
    try:
        response = requests.get(api_url)
        data = response.json()
        drink = data["drinks"][0]
        return render_template("rating.html", drink=drink, form=form)
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/history")
def show_history():
    """Display page with list of user's past drinks"""
    rated_drinks = User_Rating.query.filter_by(userID=g.user.userID).all()

    return render_template("history.html", rated_drinks=rated_drinks)


@app.route("/history/<int:user_drink_id>")
def show_user_drink(user_drink_id):
    """Display page for specific drink from user's history"""
    rated_drink = User_Rating.query.filter_by(user_drink_ID=user_drink_id).first()

    return render_template("user_drink.html", rated_drink=rated_drink)


@app.route("/random")
def show_random_drink():
    """Display page for a random cocktail"""
    api_url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"

    try:
        response = requests.get(api_url)
        data = response.json()

        # Convert JSON string to a Python dictionary
        data_dict = json.loads(json.dumps(data))

        # Extract 'strInstructions' from each item in 'drinks'
        words_to_check = ["oz, shot, shots, part, parts, dashes, dash"]
        id = [item["idDrink"] for item in data_dict["drinks"]]
        name = [item["strDrink"] for item in data_dict["drinks"]]
        ing1 = [item["strIngredient1"] for item in data_dict["drinks"]]
        ing2 = [item["strIngredient2"] for item in data_dict["drinks"]]
        ing3 = [item["strIngredient3"] for item in data_dict["drinks"]]
        ing4 = [item["strIngredient4"] for item in data_dict["drinks"]]
        ing5 = [item["strIngredient5"] for item in data_dict["drinks"]]
        ing6 = [item["strIngredient6"] for item in data_dict["drinks"]]
        ing7 = [item["strIngredient7"] for item in data_dict["drinks"]]
        ing8 = [item["strIngredient8"] for item in data_dict["drinks"]]
        ing9 = [item["strIngredient9"] for item in data_dict["drinks"]]
        ing10 = [item["strIngredient10"] for item in data_dict["drinks"]]
        mes1 = [item["strMeasure1"] for item in data_dict["drinks"]]
        mes2 = [item["strMeasure2"] for item in data_dict["drinks"]]
        mes3 = [item["strMeasure3"] for item in data_dict["drinks"]]
        mes4 = [item["strMeasure4"] for item in data_dict["drinks"]]
        mes5 = [item["strMeasure5"] for item in data_dict["drinks"]]
        mes6 = [item["strMeasure6"] for item in data_dict["drinks"]]
        mes7 = [item["strMeasure7"] for item in data_dict["drinks"]]
        mes8 = [item["strMeasure8"] for item in data_dict["drinks"]]
        mes9 = [item["strMeasure9"] for item in data_dict["drinks"]]
        mes10 = [item["strMeasure10"] for item in data_dict["drinks"]]
        # ing11 = [item["strIngredient11"] for item in data_dict["drinks"]]
        # ing12 = [item["strIngredient12"] for item in data_dict["drinks"]]
        # ing13 = [item["strIngredient13"] for item in data_dict["drinks"]]
        # ing14 = [item["strIngredient14"] for item in data_dict["drinks"]]
        # ing15 = [item["strIngredient15"] for item in data_dict["drinks"]]
        # ing16 = [item["strIngredient16"] for item in data_dict["drinks"]]

        # Now 'instructions' is a list containing 'strInstructions' from each item
        print(id)

        # Return a JSON response containing the 'strInstructions' list
        res = id[0]

    except Exception as e:
        return jsonify({"error": str(e)})

    return render_template(
        "random.html",
        res=res,
        name=name[0],
        ing1=ing1[0],
        ing2=ing2[0],
        ing3=ing3[0],
        ing4=ing4[0],
        ing5=ing5[0],
        ing6=ing6[0],
        ing7=ing7[0],
        ing8=ing8[0],
        ing9=ing9[0],
        ing10=ing10[0],
        mes1=mes1[0],
        mes2=mes2[0],
        mes3=mes3[0],
        mes4=mes4[0],
        mes5=mes5[0],
        mes6=mes6[0],
        mes7=mes7[0],
        mes8=mes8[0],
        mes9=mes9[0],
        mes10=mes10[0],
        words_to_check=words_to_check,
    )


# @app.route("/")
# def get_instructions_from_api():
#     api_url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"

#     try:
#         response = requests.get(api_url)
#         data = response.json()

#         # Convert JSON string to a Python dictionary
#         data_dict = json.loads(json.dumps(data))

#         # Extract 'strInstructions' from each item in 'drinks'
#         instructions = [item["strInstructions"] for item in data_dict["drinks"]]

#         # Now 'instructions' is a list containing 'strInstructions' from each item
#         print(instructions)

#         # Return a JSON response containing the 'strInstructions' list
#         return jsonify(instructions[0])

#     except Exception as e:
#         return jsonify({"error": str(e)})
