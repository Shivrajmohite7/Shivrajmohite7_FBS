import re

# data="""

# Vishnu (/ˈvɪʃnuː/; Sanskrit: विष्णु, lit. 'All Pervasive', IAST: Viṣṇu, pronounced [ʋɪʂɳʊ]), also known as Narayana and Hari, is one of the principal deities of Hinduism. He is the Supreme Being within Vaishnavism, one of the major traditions within contemporary Hinduism, and the god of preservation (sattva).[10][11] Though not prominently represented in the Vedas,[12][13][14][a] Vishnu was possibly already a significant non-elite divine figure in early Vedic times.[15][16][17] Vishnu rose to prominence in post-Vedic times, and was identified with various local traditions and deities, particularly the Bhāgavata-deities[18] Vāsudeva-Krishna and Gopala-Krishna and the Pāñcarātra-deity[18] Narayana,[19][20][21][22] in the last centuries BCE and the early centuries CE.[23]

# Vishnu is known as The Preserver within the Trimurti, the triple deity of supreme divinity that includes Brahma and Shiva.[24][25] In Vaishnavism, Vishnu is the supreme Lord who creates, protects, and transforms the universe. Tridevi is stated to be the energy and creative power (Shakti) of each, with Lakshmi being the equal complementary partner of Vishnu.[26] He is one of the five equivalent deities in Panchayatana puja of the Smarta tradition of Hinduism.[25]

# According to Vaishnavism, the supreme being is with qualities (Saguna), and has definite form, but is limitless, transcendent and unchanging absolute Brahman, and the primal Atman (Self) of the universe.[27] There are both benevolent and fearsome depictions of Vishnu. In benevolent aspects, he is depicted as an omniscient being sleeping on the coils of the serpent Shesha (who represents time) floating in the primeval ocean of milk called Kshira Sagara with his consort, Lakshmi.[28]

# Whenever the world is threatened with evil, chaos, and destructive forces, Vishnu descends in the form of an avatar (incarnation) to restore the cosmic order and protect dharma. The Dashavatara are the ten primary avatars of Vishnu. Of these ten, Rama and Krishna are the most worshipped, with temples across India and beyond.[29]

# Etymology
# Vishnu (also spelled Viṣṇu, Sanskrit: विष्णु) means 'all pervasive'[30] and, according to Medhātith (c. 1000 CE), 'one who is everything and inside everything'.[31] Vedanga scholar Yaska (4th century BCE) in the Nirukta defines Vishnu as viṣṇur viṣvater vā vyaśnoter vā ('one who enters everywhere'); also adding atha yad viṣito bhavati tad viṣnurbhavati ('that which is free from fetters and bondage is Vishnu').[32]

# In the tenth part of the Padma Purana (4–15th century CE), Danta (Son of Bhīma and King of Vidarbha) lists 108 names of Vishnu (17.98–102).[33] These include the ten primary avatars (see Dashavatara, below) and descriptions of the qualities, attributes, or aspects of God.

# The Garuda Purana (chapter XV)[34] and the "Anushasana Parva" of the Mahabharata both list over 1000 names for Vishnu, each name describing a quality, attribute, or aspect of God. Known as the Vishnu Sahasranama, Vishnu here is defined as 'the omnipresent'.[citation needed]

# Origins and development
# Origins
# Vishnu is a Rigvedic solar deity, but does not figure prominently in the RigVeda compared to Indra, Agni and others.[12][a] Just 5 out of 1028 hymns of the Rigveda are dedicated to Vishnu, although he is mentioned in other hymns,[31][14] though this does not necessarily mean he was unimportant.[17][16] Klostermaier notes that the Rig Veda does not represent all of the religion of the Vedic people,[17] and according to Gonda "Visnu must already have been a more important divine figure than it would appear from his comparatively infrequent appearances in the texts,"[16] with possible a greater prominence among the Aryan and non-Aryan masses of the early Vedic times.[15] Vishnu is mentioned in the Brahmana layer of text in the Vedas, when he rose to prominence mid-first millennium BCE.[35][14] His profile rises further as he was syncretised, in the process of Sanskritization,[36] with various local traditions and deities (Vasudeva-Krishna, Narayana, Krishna-Golpa)[19][20][37][22] in the last centuries BCE and the early centuries CE,[23] and over the history of Indian scriptures, states Jan Gonda, Vishnu becomes a divinity of the highest rank, one equivalent to the Supreme Being.[38][39]

# Avatars
# Main articles: Avatar and Dashavatara
# The various deities were amalgated into Vaishnavism as avatars or incarnations of Vishnu, who is the preserver or sustainer aspect of God within the Hindu Trimurti, and descends as an avatar to empower the good and to destroy evil, thereby restoring Dharma and relieving the burden of the Earth. An oft-quoted passage from the Bhagavad Gita describes the typical role of an avatar of Vishnu:[citation needed]

# Whenever righteousness wanes and unrighteousness increases I send myself forth.
# For the protection of the good and for the destruction of evil,
# and for the establishment of righteousness,
# I come into being age after age.

# — Bhagavad Gita 4.7–8
# Vedic literature, in particular the Puranas (ancient; similar to encyclopedias) and Itihasa (chronicle, history, legend), narrate numerous avatars of Vishnu. The most well-known of these avatars are Krishna (most notably in the Vishnu Purana, Bhagavata Purana, and Mahabharata; the latter encompassing the Bhagavad Gita), and Rama (most notably in the Ramayana). Krishna in particular is venerated in Vaishnavism as the ultimate, primeval, transcendental source of all existence, including all the other demigods and gods, such as Vishnu.[citation needed]

# The Mahabharata
# In the Mahabharata, Vishnu (as Narayana) states to Narada that He will appear in the following ten incarnations:

# Appearing in the forms of a swan [Hamsa], a tortoise [Kurma], a fish [Matsya], O foremost of regenerate ones, I shall then display myself as a boar [Varaha], then as a Man-lion (Nrisingha), then as a dwarf [Vamana], then as Rama of Bhrigu's race, then as Rama, the son of Dasaratha, then as Krishna the scion of the Sattwata race, and lastly as Kalki.

# — Book 12, Santi Parva, Chapter CCCXL (340), translated by Kisari Mohan Ganguli, 1883–1896[40]
# The Puranas
# Specified avatars of Vishnu are listed against some of the Puranas in the table below. However, this is a complicated process, and the lists are unlikely to be exhaustive because:

# Not all Puranas provide lists per se (e.g. the Agni Purana dedicates entire chapters to avatars, and some of these chapters mention other avatars within them)
# A list may be given in one place but additional avatars may be mentioned elsewhere (e.g. the Bhagavata Purana lists 22 avatars in Canto 1, but mentions others elsewhere)
# Manava Purana, the only Upa Purana lists 42 avatars of Vishnu.
# A personality in one Purana may be considered an avatar in another (e.g. Narada is not specified as an avatar in the Matsya Purana but is in the Bhagavata Purana)
# Some avatars consist of two or more people considered as different aspects of a single incarnation (e.g. Nara-Narayana, Rama and his three brothers)
# """

# v="Vishnu"
# d=re.findall(v,data)
# print(d)



text = "Hello5 Ram123! Python is easy. is learning Python 1234 @202690 ka."
# print(re.findall(r'\w',text))
# print(re.findall(r'\W',text))
# print(re.findall(r"\d",text))
# print(re.findall(r'\D',text))
# print(re.findall(r'\s',text))
# print(re.findall(r'\S',text))
# print(re.findall(r'R?',text))
# print(re.findall(r'crowi?s','crow crows crowis crowis crowis crowis ram'))
# print(re.findall(r'\w{3}',text))
# print(re.findall(r'Python|easy',text))
# x=re.search(r'\d',text)
# if x:
#     print(x.group())

# x=re.match(r'Hell',text)
# if x:
#     print(x.group())
# text = "Hello5 Ram123! Python is easy. is learning Python 1234 @202690 ka."

# x=re.fullmatch(r"\d+\w+\W",text)
# if x:
#     print(x.group())

import re

# text = "Hello5 Ram123! Python is easy. is learning Python 1234 @202690 ka."

# x = re.fullmatch(r'.*', text)
# if x:
#     print(x.group())
# text="4Ram is where 94 and 15"
# x=re.split(r'\d',text)
# if x:
#     print(x)

# text="ram is mine forever 123 "
# # x=re.subn(r'\d',"*",text)
# # if x:
# #     print(x)
# x=re.finditer(r'\w|\W',text)
# for i in x:
#     print(i.group())


email=input("enter email:")
pattern = r'^[\w]+[\d]+@[a-zA-Z]+\.[a-zA-Z]+'

if re.fullmatch(pattern,email):
    print("valid")
else:
    print("not valid")

# Python "C:/Users/TUTION/Desktop/FBS/CORE PYTHON/DEMOS/REGEX/regex2.py"