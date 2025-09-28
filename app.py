from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Medicine data
medicine_data = [
    {
        "Medicine": "Madana Phala Kwatha / Churna",
        "Brand": "Planet Ayurveda",
        "Website": "Planet Ayurveda",
        "Price": "₹600",
        "Stock": "In Stock",
        "Rating": "No reviews",
        "Link": "https://store.planetayurveda.com/products/sahasrayogam-madanaphala-choornam-100gm?variant=41643270471728"
    },
    {
        "Medicine": "Madana Phala Kwatha / Churna",
        "Brand": "Bixa Botanical",
        "Website": "Jio Mart",
        "Price": "₹340",
        "Stock": "In Stock",
        "Rating": "⭐ 4.2",
        "Link": "https://www.jiomart.com/p/groceries/madanphal-powder-200-gm-by-bixa-botanical/594109062?source=shoppingads&city=panindia_3p&utm_source=chatgpt.com"
    },
    {
        "Medicine": "Madana Phala Kwatha / Churna",
        "Brand": "bixa botanical",
        "Website": "Flipkart",
        "Price": "₹345",
        "Stock": "Hurry,Only a few left",
        "Rating": "⭐ 4.4",
        "Link": "https://www.flipkart.com/bixa-botanical-madanphal-powder-randia-dumetorum/p/itmcd9e680349c88?pid=AYDFYJZUR8M6ZGZN&lid=LSTAYDFYJZUR8M6ZGZNONRJJ7&marketplace=FLIPKART&utm_source=chatgpt.com"
    },

    # Updated Ghee (Ghrita) entries with real prices & stock status
    {
        "Medicine": "Ghee (Ghrita)",
        "Brand": "Baidyanath",
        "Website": "Baidyanath",
        "Price": "₹243",
        "Stock": "In Stock",
        "Rating": "⭐ 4.6",
        "Link": "https://www.baidyanath.com/products/baidyanath-mahatriphala-ghrita-pack-of-2-helps-get-relief-from-eye-related-issues-100-gms-each?_pos=1&_sid=32ff45bab&_ss=r"
    },
    {
        "Medicine": "Ghee (Ghrita)",
        "Brand": "Girveda",
        "Website": "Girveda",
        "Price": "₹999",
        "Stock": "Sold Out",
        "Rating": "⭐ 4.5",
        "Link": "https://www.girveda.com/products/panchtikta-ghee"
    },
    {
        "Medicine": "Ghee (Ghrita)",
        "Brand": "Tatsat",
        "Website": "Tatsat",
        "Price": "₹1,399",
        "Stock": "In Stock",
        "Rating": "⭐ 4.7",
        "Link": "https://tatsatayur.com/product/shata-dhauta-ghrita-benefits-100-times-washed-desi-cows-a2-ghee-moisturizing-cream-prepared-in-copper-pot-100gm/"
    },
    {
        "Medicine": "Ghee (Ghrita)",
        "Brand": "Svarasya",
        "Website": "Flipkart",
        "Price": "₹724",
        "Stock": "In Stock",
        "Rating": "⭐ 4.1",
        "Link": "https://www.flipkart.com/svarasya-shata-dhauta-ghrita-natural-desi-ghee-skin-moisturizer-25-gms/p/itm121eff0e35fcf"
    },

    {
        "Medicine": "Saindhava Lavana (Rock Salt)",
        "Brand": "24 Mantra",
        "Website": "Instant",
        "Price": "₹113",
        "Stock": "In Stock",
        "Rating": "⭐ 4.2",
        "Link": "https://www.flipkart.com/kda-himalayan-pink-salt-rock-saindhava-lavana/p/itm783923edcc351?pid=SATG6Z2GHKGKEDCZ&lid=LSTSATG6Z2GHKGKEDCZ8GINKB&marketplace=FLIPKART&utm_source=chatgpt.com"
    },
    {
        "Medicine": "Saindhava Lavana (Rock Salt)",
        "Brand": "Kalpatharu",
        "Website": "Manglore Cart",
        "Price": "₹135",
        "Stock": "In Stock",
        "Rating": "⭐ 4.0",
        "Link": "https://www.mangalorecart.com/products/kalpatharu-saindhava-lavana-1kg/1556268000000307949?utm_source=chatgpt.com"
    },
    {
        "Medicine": "Saindhava Lavana (Rock Salt)",
        "Brand": "Pragati",
        "Website": "Jiocart",
        "Price": "₹280",
        "Stock": "In Stock",
        "Rating": "⭐ 4.1",
        "Link": "https://www.jiomart.com/p/groceries/pragatinatural-saindhava-lavanam-rock-salt/604708132?utm_source=chatgpt.com"
    },
    {
        "Medicine": "Saindhava Lavana (Rock Salt)",
        "Brand": "Himalyan",
        "Website": "Flipkart",
        "Price": "₹195",
        "Stock": "In Stock",
        "Rating": "⭐ 4.3",
        "Link": "https://www.flipkart.com/kda-himalayan-pink-salt-rock-saindhava-lavana/p/itm783923edcc351?pid=SATG6Z2GHKGKEDCZ&lid=LSTSATG6Z2GHKGKEDCZ8GINKB&marketplace=FLIPKART&utm_source=chatgpt.com"
    },
    {
        "Medicine": "Honey (Madhu)",
        "Brand": "Baidyanath",
        "Website": "Baidyanath",
        "Price": "₹219",
        "Stock": "In Stock",
        "Rating": "⭐ 4.7",
        "Link": "https://www.baidyanath.com/products/honey-madhu?variant=47812673012013&country=IN&currency=INR&utm_source=chatgpt.com"
    },
    {
        "Medicine": "Honey (Madhu)",
        "Brand": "Dabur",
        "Website": "Big Basket",
        "Price": "₹118",
        "Stock": "In Stock",
        "Rating": "⭐ 4.1",
        "Link": "https://www.bigbasket.com/pd/240124/dabur-100-pure-honey-worlds-no1-honey-brand-with-no-sugar-adulteration-250-g/?z=MzE0OTkyNTYxMA&utm_source=chatgpt.com"
    },
    {
        "Medicine": "Honey (Madhu)",
        "Brand": "Dabur",
        "Website": "Flipkart",
        "Price": "₹70(Special Price)",
        "Stock": "In Stock",
        "Rating": "⭐3.9",
        "Link": "https://www.flipkart.com/dabur-100-pure-world-s-no-1-honey-brand-no-sugar-adulteration/p/itm30c6cf2f7a97f?pid=HNYEU6MGZXDDA5FE&lid=LSTHNYEU6MGZXDDA5FEX91WWW&marketplace=FLIPKART&utm_source=chatgpt.com"
    },

    {
        "Medicine": "Licorice (Yashtimadhu)",
        "Brand": "Dabur",
        "Website": "Flipkart",
        "Price": "₹96",
        "Stock": "In Stock",
        "Rating": "⭐ 4.1",
        "Link": "https://www.flipkart.com/dabur-mulethi-yashtimadhu-churna-100g-1-piece/p/itm0b7d18f8c7574?pid=AYDGA4QNSHTJ7EYZ&lid=LSTAYDGA4QNSHTJ7EYZSI8LP2&marketplace=FLIPKART&utm_source=chatgpt.com"
    },
    {
        "Medicine": "Licorice (Yashtimadhu)",
        "Brand": "Yuvika Muleth",
        "Website": "Tata 1mg",
        "Price": "₹155",
        "Stock": "In Stock",
        "Rating": "⭐ 4.2",
        "Link": "https://www.1mg.com/otc/yuvika-mulethi-multhi-spl-glycyrrhiza-glabra-yashtimadhu-jeshthamadha-licorice-root-otc520451?utm_source=chatgpt.com"
    },
    {
        "Medicine": "Licorice (Yashtimadhu)",
        "Brand": "Triphal",
        "Website": "Flipkart",
        "Price": "₹207",
        "Stock": "In Stock",
        "Rating": "⭐ 4.5",
        "Link": "https://www.flipkart.com/triphal-mulethi-powder-licorice-roots-yashtimadhu-churn-jethimadh-churan/p/itm23dca22466201?pid=AYDGQTXWBGGFAQQT&lid=LSTAYDGQTXWBGGFAQQTF2AXWI&marketplace=FLIPKART&utm_source=chatgpt.com"
    },
    
    {
        "Medicine": "Panchakola Churna",
        "Brand": "Kottakkal",
        "Website": "AyurCall",
        "Price": "₹21",
        "Stock": "In Stock",
        "Rating": "⭐ 4.2",
        "Link": "https://www.ayurcall.com/med/kottakkal_panchakola_churnam?utm_source=chatgpt.com"
    },
    {
        "Medicine": "Panchakola Churna",
        "Brand": "SNA OUSHADHASALA",
        "Website": "Sushain",
        "Price": "₹85",
        "Stock": "In Stock",
        "Rating": "⭐ 4",
        "Link": "https://sushainclinic.com/order/medicines/pro00017962/Sna-Oushadhasala-Panchakolachoornam-Jar-Of-50-Gm?utm_source=chatgpt.com"
    },
    {
        "Medicine": "Panchakola Churna",
        "Brand": "Malabar",
        "Website": "E-Ayur.com",
        "Price": "₹92",
        "Stock": "In Stock",
        "Rating": "⭐ 4.3",
        "Link": "https://www.eayur.com/index.php/ayurvedic/churna/malabar-panchakola-choornam.htm?utm_source=chatgpt.com"
    },
    {
        "Medicine": "Trikatu Churna",
        "Brand": "SHARMAYU",
        "Website": "FlipKart",
        "Price": "₹192",
        "Stock": "In Stock",
        "Rating": "⭐ 3.4",
        "Link": "https://www.flipkart.com/sharmayu-trikatu-churna-100-gm/p/itmaae7f46de4121?pid=AYDGAW7WZZMUZ8YW&lid=LSTAYDGAW7WZZMUZ8YWZETJJD&marketplace=FLIPKART&utm_source=chatgpt.com"
    },
    {
        "Medicine": "Trikatu Churna",
        "Brand": "Patanjali",
        "Website": "KeepFit",
        "Price": "₹40",
        "Stock": "In Stock",
        "Rating": "No reviews",
        "Link": "https://kapeefit.com/product/patanjali-trikatu-churna/?utm_source=chatgpt.com"
    },
    {
        "Medicine": "Trikatu Churna",
        "Brand": "Dabur",
        "Website": "Ayush Pharmacy",
        "Price": "₹123",
        "Stock": "In Stock",
        "Rating": "No reviews",
        "Link": "https://www.ayushpharmacy.com/products/dabur-trikatu-churna-100gm-SKU-1184?utm_source=chatgpt.com"
    },
    {
        "Medicine": "Guduchi (Giloy)",
        "Brand": "Baidyanath",
        "Website": "Baidyanath",
        "Price": "₹225",
        "Stock": "In Stock",
        "Rating": "⭐ 4.6",
        "Link": "https://www.baidyanath.com/products/guduchi-giloy-ghan-bati-60-tablets-pack-of-2-boosts-immunity-reduces-anxiety-improves-mental-strength?variant=47762352505133&country=IN&currency=INR"
    },
    {
        "Medicine": "Guduchi (Giloy)",
        "Brand": "Baidyanath",
        "Website": "Flipkart",
        "Price": "₹221",
        "Stock": "In Stock",
        "Rating": "⭐ 4.3",
        "Link": "https://www.flipkart.com/baidyanath-giloy-guduchi-ghan-bati-boosts-immunity-level-improves-blood-formation-useful-gout-joints-related-troubles-fights-against-various-infections-fever-conditions/p/itm4da2c63ed1737?pid=AYDG2S968DEFHARX&lid=LSTAYDG2S968DEFHARXKZRGKQ&marketplace=FLIPKART"
    },
{
        "Medicine": "Guduchi (Giloy)",
        "Brand": "Alam roots",
        "Website": "Alam roots",
        "Price": "₹128",
        "Stock": "In Stock",
        "Rating": "⭐ 3.9",
        "Link": "https://www.aalamroots.com/product/baidyanath-guduchyadi-giloy-ghan-bati-helps-to-boost-immunity/?v=f7c7a92a9cb9"
    },
    {
        "Medicine": "Guduchi (Giloy)",
        "Brand": "Patanjali",
        "Website": "Tata1mg",
        "Price": "₹93",
        "Stock": "In Stock",
        "Rating": "⭐ 4.5",
        "Link": "https://www.1mg.com/otc/patanjali-ayurveda-giloy-ghanvati-for-debility-fever-skin-urinary-disorders-otc324816?utm_source=google&utm_medium=cpc&utm_campaign={1mg_Paid_Google_OTC_Performance_Max_New_Users_Feed_Based}&utm_adgroup={adgroup}&utm_keyword=&wpsrc=Google%20AdWords&wpcid=23006259980&wpsnetn=x&wpkwn=&wpkmatch=&wpcrid=&wpscid=&wpkwid=&gad_source=1&gad_campaignid=23010275425&gbraid=0AAAAADSXlOQfhA4yVLTQr2zujdkn4PxwI&gclid=CjwKCAjwuePGBhBZEiwAIGCVS4vHPHe8pqDtehaL1wHAxDDQpZ2zwvrVFje9Sf6kgIZOV28vvqdGdRoCJmkQAvD_BwE"
    },
]

# Convert to DataFrame
df = pd.DataFrame(medicine_data)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home_remedies")
def home_remedies():
    return render_template("home_remedies.html")

@app.route("/buy_medicine", methods=["GET", "POST"])
def buy_medicine():
    medicines = sorted(df["Medicine"].unique())
    selected = request.form.get("medicine") if request.method == "POST" else None
    results = None
    if selected:
        results = df[df["Medicine"] == selected].to_dict(orient="records")
    return render_template("buy_medicine.html", medicines=medicines, results=results, selected=selected)

if __name__ == "__main__":
    app.run(debug=True)

