import time
import random
import webbrowser

# List of 40 unique keywords

keywords0=['israel vs iran', 'world wide ppp apis', 'netanyahu', 'idhazin oru oram', 
           'ipl 2024', 'purple cap table latest', 'income inequality in india', 'ssn college vs snu c', 'cyber security', 
           'mern vs java springboot', 'political polarization in india', 'apj abdul kalam books', 'ind vs pak', 'electricity ', 'nta', 'live wallpapers pc 4k', 
           'Economic equity vs eqaulity', 'chinese pandas vs ml pandas', 'latest gen ai pdts', 'airchat', 'solar panels economic benefits mkbhd', 'mutual funds vs bonds', 
           'anirudh', 'mexican tacos', 'atomberg', 'nextlevel',  'linkedin', 'noise headphones', 'isl latest',  'marvel what if',   'apis for image gen free','perxplexity',
           'suno ai','backtracking','hackathons',"YouTube tips","Online learning","Data analysis courses","Artificial intelligence applications",
           "Andrew yang"]

keywords1 = ["gop meaning", "vp", "soemthing", "nothing", "hey there", 
             "open ai vs grok", "chatgpt vs grok", "gdrive", "gmail", "light yagami", 
             "keyword11", "aot latest episode", "ananth vp ", "elon ma", "pv", "llama ", 
             "lmao full in chat ", "lol full meaning", "sam ", "uncle sam meme", "us vs russ", "geopolitics", 
             "bigg boss", "take", "give", "ggyuhjkn", "kwjfn", "nile", "flikart", "flipkart", 
             "rain water harvesting ppt", "okay", "hit it off", "edgy"] +  [
    "IPL 2024",  "BCCI","Stock market","Income tax","Travel deals",  "Government schemes"
]

keywords2=[
    "Regional cinema releases", "Music awards show",  "Celebrity wedding",   "Viral social media post",   "Sports tournament schedule",  
    "Public speaker",  "Motivational quotes","Investment advice","Real estate market","Home loan options",
    "Car buying guide","Travel insurance","Pet adoption","Weekend getaways","Adventure travel",
    "Online shopping deals","Discount coupons","Online reviews platform","Food delivery app",
    "Streaming service recommendations","Subscription boxes","DIY projects",
    "Home improvement tips","Gardening for beginners","Pet training guide",
    "Financial planning","Retirement savings","Tax saving tips", "Legal advice", "Consumer rights", "Mental health resources",
    "Stress management techniques","Healthy sleep habits","Workout routines",
    "Meditation apps","Travel vlogs","Food photography tips","Social media marketing","Content marketing tools","E-commerce SEO strategies"
]


keywords3= [
    "LSG vs DC","Chamkila movie",
    "Baisakhi 2024","Samayam Telugu","Inter Results 2024","KL Rahul","Iran","Kerala Blasters",
    "Bharti Hexacom","Park Bo Ram","Moneycontrol","TCS Results","Livemint","Amar Ujala","Punjab",
    "Truong My Lan","Indian Super League","Netflix",  "Amazon Prime", "Hotstar",  "GAAMI",  
    "Jawan movie",   "Gadar 2 movie",  "Cricket news","Stock market","Income tax",
    "Government schemes", "RBI policy","IPL 2024",  "BCCI","Covid-19 update","Travel booking","E-commerce deals",
    "PUBG Mobile",  "Free Fire",  
    "WhatsApp update","Instagram update","YouTube tips","Online learning","Work from home","Bitcoin price",
]

keywords4= [
    "Ayurvedic remedies",
    "Astrology predictions","Viral video",  
    "Weather update",
    "Ration card status","Pan Card download","Aadhaar update","IRCTC booking","Flight tickets","Fuel prices",
    "Share market tips","Tax return filing","Scholarship schemes", "Entrance exams", "Healthy recipes",
    "Fitness tips","Makeup tutorials","Fashion trends","Home decor ideas","Relationship advice","Parenting tips","Pet care",
    "Learning a new language","Coding tutorials","Data science course","Content creation tips","Stock market analysis","Investment options",
    "Personal finance tips",
    "Mental health awareness", "Meditation techniques", "Travel destinations", "Sustainable living", "E-waste disposal",
    "Movie reviews","Music streaming","Audiobook recommendations","E-sports tournament",  
    "Social media challenges","Online games",
]

keywords5= [
    "Upcoming festivals","Public holidays 2024","Government jobs","Railway recruitment","Scholarship applications","University admissions","Exam results","Local news",
    "Public transport updates","Traffic alerts","Restaurant reviews","Movie release dates","Book recommendations","Travel hacks","Language learning apps","Online courses",
    "Productivity tips","Remote work opportunities","Freelancing platforms","E-commerce apps","Online payment methods","Cybersecurity awareness","Social media trends",
    "Viral content analysis","Blogging platforms","Video editing software","Freelance writing tips", "Content marketing strategies", "E-commerce business ideas", 
    "Start-up funding", "Sustainable fashion","Eco-friendly products", "Renewable energy sources", "Climate change awareness", "Volunteer opportunities",
    "Social work initiatives","Historical documentaries","Zomato","Learning a new skill","Brain training games","Healthy lifestyle tips",
]

d={0:keywords0,1:keywords1,2:keywords2,3:keywords3,4:keywords4,5:keywords5}
# # Open Edge and search for each keyword
for keyword in random.sample(d[random.randint(0, 5)],34):
    time.sleep(random.randint(7, 13))
    webbrowser.open(f"https://www.bing.com/search?q={keyword}&form=QBLH&sp=-1&pq={keyword}&sc=8-7&qs=n&sk=&cvid=8C1B3D3B7A9D4E1F9C0E8C7D8D7E5F3D")