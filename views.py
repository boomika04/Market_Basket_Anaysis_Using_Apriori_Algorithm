import pandas as pd
from collections import defaultdict
from itertools import combinations
from django.shortcuts import render
from django.http import HttpResponse
import openpyxl


def index(request):
    return render(request, 'index.html') 
def contact(request):
    return render(request, 'contact.html') 
def about(request):
    return render(request, 'about.html') 
def veg(request):
    return render(request, 'veg.html') 
def dairy(request):
    return render(request, 'dairy.html') 
def fruits(request):
    return render(request, 'fruits.html') 
def cold(request):
    return render(request, 'cold.html') 
def addtocart(request):
    return render(request, 'addtocart.html') 
def dry(request):
    return render(request, 'dry.html') 
def spi(request):
    return render(request, 'spi.html') 

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        return render(request, 'index.html', {'username': username})
    return render(request, 'login.html')

product_details ={
    'Apple': {'name':'Apple','img_url': 'Apple.jpg', 'rate': '₹220(1kg)', 'offer': '25%off'},
    'Watermelon': {'name':'Watermelon','img_url': 'Watermelon.jpg', 'rate': '₹30(1kg)', 'offer': '20%off'},
    'Kiwi': {'name':'Kiwi','img_url': 'Kiwi.jpg', 'rate': '₹399(1kg)', 'offer': '50%off'},
    'Banana': {'name':'Banana','img_url': 'Banana.jpg', 'rate': '₹65(1kg)', 'offer': '35%off'},
    'Pineapple': {'name':'Pineapple','img_url': 'Pineapple.jpg', 'rate': '₹90(1kg)', 'offer':'40%off'},

    'Carrot': {'name':'Carrot','img_url': 'Carrot.jpg', 'rate': '₹35(per kg)', 'offer': '30%off'},
    'Potato': {'name':'Potato','img_url': 'Potato.jpg', 'rate': '₹35.00(per kg)', 'offer': '20%off'},
    'Tomato': {'name':'Tomato','img_url': 'Tomato.jpg', 'rate': '₹20(per kg)', 'offer': '50%off'},
    'Onion': {'name':'Onion','img_url': 'Onion.jpg', 'rate': '₹30(per kg)', 'offer': '25%off'},
    'Beetroot': {'name':'Beetroot','img_url': 'Beetroot.jpg', 'rate': '₹40(per kg)', 'offer': '15%off'},

    'Milk': {'name':'Milk','img_url': 'milk.jpg', 'rate': '₹102(200kg)', 'offer': '50%off'},
    'Fresh cream': {'name':'Fresh cream','img_url': 'Freshcream.jpeg', 'rate': '₹45(500ml)', 'offer': '15%off'},
    'Butter': {'name':'Butter','img_url': 'Butter.jpg', 'rate': '₹56(100g)', 'offer': '20%off'},
    'Cheese': {'name':'Cheese','img_url': 'Cheese.jpg', 'rate': '₹102(200kg)', 'offer': '50%off'},
    'Yogurt': {'name':'Yogurt','img_url': 'Yogurt.jpg', 'rate': '₹35(100kg)', 'offer': '19%off'},

    'Almonds': {'name':'Almonds','img_url': 'Almond.jpg', 'rate': '₹69.00(100g)', 'offer': '5%off'},
    'Cashew Nut': {'name':'Cashew Nut','img_url': 'Cashew.jpg', 'rate': '₹240(100g)', 'offer': '10%off'},
    'Pista': {'name':'Pista','img_url': 'Pista.jpg', 'rate': '₹360(250g)', 'offer': '50%off'},
    'Raisins': {'name':'Raisins','img_url': 'Raisins.jpg', 'rate': '₹41(100g)', 'offer': '54%off'},
    'Walnut': {'name':'Walnut','img_url': 'Walnut.jpg', 'rate': '₹143(100g)', 'offer': '28%off'},

    'Fanta': {'name':'Fanta','img_url': 'Fanta.jpg', 'rate': '₹48(1L)', 'offer': '10%off'},
    'Mazza': {'name':'Mazza','img_url': 'Mazza.jpg', 'rate': '₹40(1L)', 'offer': '12%off'},
    'Mountain Dew': {'name':'Mountain Dew','img_url': 'Mountaindew.jpg', 'rate': '₹55(1L)', 'offer': '14%off'},
    'Pepsi': {'name':'Pepsi','img_url': 'pepsi.jpg', 'rate': '₹43(1L)', 'offer': '27%off'},
    'Sprite': {'name':'Sprite','img_url': 'Sprite.jpg', 'rate': '₹45(1L)', 'offer': '15%off'},

    'Chilli Powder': {'name':'Chilli Powder','img_url': 'Chilli.jpg', 'rate': '₹40(100g)', 'offer': '25%off'},
    'Coriander Powder': {'name':'Coriander Powder','img_url': 'Coriander.jpg', 'rate': '₹28.8(100g)', 'offer': '10%off'},
    'Garam Masala': {'name':'Garam Masala','img_url': 'Garam.jpg', 'rate': '₹41(100g)', 'offer': '27%off'},
    'Turmeric': {'name':'Turmeric','img_url': 'Turmeric.jpeg', 'rate': '₹46(100g)', 'offer': '29%off'},
    'Cumin Seeds': {'name':'Cumin Seeds','img_url': 'Cumin.jpg', 'rate': '₹37(100g)', 'offer': '30%off'},
    }
def get_item_counts(transactions):
    item_counts = defaultdict(int)
    for transaction in transactions:
        for item in transaction:
            item_counts[item] += 1
    return item_counts

def join(candidate_itemsets, k):
    joined_itemsets = set()
    for itemset1 in candidate_itemsets:
        for itemset2 in candidate_itemsets:
            # Check if the first (k-1) items are the same in both sets
            common_items = itemset1.intersection(itemset2)
            if len(common_items) == k - 1:
                joined_itemset = itemset1.union(itemset2)
                if len(joined_itemset) == k + 1:
                    joined_itemsets.add(joined_itemset)
    return joined_itemsets

def prune(candidate_itemsets, transactions, min_support_count):
    pruned_itemsets = set()
    item_counts = get_item_counts(transactions)

    for itemset in candidate_itemsets:
        # Calculate the support count for the itemset
        support_count = sum(1 for transaction in transactions if itemset.issubset(transaction))
        if support_count >= min_support_count:
            pruned_itemsets.add(itemset)

    return pruned_itemsets

def product(request, item_name):
    # Accept the desired item from the user by click
    desired_item = item_name

    # Load data from the Excel file using Pandas
    excel_file = r'E:\Boomika\Mini-Project\Transaction1.xlsx'
    df = pd.read_excel(excel_file)

    # Extract data from the Pandas DataFrame, excluding the first row (headings) and first column (Transaction ID)
    transactions = []
    for index, row in df.iterrows():
        transaction = sorted([item.strip() for item in row[1:] if pd.notna(item)])  # Sort items in the transaction
        transactions.append(transaction)

    # Set the minimum support count to 2
    min_support_count = 2

    # Calculate the frequent itemsets

    k = 1
    frequent_itemsets = defaultdict(set)
    while True:
        if k == 1:
            candidate_itemsets = {frozenset([item]) for item in get_item_counts(transactions)}
        else:
            candidate_itemsets = join(frequent_itemsets[k - 1], k - 1)
        frequent_itemsets[k] = prune(candidate_itemsets, transactions, min_support_count)
        if not frequent_itemsets[k]:
            break
        k += 1
    
    # Filter frequent items bought together with the desired item that meet the criteria
    filtered_itemsets = frequent_itemsets[2]  # Consider only 2-itemsets
    filtered_itemsets = [itemset for itemset in filtered_itemsets if desired_item in itemset]
    f_item=[]
    # Find the product details of the main item
    main_product_details = product_details.get(desired_item, {'name': 'N/A', 'img_url': 'N/A', 'rate': 'N/A', 'offer': 'N/A'})

    # Create a list to store frequent item details
    if filtered_itemsets:
       print(f"Frequent Itemsets Bought Together with '{desired_item}' (Support Count >= 2):")
       for itemset in filtered_itemsets:
        support_itemset = sum(1 for transaction in transactions if itemset.issubset(transaction))
        antecedent = itemset - {desired_item}
        support_antecedent = sum(1 for transaction in transactions if antecedent.issubset(transaction))
        confidence = support_itemset / support_antecedent
        if confidence >= 0.30:
            f_item = itemset  # Set f_item to the current itemset
            print(f"Itemset: {', '.join(itemset)} (Support Count: {support_itemset}, Confidence: {confidence:.2f})")
            print(f_item)
    else:
      print("No frequent item found.")
    frequent_item_details = []
    
    if filtered_itemsets:
     for f_item in filtered_itemsets:
        if desired_item in f_item:
            mutable_f_item = set(f_item)  # Convert the frozenset to a mutable set
            mutable_f_item.discard(desired_item)  # Remove the desired_item from the mutable set
            frequent_item_names = list(mutable_f_item)  # Convert the set to a list of item names
            frequent_item_details.extend([product_details.get(item) for item in frequent_item_names])
            print(frequent_item_details)

    return render(request, 'product.html', {
        'main_product_details': main_product_details,
        'frequent_item_details': frequent_item_details,
    })
   