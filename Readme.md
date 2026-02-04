# РуСлог / RusLyric Hyphenator

Профессиональная утилита для автоматической подготовки русского вокального текста к вставке в нотные редакторы (Sibelius, Finale).

### О программе
В нотаторах Сибелиус и Финал нет деления на слоги русских слов. Для вставки в ноты слогов на русском приходится самому делить слова на слоги, либо обращаться к специальным сервисам или нейросетям. Любой из этих способов неудобный и затратный по времени. Также, после самостоятельного деления на слоги возникают другие проблемы при вставке их в ноты – при наличии в тексте предлогов «в», «к», «с», а также частиц «ж», «ль», «б» нотатор, после вставки этих предлогов или частиц, автоматически перебрасывает на следующую ноту. Это заставляет возвращаться к предлогу/частице и использовать неразрывный пробел (ещё одно лишнее действие).

**РуСлог** автоматизирует процесс подготовки текста, избавляя от ручной расстановки дефисов и неразрывных пробелов между предлогами и слогами/словами и между словами/слогами и частицами.

### Основные функции:
* **Вокальный слогораздел:** Алгоритм делит слова на слоги, стремясь к "открытым" слогам (оканчивающимся на гласную), что соответствует правилам вокального исполнения.
* **Умная привязка предлогов:** Автоматически объединяет предлоги `в, к, с` со следующим словом через неразрывный пробел. Предлог всегда остается вместе со словом на одной ноте.
* **Работа с частицами:** Частицы `ж, б, ль` привязываются к предыдущему слову/слогу.

### **ВАЖНО:**
**Если у вас Windows 7** и основная версия выдает ошибку (например, api-ms-win-core-path-l1-1-0.dll), **используйте файл с пометкой _Win7**

### Инструкция по применению:
0. **Зайдите в настройки нотатора и обязательно отключите автоматическое разбиение на слоги. В Сибелиусе это находится в Настройки->Другое.
   Справа под надписью "Вставить текст песни из буфера обмена" снять галочку "Автоматически разбивать вставленный текст песни на слоги".
   Если этого не сделать, то алгоритмы сибелиуса начнут мешать правильной вставке неразрывных пробелов для предлога "в" и частиц "б" и "ж", склеивая слово/слог с предлогом/частицей.**
2.	Скопируйте исходный русский текст из любого источника (Word, блокнот, браузер).
3.	Запустите файл `RusLyric_Hyphenator.exe` (ни консоли, ни отображения окна с программой не будет, всё произойдёт в фоновом режиме – отредактированный текст сразу окажется в буфере обмена).
4. Перейдите в нотный редактор, выберите первую ноту и активируйте инструмент ввода текста (Lyrics).
5. Нажимайте `Ctrl+V`. Программа сама расставит слоги по нотам.

Чего НЕ удалось достичь – правильного копирования в ноты начала прямой речи. Т.е. текст типа “«- Деление слов…»” (прямая речь с кавычками) нотатор будет менять на « - Деление слов», а “- Деление слов” (т.е. прямая речь без кавычек), нотатор будет менять на “Деление слов”. Дефис/тире в начале текста он будет игнорировать сразу, «приклеенный» к кавычке дефис/тире он будет разделять пробелом. 
Также была идея создания программы, чтобы она работала в трее. Т.е. после запуска любой скопированный текст сразу делится на слоги и возвращается в буфер обмена. НО такой способ не смог устранить проблему сочетания предлога «в» со словами/слогами начинающимися на «т». Почему в такой версии программы неразрывный пробел (неважно в каком из 3х вариантов) не срабатывает и, например, сочетание «в том» отображается как «втом», что заставляет вернуться к этой ноте и вручную вбивать неразрывный пробел между предлогом и словом/слогом. 

Для разработчиков: Если вы хотите изменить логику слогоделения под свои задачи (например, использовать строгий школьный перенос), вы можете отредактировать соответствующие правила в исходном коде (RusLyric_Hyphenator.py) в секции обработки согласных.

---

### Поддержать проект
Если программа сэкономила вам время и вы хотите поблагодарить автора, вы можете отправить донат на развитие проекта через **ЮMoney**:
* **[Поддержать автора (картой или из кошелька)](https://yoomoney.ru/to/4100118714515464)**

---

English Version (Mirror of the Russian one)

RusLog (RusLyric Hyphenator) A professional utility for automatic preparation of Russian vocal texts for music notation software (Sibelius, Finale).
About the Program

Music notation programs like Sibelius and Finale do not support automatic hyphenation for the Russian language. Users are forced to manually split lyrics into syllables or use external services, which is inconvenient and time-consuming. Additionally, manual hyphenation creates issues with prepositions (в, к, с) and particles (ж, ль, б). By default, notation software moves to the next note after these characters, forcing the user to manually insert non-breaking spaces every single time.

RusLog automates this process, handling both hyphenation and the insertion of non-breaking spaces between prepositions, syllables, and particles.
Key Features:

    1. Vocal Hyphenation: The algorithm follows classical vocal rules, favoring "open" syllables (ending in a vowel).
    2. Smart Preposition Binding: Automatically binds prepositions в, к, с to the following word using a non-breaking space. The preposition always stays on the same note as the word.
    3. Particle Handling: Particles ж, б, ль are automatically bound to the preceding word/syllable.

    IMPORTANT: If you are using Windows 7 and the main version shows an error (e.g., api-ms-win-core-path-l1-1-0.dll), please use the file marked _Win7.

Instructions for Use:

    Notation Software Settings: 
    0. You must disable automatic syllabification. In Sibelius, go to Preferences -> Other. Under the "Paste lyrics from clipboard" section, uncheck "Split pasted lyrics into syllables automatically". Otherwise, Sibelius's internal algorithms will interfere with the correct insertion of non-breaking spaces, merging prepositions and particles incorrectly.
    1. Copy Source Text: Copy your Russian text from any document (Word, Notepad, Browser).
    2. Run the Utility: Run RusLyric_Hyphenator.exe. The program runs silently in the background; there is no window. Your clipboard will be updated instantly.
    3. Paste into Notation Software: Select the first note, activate the Lyrics tool, and press Ctrl+V. The program will automatically distribute the syllables across the notes.

Known Limitations:

The program currently cannot correctly handle the beginning of direct speech. For example, text like «- Syllable...» (direct speech with quotes) will be changed by the notation software to « - Syllable», and - Syllable (without quotes) will become Syllable. The notation software ignores the leading hyphen/dash or separates it with a space.
For Developers:

If you wish to modify the hyphenation logic (e.g., to use strict school-style rules), you can edit the rules in the source code (RusLyric_Hyphenator.py) in the consonant processing section.
---

### Support the Project
If you find this tool useful and would like to support the developer, you can make a donation via **Yoomoney** (supports bank cards):
* **[Donate via Yoomoney](https://yoomoney.ru/to/4100118714515464)**











