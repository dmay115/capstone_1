const input = document.querySelector("#ing_search");
const suggestions = document.querySelector(".suggestions ul");

const ings = [
    "Vodka",
    "Gin",
    "Rum",
    "Tequila",
    "Scotch",
    "Absolut Kurant",
    "Absolut Peppar",
    "Absolut Vodka",
    "Advocaat",
    "Aejo Rum",
    "Aftershock",
    "Agave Syrup",
    "Ale",
    "Allspice",
    "Almond Flavoring",
    "Almond",
    "Amaretto",
    "Angelica Root",
    "Angostura Bitters",
    "Anis",
    "Anise",
    "Anisette",
    "Aperol",
    "Apfelkorn",
    "Apple Brandy",
    "Apple Cider",
    "Apple Juice",
    "Apple Schnapps",
    "Apple",
    "Applejack",
    "Apricot Brandy",
    "Apricot Nectar",
    "Apricot",
    "Aquavit",
    "Asafoetida",
    "A\u00f1ejo Rum",
    "Bacardi Limon",
    "Bacardi",
    "Baileys Irish Cream",
    "Banana Liqueur",
    "Banana Rum",
    "Banana Syrup",
    "Banana",
    "Barenjager",
    "Basil",
    "Beef Stock",
    "Beer",
    "Benedictine",
    "Berries",
    "Bitter lemon",
    "Bitters",
    "Black Pepper",
    "Black Rum",
    "Black Sambuca",
    "Blackberries",
    "Blackberry Brandy",
    "Blackberry Schnapps",
    "Blackcurrant Cordial",
    "Blackcurrant Schnapps",
    "Blackcurrant Squash",
    "Blended Whiskey",
    "Blue Curacao",
    "Blue Maui",
    "Blueberries",
    "Blueberry Schnapps",
    "Bourbon",
    "Brandy",
    "Brown Sugar",
    "Butter",
    "Butterscotch Schnapps",
    "Cachaca",
    "Calvados",
    "Campari",
    "Canadian Whisky",
    "Candy",
    "Cantaloupe",
    "Caramel Coloring",
    "Carbonated Soft Drink",
    "Carbonated Water",
    "Cardamom",
    "Cayenne Pepper",
    "Celery Salt",
    "Celery",
    "Chambord Raspberry Liqueur",
    "Champagne",
    "Cherries",
    "Cherry Brandy",
    "Cherry Cola",
    "Cherry Grenadine",
    "Cherry Heering",
    "Cherry Juice",
    "Cherry Liqueur",
    "Cherry",
    "Chocolate Ice-cream",
    "Chocolate Liqueur",
    "Chocolate Milk",
    "Chocolate Syrup",
    "Chocolate",
    "Cider",
    "Cinnamon Schnapps",
    "Cinnamon",
    "Citrus Vodka",
    "Clamato Juice",
    "Cloves",
    "Club Soda",
    "Coca-Cola",
    "Cocktail Onion",
    "Cocoa Powder",
    "Coconut Cream",
    "Coconut Liqueur",
    "Coconut Milk",
    "Coconut Rum",
    "Coconut Syrup",
    "Coffee Brandy",
    "Coffee Liqueur",
    "Coffee",
    "Cognac",
    "Cointreau",
    "Cola",
    "Cold Water",
    "Condensed Milk",
    "Coriander",
    "Corn Syrup",
    "Cornstarch",
    "Corona",
    "Cranberries",
    "Cranberry Juice",
    "Cranberry Liqueur",
    "Cranberry Vodka",
    "Cream of Coconut",
    "Cream Sherry",
    "Cream Soda",
    "Cream",
    "Creme De Almond",
    "Creme De Banane",
    "Creme De Cacao",
    "Creme De Cassis",
    "Creme De Noyaux",
    "Creme Fraiche",
    "Crown Royal",
    "Crystal Light",
    "Cucumber",
    "Cumin Powder",
    "Cumin Seed",
    "Curacao",
    "Cynar",
    "Daiquiri Mix",
    "Dark Chocolate",
    "Dark Creme De Cacao",
    "Dark Rum",
    "Dark Soy Sauce",
    "Demerara Sugar",
    "Dr. Pepper",
    "Drambuie",
    "Dried Oregano",
    "Dry Vermouth",
    "Dubonnet Blanc",
    "Dubonnet Rouge",
    "Egg White",
    "Egg Yolk",
    "Egg",
    "Eggnog",
    "Erin Cream",
    "Espresso",
    "Everclear",
    "Fanta",
    "Fennel Seeds",
    "Firewater",
    "Flaked Almonds",
    "Food Coloring",
    "Forbidden Fruit",
    "Frangelico",
    "Fresca",
    "Fresh Basil",
    "Fresh Lemon Juice",
    "Fruit Juice",
    "Fruit Punch",
    "Fruit",
    "Galliano",
    "Garlic Sauce",
    "Gatorade",
    "Ginger Ale",
    "Ginger Beer",
    "Ginger",
    "Glycerine",
    "Godiva Liqueur",
    "Gold rum",
    "Gold Tequila",
    "Goldschlager",
    "Grain Alcohol",
    "Grand Marnier",
    "Granulated Sugar",
    "Grape juice",
    "Grape soda",
    "Grapefruit Juice",
    "Grapes",
    "Green Chartreuse",
    "Green Creme de Menthe",
    "Green Ginger Wine",
    "Green Olives",
    "Grenadine",
    "Ground Ginger",
    "Guava juice",
    "Guinness stout",
    "Guinness",
    "Half-and-half",
    "Hawaiian punch",
    "Hazelnut liqueur",
    "Heavy cream",
    "Honey",
    "Hooch",
    "Hot Chocolate",
    "Hot Damn",
    "Hot Sauce",
    "Hpnotiq",
    "Ice-Cream",
    "Ice",
    "Iced tea",
    "Irish cream",
    "Irish Whiskey",
    "Jack Daniels",
    "Jello",
    "Jelly",
    "Jagermeister",
    "Jim Beam",
    "Johnnie Walker",
    "Kahlua",
    "Key Largo Schnapps",
    "Kirschwasser",
    "Kiwi liqueur",
    "Kiwi",
    "Kool-Aid",
    "Kummel",
    "Lager",
    "Lemon Juice",
    "Lemon Peel",
    "Lemon soda",
    "Lemon vodka",
    "Lemon-lime soda",
    "lemon-lime",
    "lemon",
    "Lemonade",
    "Licorice Root",
    "Light Cream",
    "Light Rum",
    "Lillet",
    "Lime juice cordial",
    "Lime Juice",
    "Lime liqueur",
    "Lime Peel",
    "Lime vodka",
    "Lime",
    "Limeade",
    "Madeira",
    "Malibu Rum",
    "Mandarin",
    "Mandarine napoleon",
    "Mango",
    "Maple syrup",
    "Maraschino cherry juice",
    "Maraschino Cherry",
    "Maraschino Liqueur",
    "Margarita mix",
    "Marjoram leaves",
    "Marshmallows",
    "Maui",
    "Melon Liqueur",
    "Melon Vodka",
    "Mezcal",
    "Midori Melon Liqueur",
    "Midori",
    "Milk",
    "Mint syrup",
    "Mint",
    "Mountain Dew",
    "Nutmeg",
    "Olive Oil",
    "Olive",
    "Onion",
    "Orange Bitters",
    "Orange Curacao",
    "Orange Juice",
    "Orange liqueur",
    "Orange Peel",
    "Orange rum",
    "Orange Soda",
    "Orange spiral",
    "Orange vodka",
    "Orange",
    "Oreo cookie",
    "Orgeat Syrup",
    "Ouzo",
    "Oyster Sauce",
    "Papaya juice",
    "Papaya",
    "Parfait amour",
    "Passion fruit juice",
    "Passion fruit syrup",
    "Passoa",
    "Peach brandy",
    "Peach juice",
    "Peach liqueur",
    "Peach Nectar",
    "Peach Schnapps",
    "Peach Vodka",
    "Peach",
    "Peachtree schnapps",
    "Peanut Oil",
    "Pepper",
    "Peppermint extract",
    "Peppermint Schnapps",
    "Pepsi Cola",
    "Pernod",
    "Peychaud bitters",
    "Pina colada mix",
    "Pineapple Juice",
    "Pineapple rum",
    "Pineapple vodka",
    "Pineapple-orange-banana juice",
    "Pineapple",
    "Pink lemonade",
    "Pisang Ambon",
    "Pisco",
    "Plain Chocolate",
    "Plain Flour",
    "Plums",
    "Port",
    "Powdered Sugar",
    "Purple passion",
    "Raisins",
    "Raspberry cordial",
    "Raspberry Jam",
    "Raspberry Juice",
    "Raspberry Liqueur",
    "Raspberry schnapps",
    "Raspberry syrup",
    "Raspberry Vodka",
    "Red Chile Flakes",
    "Red Chili Flakes",
    "Red Hot Chili Flakes",
    "Red Wine",
    "Rhubarb",
    "Ricard",
    "Rock Salt",
    "Root beer schnapps",
    "Root beer",
    "Roses sweetened lime juice",
    "Rosewater",
    "Rumple Minze",
    "Rye Whiskey",
    "Sake",
    "Salt",
    "Sambuca",
    "Sarsaparilla",
    "Schnapps",
    "Schweppes Lemon",
    "Schweppes Russchian",
    "Sherbet",
    "Sherry",
    "Sirup of roses",
    "Sloe Gin",
    "Soda Water",
    "Sour Apple Pucker",
    "Sour Mix",
    "Southern Comfort",
    "Soy Milk",
    "Soy Sauce",
    "Soya Milk",
    "Soya Sauce",
    "Spiced Rum",
    "Sprite",
    "Squeezed Orange",
    "Squirt",
    "Strawberries",
    "Strawberry juice",
    "Strawberry liqueur",
    "Strawberry Schnapps",
    "Strawberry syrup",
    "Sugar Syrup",
    "Sugar",
    "Sunny delight",
    "Surge",
    "Swedish punsch",
    "Sweet and Sour",
    "Sweet Cream",
    "Sweet Vermouth",
    "Tabasco Sauce",
    "Tang",
    "Tawny port",
    "Tea",
    "Tennessee whiskey",
    "Tequila rose",
    "Tia Maria",
    "Tomato Juice",
    "Tomato",
    "Tonic Water",
    "Triple Sec",
    "Tropicana",
    "Tuaca",
    "Vanilla extract",
    "Vanilla Ice-Cream",
    "Vanilla liqueur",
    "Vanilla schnapps",
    "Vanilla syrup",
    "Vanilla vodka",
    "Vanilla",
    "Vermouth",
    "Vinegar",
    "Water",
    "Watermelon schnapps",
    "Whipped Cream",
    "Whipping Cream",
    "White chocolate liqueur",
    "White Creme de Menthe",
    "White grape juice",
    "White port",
    "White Rum",
    "White Vinegar",
    "White Wine",
    "Wild Turkey",
    "Wildberry schnapps",
    "Wine",
    "Worcestershire Sauce",
    "Wormwood",
    "Yeast",
    "Yellow Chartreuse",
    "Yoghurt",
    "Yukon Jack",
    "Zima",
    "Caramel Sauce",
    "Chocolate Sauce",
    "Lillet Blanc",
    "Peach Bitters",
    "Mini-snickers bars",
    "Prosecco",
    "Salted Chocolate",
    "Martini Rosso",
    "Martini Bianco",
    "Martini Extra Dry",
    "Fresh Lime Juice",
    "Fresh Mint",
    "Rosemary",
    "Habanero Peppers",
    "Ilegal Joven mezcal",
    "Elderflower cordial",
    "Rosso Vermouth",
    "Creme de Violette",
    "Cocchi Americano",
    "White Vermouth",
    "Dry Curacao",
    "Nocino",
    "Averna",
    "Ramazzotti",
    "Fernet-Branca",
    "Allspice Dram",
    "Falernum",
    "Singani",
    "Arrack",
    "Blackstrap rum",
    "Ginger Syrup",
    "Honey syrup",
    "Blended Scotch",
    "Islay single malt Scotch",
    "151 proof rum",
    "7-up",
    "Absinthe",
    "Absolut citron",
    "Creme de Mure",
    "Olive Brine",
    "Pineapple Syrup",
    "St. Germain",
    "Lavender",
    "Whiskey",
    "Whisky",
    "Pomegranate juice",
    "Watermelon",
    "Chareau",
    "Cinnamon Whisky",
    "Red Bull",
    "Diet Coke",
    "Rosemary Syrup",
    "Figs",
    "Thyme",
    "Orange Slice",
    "Blood Orange",
    "Amaro Montenegro",
    "Ruby Port",
    "Rose",
    "Tajin",
];

let results = [];

function search(str) {
    let results = [];
    for (let strings of ings) {
        if (strings.toLowerCase().includes(str)) {
            results.push(strings);
        }
    }
    return showSuggestions(results, str);
}

function searchHandler() {
    let searchStr = input.value.toLowerCase();
    suggestions.innerText = "";
    search(searchStr);
}

function showSuggestions(arr, searched) {
    if (input.value === "") {
        search();
    }
    for (let str of arr) {
        const item = document.createElement("li");
        let bolded = str.replace(searched, `<b>${searched}</b>`);
        item.innerHTML = bolded;
        suggestions.appendChild(item);
    }
}

function useSuggestion(e) {
    input.value = e.target.innerText;
    suggestions.innerText = "";
}

document.addEventListener("DOMContentLoaded", function () {
    const submitBtn = document.getElementById("submitBtn");

    if (submitBtn) {
        submitBtn.addEventListener("click", function () {
            const ingredient = document.getElementById("ing_search").value;
            console.log(ingredient);
            // Assuming you have a Flask route to handle the submission
            fetch("/submit-ingredient", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ ingredient: ingredient }),
            })
                .then(function (response) {
                    if (!response.ok) {
                        throw new Error("Network response was not ok");
                    }
                    location.reload();
                    return response.json();
                })
                .then(function (data) {
                    console.log(data);
                    if (data.success) {
                        console.log("Ingredient submitted successfully");
                        location.reload();
                    } else {
                        console.error(
                            "Error submitting ingredient:",
                            data.error
                        );
                        // Display error message to the user, e.g., using an alert
                        alert("Error submitting ingredient: " + data.error);
                        location.reload();
                    }
                })
                .catch(function (error) {
                    console.error("Error submitting ingredient:", error);
                    // Display error message to the user, e.g., using an alert
                    alert("Error submitting ingredient: " + error.message);
                });
        });
    }
});

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".deleteBtn").forEach(function (button) {
        button.addEventListener("click", function () {
            const ingredientId = this.getAttribute("data-ingredient-id");

            fetch("/delete-ingredient", {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ ingredientId: ingredientId }),
            })
                .then(function (response) {
                    if (!response.ok) {
                        throw new Error("Network response was not ok");
                    }
                    return response.json();
                })
                .then(function (data) {
                    // Optionally, you can remove the ingredient from the UI
                    button.parentNode.remove();
                    console.log("Ingredient deleted successfully");
                })
                .catch(function (error) {
                    console.error("Error deleting ingredient:", error);
                });
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const submitSelectionBtn = document.getElementById("submitSelection");

    if (submitSelectionBtn) {
        submitSelectionBtn.addEventListener("click", function () {
            const selectedIngredients = getSelectedIngredients();

            // Extract ingredientName values from the objects
            const ingredientNames = selectedIngredients.map(
                (ingredient) => ingredient.ingredientName
            );

            console.log(ingredientNames);

            // Create a query string from the selected ingredient names
            const queryString = ingredientNames.join(",");

            console.log(queryString);
            // Redirect to the Flask route with the query string
            window.location.href = `/drink-search?ingredients=${queryString}`;
        });
    }
    function getSelectedIngredients() {
        var checkboxes = document.querySelectorAll(
            ".ingredientCheckbox:checked"
        );
        var selectedIngredients = Array.from(checkboxes).map(function (
            checkbox
        ) {
            return {
                ingredientID: checkbox.getAttribute("data-ingredient-id"),
                ingredientName: checkbox.value,
            };
        });
        return selectedIngredients;
    }
});

input.addEventListener("keyup", searchHandler);
suggestions.addEventListener("click", useSuggestion);
