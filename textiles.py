def textile_info(**kwargs):
    return{"name":"Rossy_textiles",
    "address":"1,AAA road,YYY city",
    "phone":"9942458690",
    "email":"jananykam054@gmail.com",
    "website":"https://google.com/chrome",
    "speciality":"This textile mainly focuses on brands"}

def floor(**kwargs):
    return{"first_floor":"men_collection",
    "second_floor":"women_collection",
    "third_floor":"kids_collection",
    "fourth_floor":"wedding_collection",
    "fifth_floor":"party_wear"}

def men_collection(**kwargs):
    return{"section": "Men Collection",
            "types": ["Shirts", "T-Shirts", "Jeans", "Blazers", "Ethnic Wear"],
            "brands": ["Levis", "Peter England", "Van Heusen"],
            "price_range": "₹499 - ₹4999",
            "sizes": ["S", "M", "L", "XL", "XXL"],
            "offers": "Flat 20% discount"}

def women_collection():
    return {"section": "Women Collection",
        "categories": [
            "Sarees",
            "Salwar Suits",
            "Kurtis",
            "Western Wear",
            "Lehengas",
            "Night Wear"
        ],
        "brands": [
            "Biba",
            "W for Woman",
            "Global Desi",
            "Zara",
            "H&M"
        ],
        "price_range": "₹699 - ₹9999",
        "sizes_available": ["XS", "S", "M", "L", "XL", "XXL"],
        "colors_available": ["Red", "Blue", "Black", "Pink", "Green", "Yellow"],
        "offers": "Buy 2 Get 1 Free on Kurtis"}

def kids_collection():
    return {"section": "Kids Collection",
        "age_groups": ["0-2 Years", "3-5 Years", "6-10 Years", "11-15 Years"],
        "categories": [
            "Frocks",
            "T-Shirts",
            "Shorts",
            "Jeans",
            "School Uniforms",
            "Ethnic Wear"
        ],
        "brands": [
            "Chicco",
            "Babyhug",
            "Gini & Jony",
            "Hopscotch"
        ],
        "price_range": "₹299 - ₹3999",
        "sizes_available": ["XS", "S", "M", "L"],
        "offers": "Flat 15% discount on School Uniforms"}

def wedding_collection():
    return {"section": "Wedding Collection",
        "categories": [
            "Bridal Sarees",
            "Lehengas",
            "Designer Gowns",
            "Sherwanis",
            "Reception Wear",
            "Engagement Dresses"
        ],
        "fabric_types": [
            "Silk",
            "Kanchipuram Silk",
            "Velvet",
            "Net",
            "Georgette"
        ],
        "brands": [
            "Manyavar",
            "Mohey",
            "Ritu Kumar",
            "Sabyasachi Inspired"
        ],
        "price_range": "₹4,999 - ₹1,50,000",
        "custom_stitching_available": True,}

def party_wear(**kwargs):
    return {
        "section": "Party Wear",

    }















