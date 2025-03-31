import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import base64
from io import BytesIO

# Set page config
st.set_page_config(
    page_title="Mutya ning Kapampangan 2023 Q&A Analytics",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to load the Mutya ning Kapampangan 2023 data
@st.cache_data
def load_data():
    """Load the Mutya ning Kapampangan 2023 data from YouTube transcript analysis."""
    
    data = [
        # Semifinal Round Questions
        {
            "id": 1,
            "year": 2023,
            "candidate_name": "Kate Lee Kino",
            "candidate_number": 22,
            "location": "Santo Tomas",
            "question": "What role should a beauty pageant winner play in advocating for social causes, and what cause would you prioritize?",
            "answer": "I believe that the winner should serve as a good role model. If asked what I would advocate for, it would be about mental health awareness. Since I have personally experienced losing a best friend, I want to let them know that their feelings are valued and that there is a safe space where they can talk about it.",
            "word_count": 57,
            "sentence_count": 3,
            "filler_word_count": 1,
            "sentiment_score": 0.4,
            "readability_score": 82.5,
            "power_keywords": "mental health, awareness, valued, safe space",
            "duration": 32.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Semifinalist"
        },
        {
            "id": 2,
            "year": 2023,
            "candidate_name": "Nelia Marie Dionon",
            "candidate_number": 16,
            "location": "San Fernando",
            "question": "As a title holder, what strategies would you employ to engage with Kapampangan community and promote volunteerism?",
            "answer": "As a public figure, I would use my platforms and social media. I believe this would help promote tourism and what we as Kapampangans believe in and are proud of. That is why I want to utilize this platform of mine and really spread what I am proud of to my fellowmen.",
            "word_count": 49,
            "sentence_count": 3,
            "filler_word_count": 2,
            "sentiment_score": 0.65,
            "readability_score": 76.0,
            "power_keywords": "platforms, social media, tourism, proud, fellowmen",
            "duration": 28.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Semifinalist"
        },
        {
            "id": 3,
            "year": 2023,
            "candidate_name": "Samantha Mhee-Ashtelle Duyay",
            "candidate_number": 4,
            "location": "Bacolor",
            "question": "If crowned as a title holder, how do you envision using your platform to make a positive impact on the Kapampangan community?",
            "answer": "Mental health awareness is something that is important to me. I would like to prioritize not just the tourism of Pampanga but also the people of Pampanga. Mental health is becoming taboo and I want to eliminate that stigma. I want to have open conversations while accepting people's thoughts.",
            "word_count": 52,
            "sentence_count": 4,
            "filler_word_count": 3,
            "sentiment_score": 0.5,
            "readability_score": 72.0,
            "power_keywords": "mental health, awareness, stigma, open conversations",
            "duration": 30.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Semifinalist"
        },
        {
            "id": 4,
            "year": 2023,
            "candidate_name": "Maria Gachi Golospe",
            "candidate_number": 13,
            "location": "Mexico",
            "question": "The recently concluded Miss Universe opened its doors to mothers, transgender women, and plus-sized women. What is your stand on this inclusivity?",
            "answer": "Good evening. Ladies and gentlemen, my stand on Miss Universe and transgender women and mothers is that I am for them. Women have substances and they should have substances that they can improve. Women exist as long as they have their purpose and passion in life. Winning in Miss Universe could be their platform to express themselves, and there is nothing wrong about that. In fact, being a woman and having self-awareness is the main reason why we stand on honorable pageants.",
            "word_count": 85,
            "sentence_count": 5,
            "filler_word_count": 1,
            "sentiment_score": 0.75,
            "readability_score": 68.0,
            "power_keywords": "transgender, inclusivity, purpose, passion, self-awareness",
            "duration": 45.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Semifinalist"
        },
        {
            "id": 5,
            "year": 2023,
            "candidate_name": "Maria Cecilia Ann Ocao",
            "candidate_number": 21,
            "location": "Santa Rita",
            "question": "Beauty pageants are often criticized for perpetuating certain beauty standards. How do you plan to challenge these stereotypes and promote a more inclusive definition of beauty?",
            "answer": "I believe that each of us has our own unique personality. In beauty pageants, there are indeed such standards, but looks aren't really that important. There are many physical elements, but what's important is personality and purpose. I am standing here for the purpose of inclusivity where everyone can participate. I am standing up for that mission with heart, with substance.",
            "word_count": 62,
            "sentence_count": 5,
            "filler_word_count": 2,
            "sentiment_score": 0.7,
            "readability_score": 71.0,
            "power_keywords": "unique personality, inclusivity, purpose, substance",
            "duration": 35.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Semifinalist"
        },
        {
            "id": 6,
            "year": 2023,
            "candidate_name": "Stacey Davide",
            "candidate_number": 9,
            "location": "Mabalacat City",
            "question": "Over 30 years after the eruption of Mount Pinatubo, Pampanga has been able to thrive and develop again. What do you think are the main characteristics of Kapampangans that helped them bounce back better from disaster?",
            "answer": "We Kapampangans are resilient and we are not hindered by any difficulty that we face in life. Because we have the mindset that no matter what difficulties or obstacles we face, with family surrounding us and community supporting us, we can stand up as one.",
            "word_count": 47,
            "sentence_count": 2,
            "filler_word_count": 0,
            "sentiment_score": 0.8,
            "readability_score": 75.0,
            "power_keywords": "resilient, difficulties, obstacles, family, community",
            "duration": 25.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Top 5 Finalist"
        },
        {
            "id": 7,
            "year": 2023,
            "candidate_name": "Joanne Marie Thornley",
            "candidate_number": 1,
            "location": "Angeles City",
            "question": "In the world of beauty pageants today, it is encouraged for candidates to have their own respective advocacies. What do you think about this?",
            "answer": "I think beauty pageants are more than a display of beauty and charm. Beauty pageants are a means to connect with a wider audience and speak about your beliefs, and for me, advocacy is the biggest role in the beauty pageant industry. To be able to speak about things that people are afraid to talk about, to have a voice and have a cause to fight for, is something that you should be most proud of. I think beauty pageants are a great way to talk about causes that I believe in.",
            "word_count": 90,
            "sentence_count": 4,
            "filler_word_count": 3,
            "sentiment_score": 0.85,
            "readability_score": 79.0,
            "power_keywords": "advocacy, voice, cause, beliefs, audience",
            "duration": 48.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "1st Runner-Up"
        },
        {
            "id": 8,
            "year": 2023,
            "candidate_name": "Gabrielle Galapia",
            "candidate_number": 11,
            "location": "Magalang",
            "question": "Pampanga has limited natural attractions, no lakes, no beaches, and no cold climate. With such limitations, as a multimedia artist, how can you promote Pampanga to tourists and travelers?",
            "answer": "I know that what people actually look for beyond looks and feel is the experience they get while they are in that place. Personally, I would like to invite them to my town of Magalang during our Lubenas Pasku on December 13, where they can see different balangays coming together and showcase their arts and crafts during the festival. They can see people coming together, being inspired through great lengths, and will want to come back to Pampanga for that experience.",
            "word_count": 85,
            "sentence_count": 3,
            "filler_word_count": 1,
            "sentiment_score": 0.75,
            "readability_score": 81.0,
            "power_keywords": "experience, Lubenas Pasku, festival, arts, crafts",
            "duration": 44.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Top 5 Finalist"
        },
        {
            "id": 9,
            "year": 2023,
            "candidate_name": "Sophia Bianca Santos",
            "candidate_number": 8,
            "location": "Lubao",
            "question": "What does the word 'Mutya' mean to you, and how does it support your identity?",
            "answer": "Pampanga is known as the culinary capital of the Philippines because of our culinary traditions. Our culinary traditions are our pride, part of our culture, and an invaluable source of life, inspiration, and identity. It is a legacy from the past, what we live by today, and what we pass on to future generations. Indeed, Pampanga deserves to be known, recognized, and promoted to the world because of our culinary traditions.",
            "word_count": 72,
            "sentence_count": 4,
            "filler_word_count": 0,
            "sentiment_score": 0.8,
            "readability_score": 77.0,
            "power_keywords": "culinary traditions, pride, culture, legacy, generations",
            "duration": 38.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Top 5 Finalist"
        },
        {
            "id": 10,
            "year": 2023,
            "candidate_name": "Salma Emma",
            "candidate_number": 15,
            "location": "Porac",
            "question": "Which is more important to you, love or career, and why?",
            "answer": "Thank you for that question, Sir Jon. For me as a beauty queen, love and career are two things that go hand in hand to create a meaningful legacy. I believe they shouldn't be separated but combined to make a better impact, to make a good impact on the world.",
            "word_count": 50,
            "sentence_count": 3,
            "filler_word_count": 1,
            "sentiment_score": 0.9,
            "readability_score": 83.0,
            "power_keywords": "love, career, legacy, impact, meaningful",
            "duration": 27.0,
            "round": "Semifinal",
            "winner": True,
            "placement": "Winner"
        },
        
        # Final Round Questions (Local Culture and Traditions)
        {
            "id": 11,
            "year": 2023,
            "candidate_name": "Salma Emma",
            "candidate_number": 15,
            "location": "Porac",
            "question": "Can you share a meaningful aspect of local culture and traditions that you are proud of? How would you showcase it as a titleholder?",
            "answer": "Thank you for that question. In Porac, we have this traditional cooking method that can make any dish special. It's called Vuro, where we stuff these foods in bamboo and cook them patiently at just the right temperature. I think this is very important because it reminds me of myself. Just like bamboo, I am constantly progressing. I will showcase it to the world by showing everyone that I am in my natural self, that Kapampangan traditions are now more beautiful than ever.",
            "word_count": 87,
            "sentence_count": 6,
            "filler_word_count": 1,
            "sentiment_score": 0.95,
            "readability_score": 86.0,
            "power_keywords": "Vuro, traditional cooking, bamboo, progressing, natural",
            "duration": 46.0,
            "round": "Final",
            "winner": True,
            "placement": "Winner"
        },
        {
            "id": 12,
            "year": 2023,
            "candidate_name": "Joanne Marie Thornley",
            "candidate_number": 1,
            "location": "Angeles City",
            "question": "Can you share a meaningful aspect of local culture and traditions that you are proud of? How would you showcase it as a titleholder?",
            "answer": "Pampanga is known as the culinary capital of the Philippines, but I think it's more than just the taste of the cuisine that we offer. For us, food is a way of sharing our love for one another. These recipes on our table have been perfected through generations for your loved ones to enjoy the dish the same way you do. I think the beauty of us being the culinary capital of the Philippines is that we can show our love for one another through food. As a beauty queen, I would like to focus on that aspect of our claim that Kapampangan culture is all about love.",
            "word_count": 102,
            "sentence_count": 5,
            "filler_word_count": 2,
            "sentiment_score": 0.9,
            "readability_score": 82.0,
            "power_keywords": "culinary capital, food, love, generations, recipes",
            "duration": 52.0,
            "round": "Final",
            "winner": False,
            "placement": "1st Runner-Up"
        },
        {
            "id": 13,
            "year": 2023,
            "candidate_name": "Sophia Bianca Santos",
            "candidate_number": 8,
            "location": "Lubao",
            "question": "Can you share a meaningful aspect of local culture and traditions that you are proud of? How would you showcase it as a titleholder?",
            "answer": "If I win as Mutya ning Kapampangan, I want to be an ambassador for our culture, arts, and tourism. Like our land's Sagita Festival. Sagita Festival aims to celebrate our identity, our cultural heritage, and our vibrant community. Sagita is one of the sources of life in our land. Indeed, the Sagita Festival deserves to be known, recognized, and promoted to the world.",
            "word_count": 65,
            "sentence_count": 5,
            "filler_word_count": 0,
            "sentiment_score": 0.85,
            "readability_score": 78.0,
            "power_keywords": "Sagita Festival, culture, heritage, identity, ambassador",
            "duration": 34.0,
            "round": "Final",
            "winner": False,
            "placement": "Top 5 Finalist"
        },
        {
            "id": 14,
            "year": 2023,
            "candidate_name": "Gabrielle Galapia",
            "candidate_number": 11,
            "location": "Magalang",
            "question": "Can you share a meaningful aspect of local culture and traditions that you are proud of? How would you showcase it as a titleholder?",
            "answer": "Winning the Mutya ning Kapampangan crown is a huge responsibility as a beauty queen. You have a platform to showcase various things. One aspect of local culture that I would like to showcase is actually the Pasku that I mentioned earlier. This festival is very meaningful to me because it touches my heart to see multiple balangays come together and be showcased all over Magalang as one beautiful parol. And I will showcase this aspect not only as a beauty queen but also as a multimedia artist because I know that content and social media are what reach people the most. And I will use these platforms to promote it and show that Magalang and Pampanga as a whole.",
            "word_count": 115,
            "sentence_count": 6,
            "filler_word_count": 3,
            "sentiment_score": 0.8,
            "readability_score": 76.0,
            "power_keywords": "Pasku, festival, balangays, parol, multimedia",
            "duration": 58.0,
            "round": "Final",
            "winner": False,
            "placement": "Top 5 Finalist"
        },
        {
            "id": 15,
            "year": 2023,
            "candidate_name": "Stacey Davide",
            "candidate_number": 9,
            "location": "Mabalacat City",
            "question": "Can you share a meaningful aspect of local culture and traditions that you are proud of? How would you showcase it as a titleholder?",
            "answer": "Pampanga is undoubtedly rich in culture and history. It is known as the culinary capital of the Philippines, but as Kapampangans, I believe there are three things that I am most proud of. First is our unique story. Second is our art. And lastly, the Kapampangan people themselves. As individuals and as a community, our unique story is a testament that we can strive and overcome obstacles. Second is our art. Our culinary masterpiece craftsmanship is displayed as a living canvas. Lastly, the Kapampangan people themselves. Our collective efforts make our province thrive and extraordinary. Together we must carry and be proud. Be proud of who we are.",
            "word_count": 117,
            "sentence_count": 10,
            "filler_word_count": 2,
            "sentiment_score": 0.85,
            "readability_score": 74.0,
            "power_keywords": "unique story, art, Kapampangan people, collective efforts, proud",
            "duration": 60.0,
            "round": "Final",
            "winner": False,
            "placement": "Top 5 Finalist"
        },
        {
            "id": 27,
            "year": 2024,
            "candidate_name": "Candidate from San Fernando",
            "candidate_number": None,
            "location": "San Fernando",
            "question": "How are Kapampangan women different from other Filipino women around the country?",
            "answer": "Kapampangan women are different because we are now living under the theme of empowered modern Kapampangan women with determination and confidence. We are Kapampangans. We are not compromising our lives, but we are working hard to achieve our ambitions. I believe that we are adaptable, and we are adapting ourselves to survive in the modern society. And I believe that every woman, every Kapampangan has the ability for empowerment. It's up to us to dive in and embrace it.",
            "word_count": 81,
            "sentence_count": 6,
            "filler_word_count": 0,
            "sentiment_score": 0.85,
            "readability_score": 80.0,
            "power_keywords": "empowered, determination, confidence, adaptable, ambitions, modern",
            "duration": 43.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "1st Runner-Up"
        },
        {
            "id": 28,
            "year": 2024,
            "candidate_name": "Candidate from Mabalacat",
            "candidate_number": None,
            "location": "Mabalacat",
            "question": "Kamu is a Kapampangan word that means gift or blessing. What do you think is the best kamu in your life?",
            "answer": "Now, the most wonderful kamu in my life is that my mother came back to my house. My mother didn't come here for years, and I'm honored and happy that my mother could experience Pampanga with me. I haven't been with my mother for about 16 years, but now my mother is here to experience the culture, the food, and the ambiance of Pampanga. I know that this coming Christmas will be a blessing for me.",
            "word_count": 81,
            "sentence_count": 5,
            "filler_word_count": 1,
            "sentiment_score": 0.9,
            "readability_score": 75.0,
            "power_keywords": "mother, blessing, family, experience, culture, reunion",
            "duration": 42.0,
            "round": "Semifinal",
            "winner": True,
            "placement": "Winner"
        },
        {
            "id": 29,
            "year": 2024,
            "candidate_name": "Candidate from Sasmuan",
            "candidate_number": None,
            "location": "Sasmuan",
            "question": "What does women empowerment mean to you, and how do you promote it in your daily life?",
            "answer": "Women empowerment is someone who is resilient, someone who stands up for herself, someone who is content with what she has. I apply it to my daily life. This is my lesson that we should have resilience. And no matter what happens, we are facing a lot of challenges now.",
            "word_count": 55,
            "sentence_count": 4,
            "filler_word_count": 0,
            "sentiment_score": 0.75,
            "readability_score": 72.0,
            "power_keywords": "resilient, empowerment, challenges, content, stands up",
            "duration": 28.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Top 5 Finalist"
        },
        {
            "id": 30,
            "year": 2024,
            "candidate_name": "Candidate from Magalang",
            "candidate_number": None,
            "location": "Magalang",
            "question": "What Kapampangan product best represents you and why?",
            "answer": "Without further ado, I would choose Kamaru, which is a delicacy from my hometown of Magalang. Kamaru is often overlooked, and it might seem unappealing to many eyes, but if you look further and understand, you will see that it is a symbol of resilience because this shows the positivity of my town and the resilience of our community and our fellow megalots and Magalang. So, I use this as a symbol and I want people to know that these are the qualities that I embody. So I chose Kamaru as the Kapampangan product that best represents me.",
            "word_count": 100,
            "sentence_count": 4,
            "filler_word_count": 2,
            "sentiment_score": 0.8,
            "readability_score": 74.0,
            "power_keywords": "Kamaru, delicacy, resilience, symbol, community, embody",
            "duration": 50.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Semifinalist"
        },
        {
            "id": 31,
            "year": 2024,
            "candidate_name": "Candidate from Bacolor",
            "candidate_number": None,
            "location": "Bacolor",
            "question": "What is the best way to preserve our Kapampangan language and why?",
            "answer": "I think the best way to preserve our Kapampangan language is to not only use it but keep it in our minds to be proud that you are a Kapampangan. Because Kapampangan women are resilient and strong. I want to promote our Kapampangan language. Not only by using it but also by promoting it with the use of social media, we can also teach the younger generation to use it more frequently. I also use it when answering questions like this. I didn't use it because I am considering the judges, but this is the way to promote Kapampangan language. To always use it and always keep it in mind.",
            "word_count": 115,
            "sentence_count": 8,
            "filler_word_count": 3,
            "sentiment_score": 0.85,
            "readability_score": 70.0,
            "power_keywords": "language, preserve, promote, proud, social media, younger generation",
            "duration": 55.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Semifinalist"
        },
        {
            "id": 32,
            "year": 2024,
            "candidate_name": "Candidate from Mexico",
            "candidate_number": None,
            "location": "Mexico",
            "question": "In your opinion, how can women balance traditional roles and modern expectations in today's world?",
            "answer": "As we are embodied as modern Kapampangan women, we are open to growth and change, and also by connecting to our roots, by doing things that would promote our culture or cultural heritage. We are not only embracing our identity but preserving it to pass it on to the next generation.",
            "word_count": 56,
            "sentence_count": 2,
            "filler_word_count": 2,
            "sentiment_score": 0.8,
            "readability_score": 79.0,
            "power_keywords": "modern, growth, change, roots, culture, heritage, identity",
            "duration": 30.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Semifinalist"
        },
        {
            "id": 33,
            "year": 2024,
            "candidate_name": "Candidate from Guagua",
            "candidate_number": None,
            "location": "Guagua",
            "question": "Do you think the essence of being a woman has changed in modern times? If so, how?",
            "answer": "To be an empowered modern Kapampangan woman is to be a bridge between the past and the future. We honor our heritage while shaping a better tomorrow. One who carries on the legacy of resilience, excellence, and pride, remaining true to local identity while embracing modernization. One who stands for causes and actively contributes to making Pampanga a driving force for all. And that woman stands here, strong, fearless, and unstoppable. And I believe that the essence of being a woman is change.",
            "word_count": 90,
            "sentence_count": 6,
            "filler_word_count": 1,
            "sentiment_score": 0.9,
            "readability_score": 76.0,
            "power_keywords": "empowered, bridge, heritage, resilience, excellence, unstoppable",
            "duration": 45.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Top 5 Finalist"
        },
        {
            "id": 34,
            "year": 2024,
            "candidate_name": "Candidate from Santa Ana",
            "candidate_number": None,
            "location": "Santa Ana",
            "question": "What unique strengths do women bring to families and communities?",
            "answer": "Since childhood, I have been surrounded by empowered women. I would like to answer that question by incorporating this quality of my mother. Her smile symbolizes the hardships and sacrifices she has dedicated to our family. And I stand in front of you all today, ready to inspire powerless Kapampangan women and embody Pampanga wherever I go. Thanks to my mother.",
            "word_count": 66,
            "sentence_count": 4,
            "filler_word_count": 0,
            "sentiment_score": 0.85,
            "readability_score": 75.0,
            "power_keywords": "empowered, mother, hardships, sacrifices, inspire, embody",
            "duration": 35.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Semifinalist"
        },
        {
            "id": 35,
            "year": 2024,
            "candidate_name": "Candidate from Bacolor",
            "candidate_number": None,
            "location": "Bacolor",
            "question": "What role does education play in empowering women and girls in your community?",
            "answer": "An empowered modern Kapampangan is a woman who embraces both tradition and innovation. I believe that progress and true empowerment come from lifting each other up and inspiring them to believe in their own strength. Tonight, just as I believe in my own strength, for me, it's taking pride in our Kapampangan roots.",
            "word_count": 57,
            "sentence_count": 3,
            "filler_word_count": 1,
            "sentiment_score": 0.8,
            "readability_score": 82.0,
            "power_keywords": "empowered, tradition, innovation, strength, pride, roots",
            "duration": 30.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Semifinalist"
        },
        {
            "id": 36,
            "year": 2024,
            "candidate_name": "Candidate from Angeles",
            "candidate_number": None,
            "location": "Angeles",
            "question": "Who is the most inspiring Kapampangan, past or present, to you?",
            "answer": "I remember a woman from the past named Rosario Pariso. She was a commander in the past, and every time she would go to war, she would put on red lipstick, symbolizing that she has confidence and that she is a warrior who should not be underestimated. Since then, I thought, we began having a conference of being proud as Kapampangans, as women. Just like the modern generation, we have our own Arlen. Lu Sing. We have the best of Pampanga. They were all started by women passed on by our mothers. Our grandmothers who have been the best C have made us the culinary capital of the Philippines. In this very corner of this place, there are successful business owners who have built their own empires and Kapampangan beauty queens. I run my own business like them. And as a beauty queen, I want to be like them someday. No matter what field I land on, in any field, I will be successful and continue to breathe this Kapampangan spirit.",
            "word_count": 171,
            "sentence_count": 9,
            "filler_word_count": 3,
            "sentiment_score": 0.9,
            "readability_score": 68.0,
            "power_keywords": "commander, confidence, warrior, proud, business owners, empires, spirit",
            "duration": 85.0,
            "round": "Semifinal",
            "winner": False,
            "placement": "Semifinalist"
        },
        
        # Final Round Questions
        {
            "id": 37,
            "year": 2024,
            "candidate_name": "Candidate from Santo Tomas",
            "candidate_number": None,
            "location": "Santo Tomas",
            "question": "What makes a true Kapampangan champion?",
            "answer": "There are different qualities for each Kapampangan, but a true Kapampangan is when they know their mission at any time, they are ready to take responsibility, and they give their all in whatever they do in life. And I believe I am advocating for the Kapampangan women who are here standing in front of you.",
            "word_count": 59,
            "sentence_count": 2,
            "filler_word_count": 1,
            "sentiment_score": 0.8,
            "readability_score": 75.0,
            "power_keywords": "mission, responsibility, advocating, qualities",
            "duration": 31.0,
            "round": "Final",
            "winner": False,
            "placement": "Top 5 Finalist"
        },
        {
            "id": 38,
            "year": 2024,
            "candidate_name": "Candidate from San Fernando",
            "candidate_number": None,
            "location": "San Fernando",
            "question": "What makes a true Kapampangan champion?",
            "answer": "What makes a true Kapampangan champion? I highlighted the characteristics of mag-bara. Mag-bara in Kapampangan means someone who stands for change. I myself, as a rescuer, stand for animal rights, and I believe that that passion makes me unique and a champion. And we, Kapampangans, are like roses, my name and the flower. There's a big possibility of blossoming and standing up.",
            "word_count": 67,
            "sentence_count": 4,
            "filler_word_count": 0,
            "sentiment_score": 0.85,
            "readability_score": 73.0,
            "power_keywords": "mag-bara, change, passion, unique, blossoming",
            "duration": 35.0,
            "round": "Final",
            "winner": False,
            "placement": "1st Runner-Up"
        },
        {
            "id": 39,
            "year": 2024,
            "candidate_name": "Candidate from Mabalacat",
            "candidate_number": None,
            "location": "Mabalacat",
            "question": "What makes a true Kapampangan champion?",
            "answer": "A Kapampangan champion is composed of the knowledge about Pampanga and the plans to encourage people to progress. To be a Kapampangan champion, you need to know the root of being a Kapampangan, not just respect the Pampangan culture. Regardless of where you live in Pampanga, you need to know the history and what we stand for. Especially in my case, I know that my locality needs to encourage the youth more in terms of art.",
            "word_count": 79,
            "sentence_count": 4,
            "filler_word_count": 0,
            "sentiment_score": 0.8,
            "readability_score": 79.0,
            "power_keywords": "knowledge, progress, root, history, youth, art",
            "duration": 40.0,
            "round": "Final",
            "winner": True,
            "placement": "Winner"
        },
        {
            "id": 40,
            "year": 2024,
            "candidate_name": "Candidate from Guagua",
            "candidate_number": None,
            "location": "Guagua",
            "question": "What makes a true Kapampangan champion?",
            "answer": "I have within me the values, traditions, and dreams that this title represents. First, I am deeply connected to Kapampangan traditions. Next, I have a heart for service. I believe that the true spirit is embodied in actions and compassion. And ultimately, I embody the grace and resilience of Kapampangan people, becoming an empowered modern Kapampangan woman for today's generation. As a social media influencer with many followers on social media, I will use my platform to promote my culture and support their organizations. Being a Kapampangan is not just about having a beautiful face but serving the people. I am ready to take on that responsibility with pride, humility, and love.",
            "word_count": 120,
            "sentence_count": 8,
            "filler_word_count": 1,
            "sentiment_score": 0.9,
            "readability_score": 71.0,
            "power_keywords": "values, traditions, service, compassion, resilience, influencer",
            "duration": 60.0,
            "round": "Final",
            "winner": False,
            "placement": "Top 5 Finalist"
        },
        {
            "id": 41,
            "year": 2024,
            "candidate_name": "Candidate from Sasmuan",
            "candidate_number": None,
            "location": "Sasmuan",
            "question": "What makes a true Kapampangan champion?",
            "answer": "What makes a true Kapampangan champion for me is someone who is resilient, who encourages their fellowmen, and who stands up for themselves. That's it.",
            "word_count": 28,
            "sentence_count": 1,
            "filler_word_count": 0,
            "sentiment_score": 0.75,
            "readability_score": 82.0,
            "power_keywords": "resilient, encourages, stands up",
            "duration": 15.0,
            "round": "Final",
            "winner": False,
            "placement": "Top 5 Finalist"
        }
    ]
    
    # Convert to DataFrame
    return pd.DataFrame(data)

# Load the data
df = load_data()

# Sidebar filters
st.sidebar.title("Filters")

# Round filter (multi-select)
rounds = sorted(df['round'].unique())
selected_rounds = st.sidebar.multiselect("Select Rounds:", rounds, default=rounds)

# Winner only filter
winner_only = st.sidebar.checkbox("Show Winners Only")

# Word count slider
min_words = int(df['word_count'].min())
max_words = int(df['word_count'].max())
word_count_range = st.sidebar.slider(
    "Word Count Range:",
    min_value=min_words,
    max_value=max_words,
    value=(min_words, max_words)
)

# Duration slider (in seconds)
min_duration = int(df['duration'].min())
max_duration = int(df['duration'].max())
duration_range = st.sidebar.slider(
    "Answer Duration (seconds):",
    min_value=min_duration,
    max_value=max_duration,
    value=(min_duration, max_duration)
)

# Apply filters to data
filtered_df = df.copy()

if selected_rounds:
    filtered_df = filtered_df[filtered_df['round'].isin(selected_rounds)]

if winner_only:
    filtered_df = filtered_df[filtered_df['winner'] == True]

filtered_df = filtered_df[
    (filtered_df['word_count'] >= word_count_range[0]) & 
    (filtered_df['word_count'] <= word_count_range[1])
]

filtered_df = filtered_df[
    (filtered_df['duration'] >= duration_range[0]) & 
    (filtered_df['duration'] <= duration_range[1])
]

# Display filtered record count
st.sidebar.markdown(f"**Displaying:** {len(filtered_df)} records")

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Q&A Analytics", "Power Keyword Explorer", "Candidate Drilldown"])

# Tab 1: Overview
with tab1:
    st.title("Mutya ning Kapampangan 2023 Q&A Analytics")
    
    # Create metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Entries", len(filtered_df))
    
    with col2:
        winner_count = filtered_df['winner'].sum()
        st.metric("Winner Entries", f"{int(winner_count)}")
    
    with col3:
        avg_sentiment = filtered_df['sentiment_score'].mean()
        st.metric("Avg Sentiment", f"{avg_sentiment:.2f}")
    
    with col4:
        avg_word_count = filtered_df['word_count'].mean()
        st.metric("Avg Word Count", f"{int(avg_word_count)}")
    
    # Second row of metrics for duration
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_duration = filtered_df['duration'].mean()
        st.metric("Avg Duration (sec)", f"{avg_duration:.1f}")
    
    with col2:
        max_duration = filtered_df['duration'].max()
        st.metric("Max Duration (sec)", f"{max_duration:.1f}")
        
    with col3:
        min_duration = filtered_df['duration'].min()
        st.metric("Min Duration (sec)", f"{min_duration:.1f}")
        
    with col4:
        words_per_sec = filtered_df['word_count'].sum() / filtered_df['duration'].sum() if filtered_df['duration'].sum() > 0 else 0
        st.metric("Words/Second", f"{words_per_sec:.1f}")
    
    # Create two columns for charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Winners vs Non-Winners")
        
        winner_counts = filtered_df['winner'].value_counts()
        labels = ['Winners', 'Non-Winners']
        if len(winner_counts) == 1 and winner_only:
            values = [winner_counts[True], 0]
        elif len(winner_counts) == 1 and not winner_only:
            values = [0, winner_counts[False]]
        else:
            values = [winner_counts.get(True, 0), winner_counts.get(False, 0)]
        
        fig = px.pie(
            names=labels, 
            values=values,
            color_discrete_sequence=['gold', 'royalblue'],
            hole=0.4
        )
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Word Count by Round")
        
        avg_by_round = filtered_df.groupby('round')['word_count'].mean().reset_index()
        
        if not avg_by_round.empty:
            fig = px.bar(
                avg_by_round, 
                x='round', 
                y='word_count',
                labels={'word_count': 'Average Word Count', 'round': 'Round'},
                color_discrete_sequence=['royalblue']
            )
            fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data available with current filters")
    
    # Analysis of duration vs words
    st.subheader("Duration vs. Word Count")
    
    if not filtered_df.empty:
        fig = px.scatter(
            filtered_df, 
            x='duration', 
            y='word_count', 
            color='winner',
            size='sentiment_score',
            hover_name='candidate_name',
            hover_data=['placement', 'round', 'location'],
            labels={
                'duration': 'Answer Duration (seconds)',
                'word_count': 'Word Count',
                'winner': 'Winner'
            },
            color_discrete_map={True: 'gold', False: 'royalblue'}
        )
        
        # Add a trendline
        fig.update_layout(
            title='Longer answers tend to have more words, but what about speaking rate?',
            margin=dict(t=50, b=0, l=0, r=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available with current filters")
    
    # Table of Rounds and Questions
    st.subheader("Questions by Round")
    
    # Group by round and question
    question_counts = filtered_df.groupby(['round', 'question']).size().reset_index(name='count')
    
    if not question_counts.empty:
        st.dataframe(question_counts, use_container_width=True)
    else:
        st.info("No data available with current filters")

# Tab 2: Q&A Analytics
with tab2:
    st.title("Q&A Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sentiment Score Distribution")
        
        if not filtered_df.empty:
            fig = px.histogram(
                filtered_df, 
                x="sentiment_score", 
                color="winner",
                marginal="box",
                nbins=20,
                labels={'sentiment_score': 'Sentiment Score', 'count': 'Frequency'},
                color_discrete_map={True: 'gold', False: 'royalblue'}
            )
            fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data available with current filters")
    
    with col2:
        st.subheader("Answer Duration Distribution")
        
        if not filtered_df.empty:
            fig = px.histogram(
                filtered_df, 
                x="duration", 
                color="winner",
                marginal="box",
                nbins=20,
                labels={'duration': 'Answer Duration (seconds)', 'count': 'Frequency'},
                color_discrete_map={True: 'gold', False: 'royalblue'}
            )
            fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No data available with current filters")
    
    st.subheader("Speaking Rate (Words per Second)")
    
    if not filtered_df.empty:
        # Calculate words per second
        filtered_df['words_per_second'] = filtered_df['word_count'] / filtered_df['duration']
        
        fig = px.box(
            filtered_df, 
            x="winner", 
            y="words_per_second",
            color="winner",
            points="all",
            labels={
                'words_per_second': 'Words per Second', 
                'winner': 'Winner Status'
            },
            color_discrete_map={True: 'gold', False: 'royalblue'}
        )
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available with current filters")
    
    st.subheader("Filler Words vs Readability")
    
    if not filtered_df.empty:
        fig = px.scatter(
            filtered_df,
            x="filler_word_count",
            y="readability_score",
            color="winner",
            size="word_count",
            hover_name="candidate_name",
            hover_data=["placement", "round"],
            labels={
                'filler_word_count': 'Number of Filler Words',
                'readability_score': 'Readability Score',
                'winner': 'Winner'
            },
            color_discrete_map={True: 'gold', False: 'royalblue'}
        )
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available with current filters")
    
    st.subheader("Top Answers by Duration")
    
    # Display top answers by duration
    longest_duration = filtered_df.sort_values('duration', ascending=False).head(5)
    
    if not longest_duration.empty:
        columns_to_display = ['candidate_name', 'location', 'round', 'duration', 'word_count', 'words_per_second', 'sentiment_score', 'winner']
        st.dataframe(longest_duration[columns_to_display], use_container_width=True)
    else:
        st.info("No data available with current filters")

# Tab 3: Power Keyword Explorer
with tab3:
    st.title("Power Keyword Explorer")
    
    # Create keyword search feature
    keyword_search = st.text_input("Search for keyword in power keywords:")
    
    if keyword_search:
        # Filter dataframe for rows containing the keyword
        keyword_results = filtered_df[filtered_df['power_keywords'].str.contains(keyword_search, case=False, na=False)]
        
        st.write(f"Found **{len(keyword_results)}** entries containing '{keyword_search}'")
        
        if not keyword_results.empty:
            columns_to_display = ['candidate_name', 'location', 'round', 'power_keywords', 'sentiment_score', 'winner']
            st.dataframe(keyword_results[columns_to_display], use_container_width=True)
        else:
            st.info("No matches found with current filters")
    
    st.subheader("Power Keywords Word Cloud")
    
    if not filtered_df.empty:
        # Combine all power keywords into a single text
        all_keywords = " ".join(filtered_df['power_keywords'].str.replace(",", " "))
        
        if all_keywords.strip():
            # Create a word cloud
            wordcloud = WordCloud(
                width=800,
                height=400,
                background_color='white',
                colormap='viridis',
                max_words=100
            ).generate(all_keywords)
            
            # Display the word cloud
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            
            # Convert to image and display
            st.image(wordcloud.to_array(), use_column_width=True)
        else:
            st.info("No power keywords available with current filters")
    else:
        st.info("No data available with current filters")
    
    # Show most common power keywords
    if not filtered_df.empty:
        st.subheader("Most Common Power Keywords")
        
        # Parse all keywords into individual words
        all_keywords_list = []
        for keywords in filtered_df['power_keywords']:
            all_keywords_list.extend([k.strip() for k in keywords.split(",")])
        
        # Count frequency of each keyword
        keyword_counts = pd.Series(all_keywords_list).value_counts().reset_index()
        keyword_counts.columns = ['Keyword', 'Frequency']
        
        # Display top 10 keywords with bar chart
        top_keywords = keyword_counts.head(10)
        
        fig = px.bar(
            top_keywords, 
            x='Frequency', 
            y='Keyword',
            orientation='h',
            labels={'Frequency': 'Number of Occurrences', 'Keyword': 'Power Keyword'},
            color='Frequency',
            color_continuous_scale='Viridis'
        )
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No data available with current filters")
        
    # Keyword co-occurrence analysis
    st.subheader("Keyword Themes")
    
    # Group keywords into themes
    st.markdown("""
    Based on our analysis, we identified several major keyword themes in the contestants' answers:
    
    1. **Cultural Pride** - Keywords: culinary traditions, culture, heritage, identity, pride, legacy
    2. **Community Values** - Keywords: love, family, community, collective efforts, fellowmen
    3. **Self-Development** - Keywords: purpose, passion, progressing, natural, meaningful
    4. **Advocacy & Voice** - Keywords: awareness, mental health, voice, cause, advocacy
    5. **Local Festivals** - Keywords: Vuro, Sagita Festival, Pasku, balangays, parol
    
    The winning contestant (Salma Emma) used keywords spanning multiple themes, particularly emphasizing 
    Cultural Pride, Community Values, and Self-Development.
    """)

# Tab 4: Candidate Drilldown
with tab4:
    st.title("Candidate Drilldown")
    
    # Get unique candidates
    candidates = sorted(df['candidate_name'].unique())
    
    if not candidates:
        st.info("No candidates available with current filters")
    else:
        selected_candidate = st.selectbox("Select a Candidate:", candidates)
        
        # Filter data for selected candidate
        candidate_data = df[df['candidate_name'] == selected_candidate]
        
        if not candidate_data.empty:
            # Check if candidate is a winner in any round
            is_winner = candidate_data['winner'].any()
            
            # Create header with winner badge if applicable
            col1, col2 = st.columns([4, 1])
            with col1:
                st.subheader(f"{selected_candidate} - {candidate_data['location'].iloc[0]}")
            with col2:
                if is_winner:
                    st.markdown("🏆 **WINNER**")
                elif candidate_data['placement'].iloc[0] == "1st Runner-Up":
                    st.markdown("🥈 **1st RUNNER-UP**")
                elif "Finalist" in candidate_data['placement'].iloc[0]:
                    st.markdown("⭐ **FINALIST**")
            
            # Display metrics for this candidate
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                avg_words = candidate_data['word_count'].mean()
                st.metric("Avg Word Count", f"{int(avg_words)}")
            
            with col2:
                avg_sentiment = candidate_data['sentiment_score'].mean()
                st.metric("Avg Sentiment", f"{avg_sentiment:.2f}")
            
            with col3:
                avg_duration = candidate_data['duration'].mean()
                st.metric("Avg Duration (sec)", f"{avg_duration:.1f}")
            
            with col4:
                avg_words_per_sec = candidate_data['word_count'].sum() / candidate_data['duration'].sum()
                st.metric("Words/Second", f"{avg_words_per_sec:.1f}")
            
            # Display candidate's rounds
            rounds_competed = sorted(candidate_data['round'].unique())
            st.write(f"**Rounds:** {', '.join(map(str, rounds_competed))}")
            
            # Display all power keywords used by this candidate
            all_keywords = set()
            for keywords in candidate_data['power_keywords']:
                all_keywords.update([k.strip() for k in keywords.split(",")])
            
            st.write(f"**Power Keywords:** {', '.join(sorted(all_keywords))}")
            
            # Speed comparison to average
            all_candidates_avg = df['word_count'].sum() / df['duration'].sum()
            percent_diff = ((avg_words_per_sec - all_candidates_avg) / all_candidates_avg) * 100
            
            if percent_diff > 0:
                st.write(f"**Speaking Rate:** {abs(percent_diff):.1f}% faster than average")
            else:
                st.write(f"**Speaking Rate:** {abs(percent_diff):.1f}% slower than average")
            
            # Display Q&A details
            st.subheader("Q&A Details")
            
            for index, row in candidate_data.sort_values(['round', 'id']).iterrows():
                with st.expander(f"{row['round']} Round - {row['question'][:60]}..."):
                    # Show winner badge if applicable
                    if row['winner']:
                        st.markdown("🏆 **WINNER THIS ROUND**")
                    
                    st.write("**Question:**")
                    st.write(row['question'])
                    
                    st.write("**Answer:**")
                    st.write(row['answer'])
                    
                    # Show metrics for this specific answer
                    cols = st.columns(5)
                    cols[0].metric("Word Count", row['word_count'])
                    cols[1].metric("Sentence Count", row['sentence_count'])
                    cols[2].metric("Duration (sec)", f"{row['duration']:.1f}")
                    cols[3].metric("Words/Second", f"{row['word_count']/row['duration']:.1f}")
                    cols[4].metric("Sentiment", f"{row['sentiment_score']:.2f}")
                    
                    # Show power keywords for this answer
                    st.write("**Power Keywords:**", row['power_keywords'])
            
            # Compare this candidate to the winner
            if not is_winner:  # Only show comparison if this candidate is not the winner
                st.subheader("Comparison to Winner")
                
                # Get winner data
                winner_data = df[df['winner'] == True]
                
                if not winner_data.empty:
                    # Prepare comparison data
                    comparison_data = pd.DataFrame({
                        'Metric': ['Avg Word Count', 'Avg Sentiment', 'Avg Duration', 'Words per Second', 'Filler Word Count'],
                        'Candidate': [
                            candidate_data['word_count'].mean(),
                            candidate_data['sentiment_score'].mean(),
                            candidate_data['duration'].mean(),
                            candidate_data['word_count'].sum() / candidate_data['duration'].sum(),
                            candidate_data['filler_word_count'].mean()
                        ],
                        'Winner': [
                            winner_data['word_count'].mean(),
                            winner_data['sentiment_score'].mean(),
                            winner_data['duration'].mean(),
                            winner_data['word_count'].sum() / winner_data['duration'].sum(),
                            winner_data['filler_word_count'].mean()
                        ]
                    })
                    
                    # Create a comparison chart
                    fig = go.Figure()
                    
                    fig.add_trace(go.Bar(
                        x=comparison_data['Metric'],
                        y=comparison_data['Candidate'],
                        name=selected_candidate,
                        marker_color='royalblue'
                    ))
                    
                    fig.add_trace(go.Bar(
                        x=comparison_data['Metric'],
                        y=comparison_data['Winner'],
                        name=winner_data['candidate_name'].iloc[0],
                        marker_color='gold'
                    ))
                    
                    fig.update_layout(
                        title="Candidate vs. Winner Comparison",
                        xaxis_title="Metric",
                        yaxis_title="Value",
                        barmode='group',
                        margin=dict(t=50, b=0, l=0, r=0)
                    )
                    
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Provide insights
                    insights = []
                    
                    # Word count comparison
                    if candidate_data['word_count'].mean() > winner_data['word_count'].mean():
                        insights.append(f"- {selected_candidate} used **more words** on average than the winner")
                    else:
                        insights.append(f"- {selected_candidate} used **fewer words** on average than the winner")
                    
                    # Sentiment comparison
                    if candidate_data['sentiment_score'].mean() > winner_data['sentiment_score'].mean():
                        insights.append(f"- {selected_candidate} expressed **more positive sentiment** than the winner")
                    else:
                        insights.append(f"- {selected_candidate} expressed **less positive sentiment** than the winner")
                    
                    # Speaking rate comparison
                    candidate_rate = candidate_data['word_count'].sum() / candidate_data['duration'].sum()
                    winner_rate = winner_data['word_count'].sum() / winner_data['duration'].sum()
                    
                    if candidate_rate > winner_rate:
                        insights.append(f"- {selected_candidate} spoke **faster** than the winner ({candidate_rate:.1f} vs {winner_rate:.1f} words/sec)")
                    else:
                        insights.append(f"- {selected_candidate} spoke **slower** than the winner ({candidate_rate:.1f} vs {winner_rate:.1f} words/sec)")
                    
                    st.markdown("### Key Insights")
                    for insight in insights:
                        st.markdown(insight)
        
        else:
            st.info("No data available for selected candidate with current filters")

# Add footer
st.markdown("---")
st.markdown("Mutya ning Kapampangan 2023 Q&A Analytics Dashboard | Created with Streamlit")