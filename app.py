import streamlit as st
import datetime

# 1. Беттің негізгі баптаулары
st.set_page_config(
    page_title="ҰстазМентор 7 сынып | Duolingo Edition",
    page_icon="🦉",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. FULL UI REDESIGN: DUOLINGO + CANVA PREMIUM CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');

    /* Негізгі фон мен қауіпсіз пастельді палитра */
    html, body, [data-testid="stAppViewContainer"] {
        background: #f7f9fc !important;
        font-family: 'Nunito', sans-serif !important;
        color: #3c4257 !important;
    }

    [data-testid="stHeader"], [data-testid="stSidebar"] {
        display: none !important;
    }

    /* SaaS Dashboard & Duolingo Hero Section */
    .hero-banner {
        background: linear-gradient(135deg, #58cc02 0%, #1cb0f6 100%);
        border-radius: 28px;
        padding: 40px;
        text-align: center;
        color: white;
        box-shadow: 0 10px 0 #3b9c00, 0 20px 30px rgba(88, 204, 2, 0.25);
        margin-bottom: 30px;
        border: 4px solid #ffffff;
    }
    .hero-banner h1 {
        font-size: 2.8rem;
        font-weight: 900;
        margin-bottom: 10px;
        text-shadow: 0 3px 0 rgba(0,0,0,0.15);
    }
    .hero-banner p {
        font-size: 1.2rem;
        font-weight: 700;
        opacity: 0.95;
    }

    /* Ойын карточкалары мен контейнерлер */
    .game-card {
        background: #ffffff;
        border: 3px solid #e5e7eb;
        border-radius: 24px;
        padding: 25px;
        box-shadow: 0 8px 0 #e5e7eb;
        margin-bottom: 20px;
        transition: all 0.2s ease;
    }
    .game-card:hover {
        border-color: #1cb0f6;
        transform: translateY(-2px);
    }

    /* 3D Тактильді батырмалар */
    .stButton > button {
        background-color: #58cc02 !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        font-size: 1.15rem !important;
        border: none !important;
        border-radius: 18px !important;
        padding: 0.85rem 2rem !important;
        box-shadow: 0 6px 0 #46a302 !important;
        transition: all 0.1s ease !important;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .stButton > button:hover {
        background-color: #61d803 !important;
        transform: translateY(-2px);
    }
    .stButton > button:active {
        transform: translateY(4px) !important;
        box-shadow: 0 2px 0 #46a302 !important;
    }

    /* Сілтеме батырмалары */
    .stLinkButton > a {
        background-color: #1cb0f6 !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        border-radius: 18px !important;
        padding: 0.85rem 2rem !important;
        box-shadow: 0 6px 0 #1899d6 !important;
        text-align: center;
        text-decoration: none;
        display: block;
        transition: all 0.1s ease !important;
    }
    .stLinkButton > a:hover {
        background-color: #22c55e !important;
        box-shadow: 0 6px 0 #16a34a !important;
    }

    /* Енгізу өрістері мен selectbox */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > div,
    .stNumberInput > div > div > input {
        background: #f7f9fc !important;
        border: 3px solid #e5e7eb !important;
        border-radius: 16px !important;
        color: #3c4257 !important;
        font-weight: 700 !important;
        padding: 12px 18px !important;
    }
    .stTextInput > div > div > input:focus {
        border-color: #1cb0f6 !important;
    }

    /* Expander және кестелерді заманауиландыру */
    div.stExpander {
        background: #ffffff !important;
        border: 3px solid #e5e7eb !important;
        border-radius: 20px !important;
        box-shadow: 0 6px 0 #e5e7eb !important;
    }
</style>
""", unsafe_allow_html=True)

# Сессияда сыныптар мен нәтижелерді сақтау
if 'classes_list' not in st.session_state:
    st.session_state.classes_list = ["7 «А»", "7 «Ә»"]

if 'results_db' not in st.session_state:
    st.session_state.results_db = {}

# 3. HERO SECTION (Басты жоғарғы блок)
st.markdown("""
    <div class="hero-banner">
        <h1>🦉 ҰстазМентор 7 сынып</h1>
        <p>🚀 Информатиканы ойын түрінде меңгер! Бір тақырып — бір өмірлік жағдаят — нақты нәтиже!</p>
    </div>
""", unsafe_allow_html=True)

# 4. CUSTOM NAVIGATION PANEL (Интерфейстің негізгі панелі)
nav_col1, nav_col2 = st.columns(2)
with nav_col1:
    mode = st.radio("🎯 Платформа режимін таңдаңыз:", ["👨‍🎓 Оқушы режимі (Game Hub)", "👩‍🏫 Мұғалім кабинеті (SaaS Dashboard)"], horizontal=True)

# 13 ресми тақырып тізімі
topics_list = [
    "1. Жеке қауіпсіздік және ондағы сервистік программалардың рөлі (Сәйкестендіру)",
    "2. Жеке қауіпсіздік және ондағы сервистік программалардың рөлі (Тест)",
    "3. Ақпараттың өлшем бірліктері",
    "4. Ақпараттың өлшем бірліктері (Тест)",
    "5. Ақпаратты өлшеу",
    "6. Мәтіндік ақпаратты және монохромды кескіндерді (ASCII, Unicode) кодтау (Сәйкестендіру)",
    "7. Мәтіндік ақпаратты және монохромды кескіндерді (ASCII, Unicode) кодтау. Практикалық жұмыс",
    "8. Үш өлшемді графика редакторы",
    "9. Үш өлшемді графика редакторы. Бекіту және қолдану (Тест)",
    "10. Нысандардың 3D модельдері (Сәйкестендіру)",
    "11. Нысандардың 3D модельдері. Бекіту және қолдану (Тест)",
    "12. 3D анимация",
    "13. Қорытынды практикалық жоба"
]

st.divider()

# ==========================================
# 👩‍🏫 МҰҒАЛІМ КАБИНЕТІ (SaaS Dashboard)
# ==========================================
if mode == "👩‍🏫 Мұғалім кабинеті (SaaS Dashboard)":
    st.markdown("### 📊 Teacher Analytics & Control Center")
    
    with st.expander("📈 Сыныптар мен оқушылардың рейтингтік нәтижелері", expanded=True):
        col_d1, col_d2 = st.columns([2, 1])
        with col_d1:
            selected_class = st.selectbox("Сыныпты таңдаңыз:", st.session_state.classes_list)
        with col_d2:
            new_class_name = st.text_input("Жаңа сынып қосу (мысалы: 7 «Б»):")
            if st.button("Сыныпты қосу"):
                if new_class_name and new_class_name not in st.session_state.classes_list:
                    st.session_state.classes_list.append(new_class_name)
                    st.success(f"✅ {new_class_name} сәтті қосылды!")
                    st.rerun()
                elif not new_class_name:
                    st.warning("⚠️ Сынып атын жазыңыз!")
                else:
                    st.info("ℹ️ Бұл сынып тізімде бар.")
                    
        st.info(f"🏫 Атырау облысы, Аққыстау орта мектебі | Белсенді сынып: **{selected_class}**")

        st.markdown(f"#### 📋 **{selected_class}** оқушыларының тапсырма нәтижелері:")
        
        if selected_class in st.session_state.results_db and len(st.session_state.results_db[selected_class]) > 0:
            st.table(st.session_state.results_db[selected_class])
        else:
            st.info(f"ℹ️ {selected_class} бойынша әзірге сақталған нәтижелер жоқ.")

    st.markdown("---")
    st.markdown("### ⚙️ Сабақ баптаулары мен оқушы сілтемесі генераторы")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        save_results = st.toggle("Оқушы нәтижелерін базаға сақтау", value=True)
        selected_topic_teacher = st.selectbox("Тақырыпты таңдаңыз:", topics_list, key="teacher_topic")
    with col_s2:
        lesson_timer = st.number_input("Сабақ таймері (минут):", min_value=5, max_value=45, value=15)
        if save_results:
            st.success("📌 Нәтижелерді сақтау режимі: ҚОСУЛЫ 🟢")
        else:
            st.warning("📌 Нәтижелерді сақтау режимі: ӨШІРУЛІ 🔴")

    st.markdown("#### 🔗 Оқушыларға арналған автоматты сілтеме:")
    app_link = f"https://ustazmentor-7class.streamlit.app/?topic={selected_topic_teacher}&timer={lesson_timer}&save={int(save_results)}"
    st.code(app_link, language="text")

    if st.button("🗑️ Барлық сақталған нәтижелерді тазарту"):
        st.session_state.results_db = {}
        st.success("✨ Дерекқор сәтті тазартылды!")
        st.rerun()

# ==========================================
# 👨‍🎓 ОҚУШЫ РЕЖИМІ (Game Hub)
# ==========================================
else:
    st.markdown("### 🎮 Оқушы режимі: Тапсырмалар әлемі")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        student_class = st.selectbox("Сыныбыңызды таңдаңыз:", st.session_state.classes_list, key="student_class_select")
    with col_p2:
        student_name = st.text_input("Аты-жөніңізді енгізіңіз:", placeholder="Мысалы: Айдын Әбілқайыр")

    selected_topic = st.selectbox("Өтетін тақырыпты таңдаңыз:", topics_list, key="student_topic")
    st.divider()

    # --- 1-ТАҚЫРЫП (СӘЙКЕСТЕНДІРУ) ---
    if "1." in selected_topic:
        st.markdown("### 🛡️ 1-тақырып: Жеке қауіпсіздік және ондағы сервистік программалардың рөлі")
        st.markdown("**Оқу мақсаты:** 7.4.1.1 — компьютерді және есептік жазбаны сенімді құпиясөздер, екі сатылы аутентификация, антивирустық программалық жасақтама мен деректерді мұрағаттау арқылы қорғауды қамтамасыз ету.")
        st.markdown("**Тапсырма:** Ұғымдарды олардың дұрыс анықтамаларымен сәйкестендіріңіз.")
        
        match_opts1 = [
            "Таңдаңыз...",
            "A) Файлдардың көлемін азайтуға және оларды бір архивке жинауға арналған үдеріс",
            "B) Компьютерді вирустардан және зиянды программалардан қорғайтын программа",
            "C) Әріптерден, сандардан және арнайы таңбалардан тұратын күрделі құпиясөз",
            "D) Пайдаланушының жеке басын екі түрлі тәсіл арқылы тексеру",
            "E) Ақпарат жоғалған жағдайда оны қалпына келтіру үшін сақталған деректер көшірмесі"
        ]
        
        ans1_1 = st.selectbox("1. Сенімді құпиясөз", match_opts1, key="m1_1")
        ans1_2 = st.selectbox("2. Екі сатылы аутентификация", match_opts1, key="m1_2")
        ans1_3 = st.selectbox("3. Антивирустық программа", match_opts1, key="m1_3")
        ans1_4 = st.selectbox("4. Деректерді мұрағаттау", match_opts1, key="m1_4")
        ans1_5 = st.selectbox("5. Резервтік көшірме", match_opts1, key="m1_5")

        if st.button("Нәтижені тексеру", key="chk_btn_m1"):
            if not student_name.strip():
                st.warning("⚠️ Нәтижені сақтау үшін аты-жөніңізді енгізіңіз!")
            else:
                score1 = 0
                if "C) Әріптерден" in ans1_1: score1 += 2
                if "D) Пайдаланушының жеке басын" in ans1_2: score1 += 2
                if "B) Компьютерді вирустардан" in ans1_3: score1 += 2
                if "A) Файлдардың көлемін" in ans1_4: score1 += 2
                if "E) Ақпарат жоғалған жағдайда" in ans1_5: score1 += 2
                
                result_entry = {
                    "Оқушы аты": student_name,
                    "Тақырып": "1-тақырып",
                    "Ұпай": f"{score1} / 10",
                    "Уақыты": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                if student_class not in st.session_state.results_db:
                    st.session_state.results_db[student_class] = []
                st.session_state.results_db[student_class].append(result_entry)
                
                st.success(f"🎉 Керемет! {student_class} оқушысы **{student_name}**, сіз 10 ұпайдан **{score1} ұпай** жинадыңыз! 🚀")

    # --- 2-ТАҚЫРЫП (ТЕСТ) ---
    elif "2." in selected_topic:
        st.markdown("### 🛡️ 2-тақырып: Жеке қауіпсіздік және ондағы сервистік программалардың рөлі (Тест)")
        
        q1 = st.radio("1. Айдана әлеуметтік желіге тіркеліп, жеке парақшасын бөтен адамдардың бұзуынан қорғағысы келеді. Қай құпиясөзді таңдағаны дұрыс?", [
            "А) Өзінің аты мен туған жылын жазу", "Б) «12345678» комбинациясын қолдану", "В) Бас және кіші әріптерді, сандар мен арнайы символдарды араластырып, ұзын әрі бірегей құпиясөз жасау", "Г) Досының есімін жазу"
        ], key="t2_1")
        
        q2 = st.radio("2. Даниярдың банк қосымшасына басқа адам кірмек болды. Қосымша құпиясөзден бөлек оның телефонына бір реттік SMS-код жіберді. Бұл қандай қауіпсіздік тәсілі?", [
            "А) Антивирустық қорғаныс", "Б) Екі сатылы аутентификация (2FA)", "В) Деректерді мұрағаттау", "Г) Мәтінді кодтау"
        ], key="t2_2")
        
        q3 = st.radio("3. Мектеп компьютерінде белгісіз файл ашылғаннан кейін компьютер баяу жұмыс істей бастады. Оқушы компьютерді зиянды бағдарламаларға тексеру үшін қандай сервистік программаны қолдануы керек?", [
            "А) Мәтіндік редактор", "Б) Антивирустық бағдарламалық жасақтама", "В) 3D графика редакторы", "Г) Кестелік процессор"
        ], key="t2_3")

        q4 = st.radio("4. Әсел информатика пәнінен жасаған жобасын компьютерде сақтады. Компьютері істен шыққан жағдайда жұмысын жоғалтпау үшін ол жобаның көшірмесін бұлттық қоймаға сақтады. Бұл әрекет қалай аталады?", [
            "А) Резервтік көшірме жасау (Backup)", "Б) Форматтау", "В) Вирусты жұқтыру", "Г) Декодтау"
        ], key="t2_4")

        q5 = st.radio("5. Оқушыға «Сіз бағалы сыйлық ұтып алдыңыз! Сыйлықты алу үшін банк картаңыздың деректерін енгізіңіз» деген электрондық хат келді. Ол не істеуі керек?", [
            "А) Барлық жеке мәліметтерін бірден жіберу", "Б) Хаттың күдікті екенін түсініп, сілтемені ашпау және жеке деректерін енгізбеу", "В) Хатты сыныптастарына тарату", "Г) Сыйлықты алу үшін барлық сілтемені ашу"
        ], key="t2_5")

        q6 = st.radio("6. Мектеп компьютеріндегі операциялық жүйе мен антивирус біраз уақыттан бері жаңартылмаған. Оларды жаңарту не үшін қажет?", [
            "А) Компьютердің сыртқы түрін өзгерту үшін", "Б) Қауіпсіздік осалдықтарын түзетіп, жаңа қауіптерден қорғану үшін", "В) Интернет жылдамдығын азайту үшін", "Г) Құжаттардың барлығын автоматты түрде өшіру үшін"
        ], key="t2_6")

        q7 = st.radio("7. Мектептегі Wi-Fi желісіне бөгде адамдардың қосылмауы үшін желі әкімшісі қандай шара қолдануы керек?", [
            "А) Желіге күрделі құпиясөз орнатып, қауіпсіздік баптауларын реттеу", "Б) Роутерді үнемі өшіріп қою", "В) Интернетті мүлдем қолданбау", "Г) Барлық компьютерді ауыстыру"
        ], key="t2_7")

        q8 = st.radio("8. Информатика мұғалімі мектеп компьютерлерінің тұрақты жұмыс істеуін және вирустардан қорғалуын қамтамасыз еткісі келеді. Сервистік программалардың негізгі қызметі қандай?", [
            "А) Тек ойын ойнауға мүмкіндік беру", "Б) Компьютердің жұмысын баптау, қорғау және оған қызмет көрсету", "В) Музыка жазу", "Г) Сурет салу"
        ], key="t2_8")

        q9 = st.radio("9. Оқушының электрондық поштасына белгісіз жіберушіден файл келді. Ол файлдың қауіпсіз екеніне көз жеткізу үшін не істеуі керек?", [
            "А) Файлды бірден ашу", "Б) Жіберушіні тексеріп, файлды қауіпсіздік бағдарламасымен тексеру", "В) Файлды барлық достарына жіберу", "Г) Файлдың атауына қарап, оны міндетті түрде қауіпсіз деп санау"
        ], key="t2_9")

        q10 = st.radio("10. Сынып оқушылары ортақ компьютерде жоба жасап жатыр. Олар өздерінің жеке деректерін қорғап, қауіпсіз жұмыс істеуі үшін қандай әрекеттерді орындауы керек?", [
            "А) Жеке деректерді қорғау, сенімді құпиясөз қолдану және күдікті сілтемелерді ашпау", "Б) Құпиясөздерін барлығына жариялау", "В) Белгісіз файлдарды тексерусіз жүктеу", "Г) Жеке деректерін кез келген сайтқа енгізу"
        ], key="t2_10")

        if st.button("Нәтижені тексеру", key="chk_btn_2"):
            if not student_name.strip():
                st.warning("⚠️ Нәтижені сақтау үшін аты-жөніңізді енгізіңіз!")
            else:
                score = 0
                if "Бас және кіші әріптерді" in q1: score += 1
                if "Екі сатылы аутентификация" in q2: score += 1
                if "Антивирустық бағдарламалық" in q3: score += 1
                if "Резервтік көшірме жасау" in q4: score += 1
                if "Хаттың күдікті екенін" in q5: score += 1
                if "Қауіпсіздік осалдықтарын" in q6: score += 1
                if "Желіге күрделі құпиясөз" in q7: score += 1
                if "Компьютердің жұмысын баптау" in q8: score += 1
                if "Жіберушіні тексеріп" in q9: score += 1
                if "Жеке деректерді қорғау" in q10: score += 1
                
                result_entry = {
                    "Оқушы аты": student_name,
                    "Тақырып": "2-тақырып (Тест)",
                    "Ұпай": f"{score} / 10",
                    "Уақыты": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                if student_class not in st.session_state.results_db:
                    st.session_state.results_db[student_class] = []
                st.session_state.results_db[student_class].append(result_entry)
                
                st.success(f"🎉 Жарайсың, {student_class} оқушысы **{student_name}**! 10 ұпайдан **{score} ұпай** жинадыңыз! 🌟")

    # --- 3-ТАҚЫРЫП ---
    elif "3." in selected_topic:
        st.markdown("### 📖 3-тақырып: Ақпараттың өлшем бірліктері")
        st.markdown("**Оқу мақсаты:** 7.2.1.1 — ақпаратты бір өлшем бірліктен басқа өлшем бірлікке аударуды жүзеге асыру.")
        st.markdown("Төмендегі батырманы басып, интерактивті **«Смартфон жадын сақтау операциясы»** кейс-ойынын ойнаңыз:")
        st.link_button("🚀 3-тақырып ойынын ашу", "https://aliyateacher80-design.github.io/game-3topic/")

    # --- 4-ТАҚЫРЫП (ТЕСТ) ---
    elif "4." in selected_topic:
        st.markdown("### 📊 4-тақырып: Ақпараттың өлшем бірліктері")
        
        q1 = st.radio("1. Компьютер жадында ақпараттың ең кіші өлшем бірлігі қандай?", ["А) Байт", "Б) Бит", "В) Килобайт", "Г) Мегабайт"], key="t4_1")
        q2 = st.radio("2. Бір байт неше биттен тұрады?", ["А) 2 бит", "Б) 8 бит", "В) 1024 бит", "Г) 16 бит"], key="t4_2")
        q3 = st.radio("3. 1 КБ шамамен қанша байтқа тең?", ["А) 100 байт", "Б) 512 байт", "В) 1024 байт", "Г) 2048 байт"], key="t4_3")
        q4 = st.radio("4. 4 ГБ бос орынға 1 ГБ болатын неше фильм сақтауға болады?", ["А) 2 фильм", "Б) 4 фильм", "В) 8 фильм", "Г) 10 фильм"], key="t4_4")
        q5 = st.radio("5. Өлшем бірліктерінің дұрыс реті:", ["А) Байт → Килобайт → Мегабайт → Гигабайт", "Б) Гигабайт → Мегабайт → Килобайт → Байт", "В) Бит → Байт → Гигабайт → Килобайт", "Г) Мегабайт → Бит → Байт → Гигабайт"], key="t4_5")
        q6 = st.radio("6. Әрқайсысы 2 МБ болатын 5 суреттің жалпы көлемі?", ["А) 5 МБ", "Б) 10 МБ", "В) 20 МБ", "Г) 2 МБ"], key="t4_6")
        q7 = st.radio("7. 3 МБ-ты килобайтқа айналдыру үшін қандай амал қолданылады?", ["А) 1024-ке бөлу", "Б) 1024-ке көбейту", "В) 8-ге бөлу", "Г) Өзгертпеу"], key="t4_7")
        q8 = st.radio("8. 16 ГБ флешкаға 512 МБ болатын неше альбом сыяды?", ["А) 16 альбом", "Б) 32 альбом", "В) 64 альбом", "Г) 10 альбом"], key="t4_8")
        q9 = st.radio("9. Қарапайым бірбайттық кодтауда бір әріп қанша орын алады?", ["А) 1 байт", "Б) 1 мегабайт", "В) 1 килобайт", "Г) 1 гигабайт"], key="t4_9")
        q10 = st.radio("10. Төмендегі қайсысы ақпарат көлемін өлшеу бірлігі?", ["А) Секунд", "Б) Градус", "В) Мегабайт", "Г) Метр"], key="t4_10")

        if st.button("Нәтижені тексеру", key="chk_btn_4"):
            if not student_name.strip():
                st.warning("⚠️ Нәтижені сақтау үшін аты-жөніңізді енгізіңіз!")
            else:
                score = 0
                if "Бит" in q1: score += 1
                if "8 бит" in q2: score += 1
                if "1024 байт" in q3: score += 1
                if "4 фильм" in q4: score += 1
                if "Байт → Килобайт" in q5: score += 1
                if "10 МБ" in q6: score += 1
                if "1024-ке көбейту" in q7: score += 1
                if "32 альбом" in q8: score += 1
                if "1 байт" in q9: score += 1
                if "Мегабайт" in q10: score += 1
                
                result_entry = {
                    "Оқушы аты": student_name,
                    "Тақырып": "4-тақырып (Тест)",
                    "Ұпай": f"{score} / 10",
                    "Уақыты": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                if student_class not in st.session_state.results_db:
                    st.session_state.results_db[student_class] = []
                st.session_state.results_db[student_class].append(result_entry)
                
                st.success(f"🎉 Керемет! **{student_name}**, сіз 10 ұпайдан **{score} ұпай** жинадыңыз!")

    # --- 5-ТАҚЫРЫП ---
    elif "5." in selected_topic:
        st.markdown("### 🚀 5-тақырып: Ақпаратты өлшеу")
        st.markdown("**Оқу мақсаты:** 7.2.1.2 — алфавиттік тәсілді қолданып ақпарат көлемін анықтау.")
        st.markdown("Төмендегі батырманы басып, ғарыштық аркада ойынын ойнаңыз:")
        st.link_button("🚀 5-тақырып ойынын ашу", "https://aliyateacher80-design.github.io/raketa-game/")

    # --- 6-ТАҚЫРЫП (СӘЙКЕСТЕНДІРУ) ---
    elif "6." in selected_topic:
        st.markdown("### 🔤 6-тақырып: Мәтіндік ақпаратты және монохромды кескіндерді (ASCII, Unicode) кодтау")
        st.markdown("**Оқу мақсаты:** 7.2.1.3 — мәтіндік ақпаратты және монохромды кескіндерді кодтау және декодтау алгоритмдерін қолдану.")
        st.markdown("**Тапсырма:** Ұғымдарды олардың дұрыс анықтамаларымен сәйкестендіріңіз.")
        
        match_opts6 = [
            "Таңдаңыз...",
            "A) Кодталған ақпаратты бастапқы қалпына келтіру үдерісі",
            "B) Әртүрлі тілдердің таңбаларын қамтитын әмбебап кодтау стандарты",
            "C) Ақпаратты белгілі бір ережелер бойынша кодтармен көрсету үдерісі",
            "D) Мәтіндік таңбаларды кодтауға арналған таңбалар стандарты",
            "E) Тек екі түстен, әдетте ақ және қара түстерден тұратын кескін"
        ]
        
        ans6_1 = st.selectbox("1. Кодтау", match_opts6, key="m6_1")
        ans6_2 = st.selectbox("2. Декодтау", match_opts6, key="m6_2")
        ans6_3 = st.selectbox("3. ASCII", match_opts6, key="m6_3")
        ans6_4 = st.selectbox("4. Unicode", match_opts6, key="m6_4")
        ans6_5 = st.selectbox("5. Монохромды кескін", match_opts6, key="m6_5")

        if st.button("Нәтижені тексеру", key="chk_btn_m6"):
            if not student_name.strip():
                st.warning("⚠️ Нәтижені сақтау үшін аты-жөніңізді енгізіңіз!")
            else:
                score6 = 0
                if "C) Ақпаратты белгілі бір" in ans6_1: score6 += 2
                if "A) Кодталған ақпаратты" in ans6_2: score6 += 2
                if "D) Мәтіндік таңбаларды" in ans6_3: score6 += 2
                if "B) Әртүрлі тілдердің" in ans6_4: score6 += 2
                if "E) Тек екі түстен" in ans6_5: score6 += 2
                
                result_entry = {
                    "Оқушы аты": student_name,
                    "Тақырып": "6-тақырып",
                    "Ұпай": f"{score6} / 10",
                    "Уақыты": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                if student_class not in st.session_state.results_db:
                    st.session_state.results_db[student_class] = []
                st.session_state.results_db[student_class].append(result_entry)
                
                st.success(f"🎉 Жұлдызды нәтиже! **{student_name}**, сіз 10 ұпайдан **{score6} ұпай** жинадыңыз!")

    # --- 7-ТАҚЫРЫП ---
    elif "7." in selected_topic:
        st.markdown("### 💻 7-тақырып: Мәтіндік ақпаратты және монохромды кескіндерді (ASCII, Unicode) кодтау. Практикалық жұмыс")
        st.markdown("**Оқу мақсаты:** 7.2.1.3 — мәтіндік ақпаратты және монохромды кескіндерді кодтау және декодтау алгоритмдерін қолдану.")
        st.markdown("Төмендегі батырманы басып, **ASCII & Pixel Hacker** ойынын ойнаңыз:")
        st.link_button("💻 7-тақырып ойынын ашу", "https://aliyateacher80-design.github.io/kod-game-7/")

    # --- 8-ТАҚЫРЫП ---
    elif "8." in selected_topic:
        st.markdown("### 🧊 8-тақырып: Үш өлшемді графика редакторы")
        st.markdown("**Оқу мақсаты:** 7.3.2.1 — компьютерлік модельдерді қолдануға мысалдар келтіру.")
        st.markdown("Төмендегі батырманы басып, **3D Cyber Architect** ойынын ойнаңыз:")
        st.link_button("🧊 8-тақырып ойынын ашу", "https://aliyateacher80-design.github.io/space_architect_game/")

    # --- 9-ТАҚЫРЫП (ТЕСТ) ---
    elif "9." in selected_topic:
        st.markdown("### 🧊 9-тақырып: Үш өлшемді графика редакторы. Бекіту және қолдану")
        
        q1 = st.radio("1. 3D графиканың 2D графикадан негізгі айырмашылығы неде?", ["А) Тек ақ-қара түспен беріледі", "Б) Кеңістіктегі тереңдік өлшемі (Z осі) бар", "В) Әрқашан баяу жұмыс істейді", "Г) Тек мәтін жазуға арналған"], key="t9_1")
        q2 = st.radio("2. Ғимараттың ішкі көрінісін компьютерде көлемді түрде жасап көрсету не деп аталады?", ["А) Компьютерлік модельдеу", "Б) Мәтіндік кодтау", "В) Антивирустық тексеру", "Г) Файлдарды мұрағаттау"], key="t9_2")
        q3 = st.radio("3. 3D редакторында қандай координаттар жүйесі қолданылады?", ["А) X және Y", "Б) X, Y және Z", "В) Тек Z", "Г) A, B, C"], key="t9_3")
        q4 = st.radio("4. Модельдегі заттардың көлеңкесі шынайы көрінуі үшін не істеу керек?", ["А) Жарық көздерін орнатып, жарық пен көлеңке параметрлерін реттеу", "Б) Компьютерді қатыру", "В) Файл көлемін азайту", "Г) Барлық нысанды қараңғы ету"], key="t9_4")
        q5 = st.radio("5. 3D модельдеуді қай салада қолдануға болады?", ["А) Дизайн, сәулет және құрылыс жобалау салаларында", "Б) Тек мәтін теруде", "В) Кесте жасауда ғана", "Г) Электрондық хат жіберуде ғана"], key="t9_5")
        q6 = st.radio("6. Камера көрінісі (Camera view) қандай қызмет атқарады?", ["А) Модельдің камера түсіретін көрінісін алдын ала қарауға мүмкіндік береді", "Б) Пернетақтаны тексереді", "В) Интернетке қосады", "Г) Дыбысты реттейді"], key="t9_6")
        q7 = st.radio("7. 3D модельді басқа бағдарламаға тасымалдау форматы?", ["А) .obj, .fbx, .stl", "Б) .txt, .doc", "В) .mp3, .wav", "Г) .mp4"], key="t9_7")
        q8 = st.radio("8. Нысанның бетіне ағаш түсі мен өрнегін беру үшін қандай әрекет орындалады?", ["А) Материал немесе текстура қолдану", "Б) Модельді өшіру", "В) Модельді кодтау", "Г) Файлды мұрағаттау"], key="t9_8")
        q9 = st.radio("9. Компьютерлік модельдеудің басты артықшылығы неде?", ["А) Қымбат материалдарды пайдаланбай тұрып, жобадағы қателерді анықтауға мүмкіндік береді", "Б) Интернетті өшіреді", "В) Компьютерді өшірмеуге рұқсат береді", "Г) Қағаз шығынын көбейтеді"], key="t9_9")
        q10 = st.radio("10. 3D модель жасауға арналған бағдарламаны атаңыз:", ["А) Blender немесе 3ds Max", "Б) Microsoft Paint", "В) Notepad", "Г) Calculator"], key="t9_10")

        if st.button("Нәтижені тексеру", key="chk_btn_9"):
            if not student_name.strip():
                st.warning("⚠️ Нәтижені сақтау үшін аты-жөніңізді енгізіңіз!")
            else:
                score = 0
                if "Кеңістіктегі тереңдік" in q1: score += 1
                if "Компьютерлік модельдеу" in q2: score += 1
                if "X, Y және Z" in q3: score += 1
                if "Жарық көздерін орнатып" in q4: score += 1
                if "Дизайн, сәулет және құрылыс" in q5: score += 1
                if "Модельдің камера түсіретін" in q6: score += 1
                if ".obj, .fbx, .stl" in q7: score += 1
                if "Материал немесе текстура" in q8: score += 1
                if "Қымбат материалдарды" in q9: score += 1
                if "Blender немесе 3ds Max" in q10: score += 1
                
                result_entry = {
                    "Оқушы аты": student_name,
                    "Тақырып": "9-тақырып",
                    "Ұпай": f"{score} / 10",
                    "Уақыты": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                if student_class not in st.session_state.results_db:
                    st.session_state.results_db[student_class] = []
                st.session_state.results_db[student_class].append(result_entry)
                
                st.success(f"🎉 Тамаша! **{student_name}**, сіз 10 ұпайдан **{score} ұпай** жинадыңыз!")

    # --- 10-ТАҚЫРЫП (СӘЙКЕСТЕНДІРУ) ---
    elif "10." in selected_topic:
        st.markdown("### 📐 10-тақырып: Нысандардың 3D модельдері")
        st.markdown("**Нұсқаулық:** Практикалық жағдаяттарды 3D модельдеу құралдарымен және әрекеттерімен сәйкестендіріңіз.")
        
        opts3 = [
            "Таңдаңыз...",
            "А) Move — нысанды жылжыту", "Ә) Scale — нысанның өлшемін өзгерту", "Б) Rotate — нысанды бұру",
            "В) Графикалық примитивтерді қолдану", "Г) Айналу денесін құру", "Ғ) Extrude — нысанның бетін созу",
            "Д) Примитивтерді біріктіріп, күрделі модель жасау", "Е) Нысанның геометриялық элементтерін өңдеу",
            "Ж) Нысанның биіктігі мен радиусын өзгерту", "З) Цилиндр примитивін пайдалану"
        ]
        
        c1 = st.selectbox("1. Оқушы 3D редакторда үстелдің аяқтарын жасау үшін цилиндр пішінін таңдады.", opts3, key="m3_1")
        c2 = st.selectbox("2. Дизайнер бөлмедегі орындықты үстелдің жанына орналастыру үшін оның орнын өзгертті.", opts3, key="m3_2")
        c3 = st.selectbox("3. Оқушы жасаған 3D орындықтың өлшемін кішірейтіп, макетке сәйкестендірді.", opts3, key="m3_3")
        c4 = st.selectbox("4. Дизайнер құмыраның көлемді моделін жасау үшін оның қимасын ось бойымен айналдырды.", opts3, key="m3_4")
        c5 = st.selectbox("5. Оқушы үстелдің үстіңгі тақтайын сыртқа қарай созып, оның пішінін өзгертті.", opts3, key="m3_5")
        c6 = st.selectbox("6. Дизайнер орындықты үстелге қаратып бұру үшін арнайы құралды қолданды.", opts3, key="m3_6")
        c7 = st.selectbox("7. Оқушы үстелдің моделін куб пен бірнеше цилиндрді біріктіру арқылы жасады.", opts3, key="m3_7")
        c8 = st.selectbox("8. Дизайнер цилиндр пішінді ыдыстың биіктігі мен жуандығын өзгерту үшін оның параметрлерін реттеді.", opts3, key="m3_8")
        c9 = st.selectbox("9. Оқушы 3D модельдің жекелеген төбелерін, қабырғалары мен беттерін таңдап өңдеді.", opts3, key="m3_9")
        c10 = st.selectbox("10. Оқушы дөңгелек шамның көлемді моделін жасау үшін цилиндрдің үстіңгі және астыңғы бөліктерін өңдеді.", opts3, key="m3_10")

        if st.button("Нәтижені тексеру", key="chk_m3"):
            if not student_name.strip():
                st.warning("⚠️ Нәтижені сақтау үшін аты-жөніңізді енгізіңіз!")
            else:
                score = 0
                if "З) Цилиндр примитивін пайдалану" in c1: score += 1
                if "А) Move — нысанды жылжыту" in c2: score += 1
                if "Ә) Scale — нысанның өлшемін өзгерту" in c3: score += 1
                if "Г) Айналу денесін құру" in c4: score += 1
                if "Ғ) Extrude — нысанның бетін созу" in c5: score += 1
                if "Б) Rotate — нысанды бұру" in c6: score += 1
                if "Д) Примитивтерді біріктіріп" in c7: score += 1
                if "Ж) Нысанның биіктігі мен радиусын" in c8: score += 1
                if "Е) Нысанның геометриялық" in c9: score += 1
                if "В) Графикалық примитивтерді" in c10: score += 1
                
                result_entry = {
                    "Оқушы аты": student_name,
                    "Тақырып": "10-тақырып",
                    "Ұпай": f"{score} / 10",
                    "Уақыты": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                if student_class not in st.session_state.results_db:
                    st.session_state.results_db[student_class] = []
                st.session_state.results_db[student_class].append(result_entry)
                
                st.success(f"🎉 Керемет! **{student_name}**, сіз 10 ұпайдан **{score} ұпай** жинадыңыз!")

    # --- 11-ТАҚЫРЫП (ТЕСТ) ---
    elif "11." in selected_topic:
        st.markdown("### 📐 11-тақырып: Нысандардың 3D модельдері. Бекіту және қолдану")
        
        q1 = st.radio("1. 3D редактордағы куб, цилиндр, сфера сияқты қарапайым геометриялық фигуралар қалай аталады?", ["А) Примитивтер", "Б) Текстуралар", "В) Анимациялар", "Г) Рендерлер"], key="t11_1")
        q2 = st.radio("2. 3D нысанның бетіне түс немесе сурет (өрнек) беру үшін не қолданылады?", ["А) Материал және текстура", "Б) Камера", "В) Жарық көзі", "Г) Тор (Mesh)"], key="t11_2")
        q3 = st.radio("3. 3D модельді әр түрлі бұрыштан көру үшін қандай құрал қолданылады?", ["А) Айналдыру (Orbit/Rotate view)", "Б) Өшіру", "В) Сақтау", "Г) Мұрағаттау"], key="t11_3")
        q4 = st.radio("4. 3D редакторында нысанның көлемін бір бағытта немесе барлық бағытта үлкейту/кішірейту құралы:", ["А) Scale", "Б) Move", "В) Rotate", "Г) Extrude"], key="t11_4")
        q5 = st.radio("5. Нысанды кеңістікте бір орыннан екінші орынға жылжыту командасы:", ["А) Move", "Б) Scale", "В) Render", "Г) Group"], key="t11_5")
        q6 = st.radio("6. Дайын 3D үлгіні шынайы сурет немесе видео түріне айналдыру үдерісі:", ["А) Рендеринг (Rendering)", "Б) Архивация", "В) Кодтау", "Г) Форматтау"], key="t11_6")
        q7 = st.radio("7. 3D графикада жарықтың дұрыс түсуі не үшін маңызды?", ["А) Нысанның көлемді әрі шынайы көрінуі үшін", "Б) Компьютерді қатыру үшін", "В) Файл өлшемін ұлғайту үшін", "Г) Түстерді өшіру үшін"], key="t11_7")
        q8 = st.radio("8. 3D модельдеу кезінде нысанды бірнеше бөлікке бөлу немесе оның пішінін өзгерту үшін не қолданылады?", ["А) Төбелерді, қабырғаларды және беттерді өңдеу (Edit mode)", "Б) Компьютерді қайта қосу", "В) Интернетті өшіру", "Г) Дыбысты қосу"], key="t11_8")
        q9 = st.radio("9. Архитекторлар мен дизайнерлер жаңа үйдің немесе бөлменің жобасын 3D форматта не үшін жасайды?", ["А) Құрылысты бастамас бұрын қателерді көріп, жобаны визуализациялау үшін", "Б) Тек уақыт өткізу үшін", "В) Қағаз шығынын арттыру үшін", "Г) Интернетті жылдамдату үшін"], key="t11_9")
        q10 = st.radio("10. 3D модельдеу бағдарламаларында көріністі басқару үшін негізінен не қолданылады?", ["А) Тінтуір (мышь) және пернетақта", "Б) Тек принтер", "В) Тек сканер", "Г) Колонна"], key="t11_10")

        if st.button("Нәтижені тексеру", key="chk_btn_11"):
            if not student_name.strip():
                st.warning("⚠️ Нәтижені сақтау үшін аты-жөніңізді енгізіңіз!")
            else:
                score = 0
                if "Примитивтер" in q1: score += 1
                if "Материал және текстура" in q2: score += 1
                if "Айналдыру" in q3: score += 1
                if "Scale" in q4: score += 1
                if "Move" in q5: score += 1
                if "Рендеринг" in q6: score += 1
                if "Нысанның көлемді" in q7: score += 1
                if "Төбелерді, қабырғаларды" in q8: score += 1
                if "Құрылысты бастамас бұрын" in q9: score += 1
                if "Тінтуір" in q10: score += 1
                
                result_entry = {
                    "Оқушы аты": student_name,
                    "Тақырып": "11-тақырып (Тест)",
                    "Ұпай": f"{score} / 10",
                    "Уақыты": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                if student_class not in st.session_state.results_db:
                    st.session_state.results_db[student_class] = []
                st.session_state.results_db[student_class].append(result_entry)
                
                st.success(f"🎉 Керемет! **{student_name}**, сіз 10 ұпайдан **{score} ұпай** жинадыңыз!")

    # --- 12-ТАҚЫРЫП ---
    elif "12." in selected_topic:
        st.markdown("### 🎬 12-тақырып: 3D анимация")
        st.markdown("**Оқу мақсаты:** 7.3.2.2 — 3D анимация құру принциптерін түсіну және қолдану.")
        st.markdown("Төмендегі батырманы басып, интерактивті **3D Animation** ойынын ойнаңыз:")
        st.link_button("🎬 12-тақырып ойынын ашу", "https://aliyateacher80-design.github.io/animation-game-7/")

    # --- 13-ТАҚЫРЫП ---
    elif "13." in selected_topic:
        st.markdown("### 🏆 13-тақырып: Қорытынды практикалық жоба")
        st.markdown("**Оқу мақсаты:** Барлық өткен модульдер бойынша алған білімді практикада жинақтау.")
        st.markdown("Төмендегі батырманы басып, қорытынды жоба тапсырмасын орындаңыз:")
        st.link_button("🚀 Қорытынды жобаны ашу", "https://aliyateacher80-design.github.io/final-project-7/")
