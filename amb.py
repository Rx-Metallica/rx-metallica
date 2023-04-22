import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Anti-Caste',page_icon='🇪🇺',layout='wide')

selected = option_menu(
	menu_title=None,
	options=["Casteism","DHM","Atrocities","Ambedkarism","Journalism","Education","Leaders"],
	icons = ["back","bookmarks","bar-chart","bricks","broadcast-pin","book","brush-fill"],
	menu_icon="cast",
	default_index=0,
	#orientation = "horizontal",
	styles={ "container": {"padding": "0!important", "background-color": "#000000"}, "icon": {"color": "white", "font-size": "15px"}, "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"}, "nav-link-selected": {"background-color": "#191970"}, }
)
if selected == "Casteism":
	st.subheader("CASTE?")
	st.image("Indian_Caste_System.jpg")
	st.write("👉 In simpler terms, caste is where society is divided up into different groups, with those who have more power at the top and those who have little or no power at the bottom. You inherit your caste and it cannot be changed. Even worse are those deemed so inferior as to be out of the system altogether – previously known as outcasts or untouchables.")
	st.write("__________________________________")
	st.subheader("WHERE DO WE SEE CASTE AND HOW IT AFFECTS CITIZENS?")
	st.write("👫 Marriages: Most Indian marriages are arranged by parents. Several factors were considered by them for finding the ideal spouse. Out of which, one’s caste is a significant factor. People do not want their son or their daughter to marry a person from another caste. Just like the word “untouchables” suggests, a Brahmin would never marry a person from an SC or ST caste.")
	st.write("✒ Education: Public universities have caste-based reservations for students coming from underprivileged backgrounds. A person from this background can secure a seat in a top tier college with par or below par academic scores based on reservation. However, impoverished Brahmans are disadvantaged with this reservation system. For example, a Brahman has to score 100% on certain exams to get into a top tier university. While the lower caste applicant can even bypass the exam for getting a seat in the university.")
	st.write("⌨  Jobs: A significant amount of public sector jobs are allocated based on caste reservation. Impoverished communities from Brahman backgrounds get affected significantly because of this reservation.")
	st.write("__________________________________")

	st.subheader("WHAT IS RESERVATION?")
	st.write("🧾 Reservation is a system of affirmative action in India that provides historically disadvantaged groups representation in education, employment, government schemes, scholarships and politics. Based on provisions in the Indian Constitution, it allows the Union Government and the States and Territories of India to set reserved quotas or seats, at particular percentage in Education Admissions, Employments, Political Bodies, Promotions, etc, for socially and educationally backward citizens.")

	st.write("___________________________________")	

	st.subheader("THE DIFFERENCE BETWEEN RACE AND CASTE")
	st.write("There is a significant difference between race and caste: two people can come from the same village (as have their families for generations), be of the same race, skin colour and religion, and yet be treated in very different ways. Similarly, it cannot be categorised as a class system: you can change your class and it is now largely determined by education, wealth and upbringing. You are born into a caste, the same as all of your ancestors, and it cannot be changed regardless of how intelligent you are, how wealthy you become or who you marry.")

if selected == "DHM":
	st.image("20230419_153408.jpg")
	st.subheader("WHY DALIT HISTORY MONTH?")
	st.write("In India, caste is a power structure that enables suppression and exploitation and hinders equality, social justice and humanitarianism to flourish.")
	st.write("__________________________________")
	st.write("Dalit History Month provides an opportunity to discuss in public spaces the everyday violence that we as Dalits face and resist, the history that seems to have been erased and the representation in society, politics and business that reamins to be attained.")
	st.write("__________________________________")
	st.write("It is important for us to think what we're doing each day to create a society without casteism - we must all develop habits that actively work against this structure in order to weaken its hold an organistanional and wider societal culture. ")

if selected == "Ambedkarism":
	st.image("Screenshot_20230419-154639_Instagram.jpg")
	st.write("All are slaves of the caste sytem. But all the slaves are not equal in status -Dr. B R Ambedkar💙")
	st.divider()
	st.write("Dr. Bhimrao Ramji Ambedkar is often thought of as a jurist, economist, and social reformer. It is certainly hard to find many figures who can be said to have had a comparable influence in modern Indian history. However, above all, Ambedkar was an arch-critic of the Hindu caste system and a leader in the fight for Dalit liberation. Modern India cannot be understood without an appreciation of Ambedkar’s life and work.")
	st.write("__________________________________")
	st.subheader("AMBEDKAR'S VISION OF DEMOCRACY: WHY ITS REVIVAL IS IMPORTANT FOR INDIA?")
	st.write("Ambedkar's vision of democracy needs to be rediscovered to fight hatred, violence, sectarianism and fundamentalism, to use it as a shield against casteist and religious fanaticism. To realise democracy not in its narrow sense, not only by counting votes while conducting elections but as Babasaheb in his vision explains it: “Democracy is not merely a form of Government. It is primarily a mode of associated living, of conjoint communicated experience. It is essentially an attitude of respect and reverence towards our fellow men.” ")

if selected == "Atrocities":
	st.image("88007_GettyImages517064586_1600179439999.jpg")
	st.write("__________________________________")
	st.subheader("Atrocities/Crime against Scheduled Castes have increased by 1.2% in 2021 (50900) over 2020 (50,291 cases).")
	st.subheader("Atrocities/Crime against Scheduled Tribes have increased by 6.4% in 2021 (8,802 cases) over 2020 (8,272 cases).")

	st.write("___________________________________")
	st.subheader("WHY CASTE MATTERS?")
	st.write("Those who are in the lowest castes (or even outside the caste system) often suffer from caste-based discrimination. They are seen as ‘impure’ or ‘polluting’ and are often shunned by people who are from so-called ‘higher’ castes. They have difficulty getting access to land, resources and education, are victims of verbal, physical and sexual abuse, are given the most demeaning jobs and are at high risk of ending up in bonded labour.")
	st.write("___________________________________")
	st.write("In spite of living in the 21st century, Caste Discrimination is still practiced by people throughout India. India has a society based on a hierarchical caste system, not only among Hindus but also among other castes. Previously, people in the lower classes did not have access to all resources and were also abused by the higher classes. Untouchables were considered very impure, so when a caste member comes into contact with them, that member becomes impure.")


if selected == "Journalism":
	st.image("Ambedkar-Mooknayak-1-1050x400.jpg")
	st.subheader("AMBEDKAR'S JOURNALISM AND ITS SIGNIFICANCE TODAY")
	st.write("___________________________________")
	st.write("Thus, Dr Ambedkar’s seeks to lay down some standards for Indian newspapers. They are:")
	st.write("1) Journalism should be fair and unbiased. In the Indian context, it also means being free from casteist biases and prejudices.")
	st.write("2) Journalism should be based on facts rather than on pre-conceived notions.")
	st.write("3) Journalism should be a mission, not a trade or business.")
	st.write("4) Journalism and journalists should have their own moral standards.")
	st.write("5) Fearlessness is an essential characteristic of journalism and journalists.")
	st.write("6) Advocacy in social interest is a prime duty of journalism and journalists.")
	st.write("7) There should be no place for hero worship in journalism.")
	st.write("8) Objectivity, not sensationalism, should be the ideal of newspapers.")
	st.write("9) Instead of whipping up passions, the journalists should strive to evoke the reason of society.")

	st.write("___________________________________")
	st.image("Screenshot_20230421-182959_Instagram.jpg")

	st.write("___________________________________")
	st.write("It is clear that until every section of society does not get due representation in the media, the one-sided, solicitous and unbalanced dissemination of information will continue. It was to counter this imbalance that Ambedkar wanted Dalits to have their own media outlets. He believed that only Dalit journalism could battle injustice faced by Dalits  ")
	st.write("___________________________________")
	st.write("Dr B. R. Ambedkar was convinced that if Dalits were to be awakened and empowered, they needed to have publications of their own. It was with this objective in mind that he began publishing Marathi fortnightly Mooknayak on 31 January 1920. “Mooknayak” means the hero of the voiceless. Explaining the logic behind its publication, Ambedkar wrote in the editorial of Mooknayak’s inaugural issue, “There is no better source than the newspaper to suggest the remedy against the injustice that is being done to our people in the present and will be done in the future, and also to discuss the ways and means for our progress in the future.” In the same editorial, he wrote, “The Hindu society is just like a tower which has several stories without a ladder or entrance. The man who is born in the lower storey cannot enter the upper story however worthy he may be and the man who is born in the upper storey cannot be driven out into the lower storey however unworthy he may be … The alienation produced by the absence of inter-dining and inter-caste marriages has fostered the feelings of touchables and untouchables so much that these touchable and untouchable castes, though a part of Hindu society, are in reality living in worlds apart.”")


if selected == "Education":
	st.image("thequint_2017-01_c7ac5815-efda-4989-b3b5-ae58228f87c3_rohitvemula.jpg")
	st.header("Educate Agitate Organize 🖋")
	st.write("__________________________________")
	st.write("Ambedkar believed that education is the birthright of every person and nobody can be denied to attain this right. Thus, all democracies of the world should provide the right to education to all the members of the nation irrespective of caste, creed, sex or any other basis.")
	st.divider()
	st.write("Dr Ambedkar said, “Education is what makes a person fearless, teaches him the lesson of unity, makes him aware of his rights and inspires him to struggle for his rights.” He believed that education is a movement. If it does not fulfil its objectives, it is useless. Dr Ambedkar unambiguously stated that an education that does not make a person capable, that does not teach him equality and morality, is not true education. True education cradles humanity, generates sources of livelihood, imparts wisdom and imbues us with egalitarianism. True education makes society alive.")

if selected == "Leaders":
	st.image("Mahatma_Jotirao_Phule.jpg")
	st.divider()
	st.write("👳 Jyotirao Govindrao Phule (11 April 1827 – 28 November 1890) was an Indian social activist, businessman, anti-caste social reformer and writer from Maharashtra.His work extended to many fields, including eradication of untouchability and the caste system and for his efforts in educating women and oppressed caste people.He and his wife, Savitribai Phule, were pioneers of women's education in India.Phule started his first school for girls in 1848 in Pune at Tatyasaheb Bhide's residence or Bhidewada.He, along with his followers, formed the Satyashodhak Samaj (Society of Truth Seekers) to attain equal rights for people from lower castes. People from all religions and castes could become a part of this association which worked for the upliftment of the oppressed classes. Phule is regarded as an important figure in the social reform movement in Maharashtra.")
	st.divider()
	st.image("Savitribai_Phule_1998_stamp_of_India.jpg")
	st.divider()
	st.write("👩‍🎓 Savitribai Phule was a teacher, Indian social reformer, educationalist, and poet from Maharashtra. Along with her husband, Jyotiba Phule in Maharashtra, she played a vital role in improving women's rights in India. She is considered to be the pioneer of India's feminist movement. Savitribai and Jyotiba together founded one of the early modern Indian girls' school in Pune, at Bhidewada in 1848. She strived to abolish discrimination and unfair treatment of people on the basis of caste and gender.")
	st.write("💬 Farming Is Divine They who toil in the fields are the outcasts They produce the food on which feast the upper castes…")
	st.divider()
	st.write("Special thanks to Dr. B R Ambedkar, Jyotiba Phule and Savitribai Phule for their special contribution towards education in the caste-based society.")
	st.write("JAI BHIM , HAIL BHIM 💙")

hide_streamlit_style = """ <style> #MainMenu {visibility: hidden;} footer {visibility: hidden;} </style> """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
